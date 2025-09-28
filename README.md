Malicious Activity Detection Proxy
This project is a local HTTP/HTTPS proxy server to detect and block malicious activity in web traffic by applying custom security policies in real-time. It helps users monitor browser traffic and enforce security rules such as blocking unauthorized or suspicious websites.

Features
Intercepts all HTTP and HTTPS traffic from your browser.

Uses a local proxy server with trusted HTTPS interception (install mitmproxy certificate).

Implements a policy engine to block or allow requests based on URL matching rules.

Logs blocked and allowed requests with relevant details.

Supports easy policy configuration via a YAML file.

Example policies include blocking unauthorized sites (HTTP 401) and allowing safe sites (HTTP 200).

How It Works
Run the local proxy server (proxy_server.py) using mitmproxy.

Configure your browser to send traffic through the proxy (localhost:8080).

The proxy intercepts all requests.

The policy engine inspects URLs and applies configured rules:

If URL matches blocked domains, request is blocked and response 403 returned.

If URL is allowed, request is passed through normally with status 200.

All requests and decisions are logged in the terminal.

You can customize policies in config.yaml.

Setup & Installation
Prerequisites
Python 3.12+

mitmproxy

Linux environment (tested on Ubuntu/Debian)

Step 1: Clone and install dependencies
bash
git clone <your-repo-url>
cd malicious_activity_detector
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
Step 2: Configure browser proxy
Configure Firefox or Chrome proxy settings to use localhost:8080 for HTTP and HTTPS.

Install the mitmproxy root certificate:

Run python3 proxy_server.py

Open browser and visit http://mitm.it

Download and install the certificate.

Step 3: Configure policies
Edit config.yaml:

text
block_domains:
  - "example.com"
  - "unauthorized.site"
Step 4: Run the proxy server
bash
python3 proxy_server.py
Testing & Use Cases
Case 1: URL returns HTTP 200 (Allowed)
Browsing allowed sites like https://www.google.com will pass through.

You will see in terminal:

text
Allowed request: https://www.google.com
Case 2: URL blocked with HTTP 403 (Policy restricted)
Browsing blocked sites like http://example.com or http://unauthorized.site

Terminal shows:

text
Blocked request to http://example.com
Browser receives “Blocked by security policy” message with HTTP status 403.

Case 3: Unauthorized HTTP 401 (future enhancement)
Policies can be extended to detect and act on HTTP 401 responses.

You can implement alerts or logging for unauthorized access attempts.

Project Structure
text
malicious_activity_detector/
├── proxy_server.py        # Runs proxy and enforces policies
├── policy_engine.py       # (Planned) Advanced policy logic
├── analyzer.py            # (Planned) Traffic content analysis
├── config.yaml            # User-defined block/allow rules
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── utils.py               # Utility functions (logging, alerts)
How to Extend
Add regex or heuristic-based URL detection in policy_engine.py.

Log requests and blocks into a file with timestamps.

Implement alerting (email, desktop notifications).

Develop a UI for easy policy management.

Integrate threat intelligence feeds to update block lists automatically.

License
MIT License# mad-proxy
