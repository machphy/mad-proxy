from mitmproxy import http
from mitmproxy.tools.main import mitmdump
import yaml

# Load policy from config.yaml once at startup
with open("config.yaml", "r") as f:
    policy = yaml.safe_load(f)

blocked_domains = set(policy.get("block_domains", []))

def request(flow: http.HTTPFlow) -> None:
    url = flow.request.pretty_url
    for domain in blocked_domains:
        if domain in url:
            print(f"Blocked request to {url}")
            flow.response = http.HTTPResponse.make(
                403,  # Status code 403 Forbidden
                b"Blocked by security policy",
                {"Content-Type": "text/plain"}
            )
            return
    print(f"Allowed request: {url}")

if __name__ == "__main__":
    mitmdump(['-p', '8080', '-s', __file__])
