# Security Policy for mad-proxy

## Supported Versions
We provide security fixes for the latest version v0.3.

## Reporting a Vulnerability
Please report vulnerabilities via email at rajeevsharmamachphy@gmail.com  Avoid posting public issues for security concerns. We acknowledge reports within 48 hours and prioritize fixes.

## Overview
mad-proxy is a Python HTTP/HTTPS interception proxy used by security professionals for real-time malicious traffic detection and domain blocking. It uses mitmproxy for trusted HTTPS interception and a YAML-configured policy engine for granular control.

## Security Best Practices
- Install and trust mitmproxy root certificate for HTTPS interception. Use only in trusted environments.
- Validate your config.yaml to prevent misconfigurations.
- Monitor logs for suspicious or unexpected blocked/allowed domains.
- Run mad-proxy with least privileges.
- Keep mad-proxy and dependencies updated.
- Handle traffic blocking carefully to avoid network disruptions.

## Known Issues
No known security vulnerabilities in version 0.3. Report any issues promptly.

## Tools & Resources
- mitmproxy docs: [https://pypi.org/project/mad-proxy/](https://pypi.org/project/mad-proxy/)
- YAML validation tools
- Recommended Python security scanners for code contributions

## Responsible Disclosure
We abide by responsible disclosure policy. Please allow 90 days for fixes before public release.

## Contact
Email: rajeevsharmamachphy@gmail.com
