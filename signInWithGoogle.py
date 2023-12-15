import json
import subprocess
import threading
import webbrowser
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs, unquote
from google_auth_oauthlib.flow import InstalledAppFlow


class MyRequestHandler(BaseHTTPRequestHandler):
    close_window_flag = False  # Class-level variable to indicate whether the window should be closed

    def do_GET(self):
        query_components = parse_qs(urlparse(self.path).query)
        authorization_code = unquote(query_components.get('code', [''])[0])
        if authorization_code:
            ans = exchange_code_for_tokens(authorization_code)
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            response_content = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Muhammad Nouman</title>
    <style>
        body {
            display: flex;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }

        .message-container {
            text-align: center;
            padding: 20px;
            border: 1px solid #ccc;
            border-radius: 5px;
            background-color: #fff;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }

        .button {
            box-shadow: 0px 1px 0px 0px #fafafa;
            background: linear-gradient(to bottom, #44c767 5%, #51733f 100%);
            background-color: #44c767;
            border-radius: 10px;
            border: 4px solid #18ab29;
            display: inline-block;
            cursor: pointer;
            color: #ffffff;
            font-family: Times New Roman;
            font-size: 20px;
            font-weight: bold;
            padding: 6px 18px;
            text-decoration: none;
            text-shadow: 0px -1px 0px #2f6627;
            margin-top: 10px; /* Added margin-top to create space between the message and the button */
        }

        .button:hover {
            background: linear-gradient(to bottom, #51733f 5%, #44c767 100%);
            background-color: #51733f;
        }

        .button:active {
            position: relative;
            top: 1px;
        }
    </style>
</head>
<body>
    <div class="message-container">
    <p>Successfully Authenticated, You can Close this window</p>
    <button class="button" onclick="openAndCloseTab()">Close Tab</button>
</div>
<script>
    function openAndCloseTab() {
        window.opener = null; // To remove the reference to the parent window
        window.open('', '_self');
        window.close();
    }
</script>
</body>
</html>

"""
            self.wfile.write(response_content.encode())

            # Check the flag and return accordingly
            return ans if not self.close_window_flag else False
        else:
            self.send_response(400)  # Bad Request
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Error: Authorization code not found.')
        return False


def do_POST(self):
    self.send_response(200)
    self.send_header('Content-type', 'text/html')
    self.end_headers()
    subprocess.run('test.py')
    self.wfile.write(b'Launching the application...')


def start_local_server():
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyRequestHandler)
    if httpd:
        print('Starting local server on port 8080...')
        httpd.serve_forever()
    else:
        print('server closed')
        httpd.server_close()


def exchange_code_for_tokens(authorization_code):
    client_secret_file = 'client_secret_1001459857047-h269q1pgg1k51dhchebpu1vcr1qtc09o.apps.googleusercontent.com.json'

    # Updated scope for email and profile
    scopes = ['https://www.googleapis.com/auth/userinfo.profile']

    flow = InstalledAppFlow.from_client_config(
        json.loads(open(client_secret_file).read()),
        scopes=scopes,
        redirect_uri='http://localhost:8080'
    )
    try:
        # Fetch the token and return credentials
        flow.fetch_token(code=authorization_code)
        session = flow.authorized_session()
        file = session.get('https://www.googleapis.com/userinfo/v2/me').json()
        name = file.get('name')
        print(session.get('https://www.googleapis.com/userinfo/v2/me').json())
        print('Successful User Authentication ')
        return True
    except Exception as e:
        print(f"An error occurred during token exchange: {str(e)}")
        return False


def signInWithGoogle():
    google_signin_url = (
        "https://accounts.google.com/o/oauth2/auth?client_id=1001459857047-h269q1pgg1k51dhchebpu1vcr1qtc09o.apps"
        ".googleusercontent.com"
        "&redirect_uri=http://localhost:8080&scope=https://www.googleapis.com/auth/userinfo.profile&response_type=code"
    )
    threading.Thread(target=webbrowser.open, args=(google_signin_url,)).start()


def main():
    signInWithGoogle()
    threading.Thread(target=start_local_server())
