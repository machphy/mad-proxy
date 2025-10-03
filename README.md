
# mad-proxy: Malicious Activity Detection Proxy

A Python-based HTTP/HTTPS proxy server for real-time detection and blocking of malicious web activity using custom security policies.  
Built with mitmproxy for cybersecurity professionals, red teamers, and developers who want transparency and control in web traffic inspection and security.

## Standard Operating Procedure.

Read [SOP](https://github.com/machphy/mad-proxy/blob/main/img/SOP_rajeev.pdf)


![IMG](https://github.com/machphy/mad-proxy/blob/main/img/image.png?raw=true)

---

## Features

- **Intercepts all HTTP and HTTPS browser traffic** via a local proxy server.
- **Customizable policy engine:** Block or allow requests using rules defined in a YAML file (`config.yaml`).
- **Quick integration** with major browsers like Firefox, Chrome, and Brave.
- **Real-time logging** of blocked and allowed requests in the terminal.
- **Supports trusted HTTPS interception** via mitmproxy root certificate installation.
- **Extensible design** for future feature additions and research.

---

## Project Architecture

Browser  
↓  
`mad-proxy` (`proxy_server.py`)  
↓  
Policy Engine (`policy_engine.py` & `config.yaml`)  
↓  
Internet

---

## Project Structure

```
mad-proxy/
├── mad_proxy/
│   ├── proxy_server.py     # Main proxy and request handler
│   ├── policy_engine.py    # Policy rules and matching logic
│   ├── config.yaml         # User-defined block/allow domains
│   ├── analyzer.py         # (Planned) Advanced traffic analysis
│   └── utils.py            # Helper functions (logging, alerts)
├── README.md               # Project documentation
├── requirements.txt        # Python dependencies
├── setup.py                # Package build and installation script
├── CHANGELOG.md            # Version and update log
└── MANIFEST.in             # Manifest file for package
```

---

## Getting Started

### Prerequisites

- Python 3.7 or higher (3.12+ recommended)
- pip
- mitmproxy
- Linux (tested on Ubuntu/Debian)

### Installation

**Clone the repository:**

```
git clone https://github.com/machphy/mad-proxy.git
cd mad-proxy
```

**Create and activate a virtual environment (recommended):**

```
python3 -m venv venv
source venv/bin/activate
```

**Install dependencies:**

```
pip install -r requirements.txt
```

---

## Configuration

Edit `mad_proxy/config.yaml` to define your block or allow list:

```
block_domains:
  - "example.com"
  - "unauthorized.site"
```

Add or modify domains as desired.

---

## Browser Setup

1. Set your browser HTTP/HTTPS proxy to `localhost:8080`.  
2. Trust the mitmproxy root certificate:  
   - Run the proxy server (next section).  
   - Visit [http://mitm.it](http://mitm.it) in the browser.  
   - Download and install the certificate following the instructions.

---

## Running the Proxy Server

Start the proxy:

```
python3 proxy_server.py
```

Default is port 8080; modify if needed.

---

## Usage Examples

**Allowed Request:**  
Visiting allowed sites (e.g., https://www.google.com) logs:  

```
Allowed request: https://www.google.com
```

**Blocked Request:**  
Blocked sites (e.g., http://example.com) log:  

```
Blocked request to http://example.com
```

Browser shows a "Blocked by security policy" HTTP 403 message.

---

## Package Build & Setup Instructions

You can build and install mad-proxy as a Python package.

### Step 1: Prerequisites

Install build and twine tools:

```
pip install --upgrade build twine
```

### Step 2: Build the package

Run in project root:

```
python3 -m build
```

This generates `.whl` and `.tar.gz` files in the `dist/` folder.

### Step 3: Local package install

Install the built wheel locally:

```
pip install dist/mad_proxy-<version>-py3-none-any.whl
```

Replace `<version>` with the actual version number.

### Step 4: (Optional) Publish package to PyPI

After configuring `.pypirc` with your PyPI token, run:

```
twine upload dist/*
```

---

## How to Extend

- Add regex or heuristic-based URL/malicious content detection in `policy_engine.py`.
- Implement advanced logging and alert mechanisms in `utils.py`.
- Build UI for easier rule management.
- Integrate with threat intelligence feeds for automated updates.

---

## Troubleshooting

- **Mitmproxy certificate errors:** Ensure the mitmproxy root certificate is installed correctly.
- **Port conflicts:** If port 8080 is busy, change the port in the proxy start command or config.
- **Configuration errors:** YAML formatting is strict—validate `config.yaml` carefully.

---

## License

MIT License

---

## Maintainer

Maintained by [machphy](https://github.com/machphy)
Email :- [Email](rajeevsharmamachphy@gmail.com)
