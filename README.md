Yeh merge conflict aapke README.md file mein hai jisme do versions ke beech clash hai. Main aapke liye cleaned aur professionally formatted README.md file banake deta hoon, jo dono versions ke best parts lekar hoga.

***

### Cleaned & formatted README.md:

```markdown
# mad-proxy: Malicious Activity Detection Proxy

A Python-based local HTTP/HTTPS proxy server designed to detect and block malicious activity in web traffic by applying custom security policies in real-time.  
Built using mitmproxy, `mad-proxy` empowers cybersecurity professionals and developers to intercept, inspect, and secure web traffic with customizable rules. 

---

## Features

- Intercepts all HTTP and HTTPS browser traffic via a local proxy server.
- Blocks or allows requests based on powerful and customizable policy rules via `config.yaml`.
- Fast setup and integration with browsers (Firefox, Chrome, etc.).
- Real-time logging of allowed and blocked requests in your terminal.
- Written with extensibility and cybersecurity in mind.

---

## How It Works

1. Run the local proxy server (`proxy_server.py`) using mitmproxy.
2. Configure your browser to send traffic through the proxy (localhost:8080).
3. The proxy intercepts all requests.
4. The policy engine inspects URLs and applies configured rules:
   - If a URL matches blocked domains, the request is blocked and HTTP 403 is returned.
   - If the URL is allowed, the request passes through with status 200.
5. All requests and policy decisions are logged in the terminal.
6. Customize policies in `config.yaml`.

---

## Setup & Installation

### Prerequisites

- Python 3.7 or higher (Python 3.12+ recommended)
- mitmproxy
- Linux environment (tested on Ubuntu/Debian)
- pip
- (Recommended) Use a virtual environment

### Step 1: Clone and install dependencies

```
git clone https://github.com/machphy/mad-proxy.git
cd mad-proxy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or install the package directly:

```
pip install .
```

Or use a pre-built wheel (replace <version> accordingly):

```
pip install dist/mad_proxy-<version>-py3-none-any.whl
```

### Step 2: Configure browser proxy

