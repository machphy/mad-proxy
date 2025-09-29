from setuptools import setup, find_packages

setup(
    name="mad_proxy",
   
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "mitmproxy",
        "pyyaml",
    ],
    include_package_data=True,
    entry_points={
    'console_scripts': [
        'mad-proxy = mad_proxy.proxy_server:main',
    ],
},

    author="Your Name",
    description="Local proxy server with malicious activity detection policies",
    python_requires='>=3.7',
)
