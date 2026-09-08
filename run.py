"""
NARADA Prototype Launcher
Starts FastAPI backend server and serves the Officer Console frontend.
"""

import sys
import os
import webbrowser
import uvicorn

# Add backend directory to sys.path so 'app' is importable
current_dir = os.path.dirname(os.path.abspath(__file__))
backend_dir = os.path.join(current_dir, "backend")
if backend_dir not in sys.path:
    sys.path.insert(0, backend_dir)

def main():
    port = 8000
    host = "127.0.0.1"
    url = f"http://{host}:{port}"
    print("=" * 60)
    print("NARADA — AI Identity Intelligence & Screening System (SIH26188)")
    print("Theme: Blockchain & Cybersecurity | Team: LARPERS")
    print("=" * 60)
    print(f"Starting server at: {url}")
    print("Opening browser console...")
    
    try:
        webbrowser.open(url)
    except Exception as e:
        print(f"Note: Could not automatically open browser: {e}")

    uvicorn.run("app.main:app", host=host, port=port, reload=False)

if __name__ == "__main__":
    main()
