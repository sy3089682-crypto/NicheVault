#!/usr/bin/env python3
"""NicheVault server — serves static files + email capture API endpoint."""
import http.server
import json
import os
import sys
from urllib.parse import urlparse

SIGNUPS_FILE = "/tmp/nichevault-signups.json"
STATIC_DIR = "/home/team/shared/site"

class NicheVaultHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        if self.path == "/api/subscribe":
            content_length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(content_length)
            try:
                data = json.loads(body)
                first_name = data.get("firstName", "").strip()
                email = data.get("email", "").strip()
                if not first_name or not email:
                    self._json_response(400, {"error": "Name and email required"})
                    return
                # Load existing signups
                signups = []
                if os.path.exists(SIGNUPS_FILE):
                    with open(SIGNUPS_FILE, "r") as f:
                        try:
                            signups = json.load(f)
                        except json.JSONDecodeError:
                            signups = []
                # Check for duplicate
                if any(s.get("email") == email for s in signups):
                    self._json_response(200, {"message": "You're already on the list!"})
                    return
                # Add new signup
                signup = {
                    "firstName": first_name,
                    "email": email,
                    "lastName": data.get("lastName", ""),
                    "interest": data.get("interest", ""),
                    "timestamp": __import__("datetime").datetime.now().isoformat()
                }
                signups.append(signup)
                with open(SIGNUPS_FILE, "w") as f:
                    json.dump(signups, f, indent=2)
                count = len(signups)
                self._json_response(200, {
                    "message": "You're on the list! Check your inbox for your free niche sample.",
                    "count": count
                })
            except (json.JSONDecodeError, KeyError) as e:
                self._json_response(400, {"error": f"Invalid data: {e}"})
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'{"error": "Not found"}')

    def _json_response(self, status, data):
        self.send_response(status)
        self.send_header("Content-Type", "application/json")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        self.wfile.write(json.dumps(data).encode())

    def do_OPTIONS(self):
        if self.path == "/api/subscribe":
            self.send_response(200)
            self.send_header("Access-Control-Allow-Origin", "*")
            self.send_header("Access-Control-Allow-Methods", "POST, OPTIONS")
            self.send_header("Access-Control-Allow-Headers", "Content-Type")
            self.end_headers()

    def do_GET(self):
        # Serve static files
        parsed = urlparse(self.path)
        if parsed.path.startswith("/api/"):
            if parsed.path == "/api/count":
                count = 0
                if os.path.exists(SIGNUPS_FILE):
                    with open(SIGNUPS_FILE, "r") as f:
                        try:
                            signups = json.load(f)
                            count = len(signups)
                        except:
                            pass
                self._json_response(200, {"count": count})
                return
            self._json_response(404, {"error": "Not found"})
            return
        return super().do_GET()

    def translate_path(self, path):
        # Serve from STATIC_DIR
        parsed = urlparse(path)
        path = parsed.path
        if not path or path == "/":
            path = "/index.html"
        # Strip leading slash, join with static dir
        rel_path = path.lstrip("/")
        full_path = os.path.join(STATIC_DIR, rel_path)
        return full_path


if __name__ == "__main__":
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 8080
    server = http.server.HTTPServer(("0.0.0.0", port), NicheVaultHandler)
    print(f"NicheVault server running on http://0.0.0.0:{port}")
    print(f"Serving static files from: {STATIC_DIR}")
    print(f"Signups saved to: {SIGNUPS_FILE}")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down...")
        server.server_close()