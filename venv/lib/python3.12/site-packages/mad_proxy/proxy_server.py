from mitmproxy import http
from mitmproxy.tools.main import mitmdump
import os
import yaml

# Get the absolute path of config.yaml relative to this script
config_path = os.path.join(os.path.dirname(__file__), "config.yaml")

# Load policy from config.yaml once at startup
with open(config_path, "r") as f:
    policy = yaml.safe_load(f)

blocked_domains = set(policy.get("block_domains", []))


def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    for domain in blocked_domains:
        if domain in url:
            print(f"Blocked request to {url}")
            flow.response = http.HTTPResponse.make(
                403,  # Status forbidden
                b"Blocked by security policy",
                {"Content-Type": "text/plain"}
            )
            return
    print(f"Allowed request: {url}")


def main():
    mitmdump(['-p', '8080', '-s', __file__])


if __name__ == "__main__":
    main()
