<<<<<<< HEAD

# mad-proxy

A Python-based local HTTP/HTTPS proxy with custom detection and blocking policies for malicious activity. Built using mitmproxy, `mad-proxy` empowers cybersecurity professionals and developers to intercept, inspect, and secure their web traffic with customizable rules.

---

## Features

- Intercepts all HTTP and HTTPS browser traffic via a local proxy server.
- Blocks or allows requests based on powerful and customizable policy rules (`config.yaml`).
- Fast setup and integration with browsers (Firefox, Chrome, etc.).
- Real-time logging of allowed and blocked requests in your terminal.
- Written with extensibility and cybersecurity in mind.

---

## Getting Started

### Prerequisites

- Python 3.7 or higher
- pip
- (Recommended) Use a virtual environment

### Installation

Clone the repository:

```
git clone https://github.com/machphy/mad-proxy.git
cd mad-proxy
```

Create and activate a virtual environment (optional but recommended):

```
python3 -m venv venv
source venv/bin/activate
```

Install the package and dependencies:

```
pip install .
```

Or use a pre-built wheel if available:

```
pip install dist/mad_proxy-<version>-py3-none-any.whl
```

---

### Configuration

Edit `mad_proxy/config.yaml` to set your policies. Example:

=======
Aapka project description aur README ka content jo aapne diya hai, usme mai aapko ek structured aur professional README.md banane me madad karta hoon, jise aap apne repo me update kar sakte hain. Ye packaging, installation instructions, features, setup, use cases, aur future plans cover karega.

***

### Updated README.md Example:

```markdown
# mad-proxy: Malicious Activity Detection Proxy

A local HTTP/HTTPS proxy server to detect and block malicious activity in web traffic by applying custom security policies in real-time.  
It helps users monitor browser traffic and enforce security rules such as blocking unauthorized or suspicious websites.

---

## Features

- Intercepts all HTTP and HTTPS traffic from your browser.
- Uses a local proxy server with trusted HTTPS interception (install mitmproxy certificate).
- Implements a policy engine to block or allow requests based on URL matching rules.
- Logs blocked and allowed requests with relevant details.
- Supports easy policy configuration via a YAML file.
- Example policies include blocking unauthorized sites (HTTP 403) and allowing safe sites (HTTP 200).

---

## How It Works

1. Run the local proxy server (`proxy_server.py`) using mitmproxy.  
2. Configure your browser to send traffic through the proxy (localhost:8080).  
3. The proxy intercepts all requests.  
4. The policy engine inspects URLs and applies configured rules:  
   - If URL matches blocked domains, request is blocked and HTTP 403 returned.  
   - If URL is allowed, request is passed through normally with status 200.  
5. All requests and decisions are logged in the terminal.  
6. You can customize policies in `config.yaml`.

---

## Setup & Installation

### Prerequisites

- Python 3.12+  
- mitmproxy  
- Linux environment (tested on Ubuntu/Debian)

### Step 1: Clone and install dependencies

```
git clone <your-repo-url>
cd mad-proxy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### Step 2: Configure browser proxy

- Configure Firefox or Chrome proxy settings to use `localhost:8080` for HTTP and HTTPS traffic.  
- Install the mitmproxy root certificate:  
  1. Run `python3 proxy_server.py`.  
  2. Open browser and visit [http://mitm.it](http://mitm.it).  
  3. Download and install the certificate.

### Step 3: Configure policies

Edit `config.yaml` to set blocked or allowed domains:

>>>>>>> a43119a (newupdate)
```
block_domains:
  - "example.com"
  - "unauthorized.site"
```
<<<<<<< HEAD

---

### Running the Proxy

Start the proxy server (default port 8080):

```
mad-proxy
```

**Change port if needed:**

```
mad-proxy --mode regular@8082
```

---

### Browser Setup

- Set your browser's HTTP and HTTPS proxy to `localhost:8080`.
- To inspect HTTPS, install and trust the mitmproxy certificate:
  - Visit [http://mitm.it](http://mitm.it) while the proxy is running.
  - Follow on-screen instructions for your browser.

---

## Usage & Examples

**Allowed request:**

- Visit any site not blocked by your policy; logs show  
  `Allowed request: https://www.google.com`

**Blocked request:**

- Try visiting a blocked site; logs show  
  `Blocked request to http://example.com`  
  Browser displays a "Blocked by security policy" message.

---

## Project Structure

```
mad-proxy/
├── mad_proxy/
│   ├── proxy_server.py
│   ├── config.yaml
│   └── ...
├── README.md
├── setup.py
├── requirements.txt
└── MANIFEST.in
```

---

## Contributing

Contributions, issues, and feature requests are welcome!  
Please open an issue or fork and submit a pull request.

---

## License

This project is licensed under the MIT License.

---

## Author

Maintained by [machphy](https://github.com/machphy).

---

```
=======

### Step 4: Run the proxy server

```
python3 proxy_server.py
```

---

## Testing & Use Cases

- **Allowed request (HTTP 200):**  
  Browsing allowed sites like https://www.google.com will pass through; logs show:  
  `Allowed request: https://www.google.com`.

- **Blocked request (HTTP 403):**  
  Browsing blocked sites like http://example.com shows log:  
  `Blocked request to http://example.com` and browser displays a "Blocked by security policy" message.

- **Unauthorized HTTP 401 (Future enhancement):**  
  Plans to detect and alert on HTTP 401 unauthorized responses.

---

## Project Structure

```
mad-proxy/
├── proxy_server.py        # Runs proxy and enforces policies
├── policy_engine.py       # (Planned) Advanced policy logic
├── analyzer.py            # (Planned) Traffic content analysis
├── config.yaml            # User-defined block/allow rules
├── README.md              # Project documentation
├── requirements.txt       # Python dependencies
└── utils.py               # Utility functions (logging, alerts)
```

---

## How to Extend

- Add regex or heuristic-based URL detection in `policy_engine.py`.
- Log requests and blocks into a file with timestamps.
- Implement alerting (email, desktop notifications).
- Develop a UI for easy policy management.
- Integrate threat intelligence feeds to update block lists automatically.

---

## License

MIT License
```

>>>>>>> a43119a (newupdate)