- Configure Firefox or Chrome proxy settings to use `localhost:8080` for HTTP and HTTPS.
- Install the mitmproxy root certificate:
  - Run `python3 proxy_server.py`.
  - Open browser to [http://mitm.it](http://mitm.it).
  - Download and install the certificate.

### Step 3: Configure policies

Edit `config.yaml` to set your blocking or allowing rules:

```
block_domains:
  - "example.com"
  - "unauthorized.site"
```

### Step 4: Run the proxy server

```
python3 proxy_server.py
```

---

## Usage & Examples

- **Allowed request:**  
  Visiting allowed sites like `https://www.google.com` will pass through the proxy. Terminal logs will show:  
  `Allowed request: https://www.google.com`.

- **Blocked request:**  
  Visiting blocked sites like `http://example.com` will be blocked with HTTP 403. Terminal logs:  
  `Blocked request to http://example.com`.  
  The browser will display a "Blocked by security policy" message.

- **Unauthorized (HTTP 401) handling:**  
  Planned feature for detecting unauthorized requests and raising alerts.

---

## Project Structure

```
mad-proxy/
├── mad_proxy/
│   ├── proxy_server.py        # Runs proxy and enforces policies
│   ├── policy_engine.py       # (Planned) Advanced policy logic
│   ├── analyzer.py            # (Planned) Traffic content analysis
│   ├── config.yaml            # User-defined block/allow rules
│   └── utils.py               # Utility functions (logging, alerts)
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup script
└── MANIFEST.in                # Packaging manifest
```

---

## How to Extend

- Add regex or heuristic-based URL detection in `policy_engine.py`.
- Log requests and blocks into a file with timestamps.
- Implement alerts (email, desktop notifications).
- Develop a UI for easy policy management.
- Integrate threat intelligence feeds to update block lists automatically.

---

## License

This project is licensed under the MIT License.

---

## Author

Maintained by [machphy](https://github.com/machphy).

```

***

Kya main ye isi tarah README.md file me daal doon? Ya aap koi aur modification chahenge?Yeh cleaned, merged aur professional README.md file hai jo dono sections ke behtareen hisson ko mila kar banaya gaya hai. Yeh aapke GitHub repository me use karne ke liye tayar hai.Yeh aapke README.md ke liye cleaned-up aur well-structured final content hai:

```markdown
# mad-proxy: Malicious Activity Detection Proxy

A Python-based local HTTP/HTTPS proxy server designed to detect and block malicious activity in web traffic by applying custom security policies in real-time.  
Built using mitmproxy, `mad-proxy` empowers cybersecurity professionals and developers to intercept, inspect, and secure web traffic with customizable rules. 

---

## Features

- Intercepts all HTTP and HTTPS browser traffic via a local proxy server.
- Blocks or allows requests based on powerful and customizable policy rules via `config.yaml`.
- Fast setup and integration with browsers (Firefox, Chrome, etc.).
- Real-time logging of allowed and blocked requests in your terminal.
- Written with extensibility and cybersecurity in mind.

---

## How It Works

1. Run the local proxy server (`proxy_server.py`) using mitmproxy.
2. Configure your browser to send traffic through the proxy (localhost:8080).
3. The proxy intercepts all requests.
4. The policy engine inspects URLs and applies configured rules:
   - If a URL matches blocked domains, the request is blocked and HTTP 403 is returned.
   - If the URL is allowed, the request passes through with status 200.
5. All requests and policy decisions are logged in the terminal.
6. Customize policies in `config.yaml`.

---

## Setup & Installation

### Prerequisites

- Python 3.7 or higher (Python 3.12+ recommended)
- mitmproxy
- Linux environment (tested on Ubuntu/Debian)
- pip
- (Recommended) Use a virtual environment

### Step 1: Clone and install dependencies

```
git clone https://github.com/machphy/mad-proxy.git
cd mad-proxy
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Or install the package directly:

```
pip install .
```

Or use a pre-built wheel (replace <version> accordingly):

```
pip install dist/mad_proxy-<version>-py3-none-any.whl
```

### Step 2: Configure browser proxy

- Configure Firefox or Chrome proxy settings to use `localhost:8080` for HTTP and HTTPS.
- Install the mitmproxy root certificate:
  - Run `python3 proxy_server.py`.
  - Open browser to [http://mitm.it](http://mitm.it).
  - Download and install the certificate.

### Step 3: Configure policies

Edit `config.yaml` to set your blocking or allowing rules:

```
block_domains:
  - "example.com"
  - "unauthorized.site"
```

### Step 4: Run the proxy server

```
python3 proxy_server.py
```

---

## Usage & Examples

- **Allowed request:**  
  Visiting allowed sites like `https://www.google.com` will pass through the proxy. Terminal logs will show:  
  `Allowed request: https://www.google.com`.

- **Blocked request:**  
  Visiting blocked sites like `http://example.com` will be blocked with HTTP 403. Terminal logs:  
  `Blocked request to http://example.com`.  
  The browser will display a "Blocked by security policy" message.

- **Unauthorized (HTTP 401) handling:**  
  Planned feature for detecting unauthorized requests and raising alerts.

---

## Project Structure

```
mad-proxy/
├── mad_proxy/
│   ├── proxy_server.py        # Runs proxy and enforces policies
│   ├── policy_engine.py       # (Planned) Advanced policy logic
│   ├── analyzer.py            # (Planned) Traffic content analysis
│   ├── config.yaml            # User-defined block/allow rules
│   └── utils.py               # Utility functions (logging, alerts)
├── README.md                  # Project documentation
├── requirements.txt           # Python dependencies
├── setup.py                   # Package setup script
└── MANIFEST.in                # Packaging manifest
```

---

## How to Extend

- Add regex or heuristic-based URL detection in `policy_engine.py`.
- Log requests and blocks into a file with timestamps.
- Implement alerts (email, desktop notifications).
- Develop a UI for easy policy management.
- Integrate threat intelligence feeds to update block lists automatically.

---

## License

This project is licensed under the MIT License.

---

## Author

Maintained by [machphy](https://github.com/machphy).
```

Aap bataen ise README.md file me update karna hai?