import urllib.request
import urllib.error
import os
import re
from datetime import datetime
from http.server import HTTPServer, BaseHTTPRequestHandler

def getTxtPage(pageNr, strip):
    urlData = f"https://teletekst-data.nos.nl/page/{pageNr}"
    print(f"Fetching page: {urlData}")
    
    try:
        with urllib.request.urlopen(urlData, timeout=10) as response:
            if response.status == 200:
                raw_data = response.read()
                
                # Decode using latin-1 to preserve binary control codes as characters
                txt_content = raw_data.decode('iso-8859-1')

                # Modify header text to resemble teletext on a TV; inject dutch date
                days = ["maa", "din", "woe", "don", "vri", "zat", "zon"]
                months = ["jan", "feb", "mrt", "apr", "mei", "jun", "jul", "aug", "sep", "okt", "nov", "dec"]
                now = datetime.now()
                dutch_date = f"{days[now.weekday()]} {now.day:02} {months[now.month - 1]}"
                
                time_match = re.search(r'(\d{2}:\d{2}:\d{2})', txt_content)
                header_time = time_match.group(1) if time_match else now.strftime('%H:%M:%S')
                
                clean_nr = pageNr.split('-')[0]
                header_text = f"\x02NOS-TT  {clean_nr}\x03{dutch_date}  {header_time}"
                new_pre_line = f"<pre>{header_text.rjust(40)}"

                lower_content = txt_content.lower()
                start_index = lower_content.find("<pre>")

                if start_index != -1:
                    # Look for the first newline (\n) OR carriage return (\r) after <pre>
                    # We use regex to find the position of the first line break
                    match = re.search(r'[\r\n]', txt_content[start_index:])
                    
                    if match:
                        end_of_line_index = start_index + match.start()
                        
                        before = txt_content[:start_index]
                        after = txt_content[end_of_line_index:] # Includes the \r or \n
                        
                        modified_content = before + new_pre_line + after
                    else:
                        modified_content = txt_content.replace(txt_content[start_index:start_index+45], new_pre_line, 1)
                else:
                    modified_content = txt_content

                final_bytes = modified_content.encode('iso-8859-1')
                with open(pageNr, 'wb') as f:
                    f.write(final_bytes)
                
                print(f"Update finished. Bytes written: {len(final_bytes)}")

    except urllib.error.HTTPError as e:
        # Handles 404 (Not Found), 500 (Server Error), etc.
        print(f"HTTP Error: Could not retrieve page {pageNr}. Status code: {e.code}")
    except urllib.error.URLError as e:
        # Handles connection issues (DNS, No Internet)
        print(f"Connection Error: Failed to reach the server. Reason: {e.reason}")
    except Exception as e:
        # Catch-all for unexpected issues (like disk full or permissions)
        print(f"An unexpected error occurred: {e}")

class Serv(BaseHTTPRequestHandler):
    
    def do_GET(self):
        # Handle the root/homepage
        if self.path == '/' or self.path == '/index.html':
            self.handle_static_file('test.html')
        
        # Handle Teletext page requests
        else:
            page_name = self.path[1:] # Remove leading slash
            print(f"Requesting Teletext page: {page_name}")
            
            getTxtPage(page_name, True)
            
            # Now try to serve the file (either the one we just got, or an old cache)
            if os.path.exists(page_name):
                try:
                    with open(page_name, mode='rb') as file:
                        content = file.read()
                    
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain; charset=ISO-8859-1")
                    self.end_headers()
                    self.wfile.write(content)
                except Exception as e:
                    self.send_error_msg(500, f"Internal error reading file: {e}")
            else:
                self.send_error_msg(404, f"Teletext page {page_name} not found.")

    def handle_static_file(self, filename):
        # Helper to serve local HTML files safely
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
            self.send_response(200)
            #self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(bytes(content, 'utf-8'))
        except FileNotFoundError:
            self.send_error_msg(404, "Static file not found.")

    def send_error_msg(self, code, message):
        # Helper to send a clean error back to the browser
        self.send_response(code)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(bytes(message, 'utf-8'))
   
httpd = HTTPServer(('',8080),Serv)
ip, port = httpd.socket.getsockname()
print(f"Teletext PetsciiProxy server, serving on port {port}")
httpd.serve_forever()
