from setuptools import setup, find_packages

setup(
    name="malicious_activity_detector",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mitmproxy",
        "pyyaml"
    ],
    entry_points={
        'console_scripts': [
            'mad-proxy = proxy_server:main',  # if you refactor proxy_server.py to have main()
        ],
    },
    author="Your Name",
    description="Local proxy server with custom policy-based malicious activity detection",
    python_requires='>=3.7',
)
