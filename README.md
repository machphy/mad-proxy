
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

```
block_domains:
  - "example.com"
  - "unauthorized.site"
```

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
