from setuptools import setup, find_packages

setup(
    name='mad_proxy',
    version="0.3",  # bump the version for new release
    description="Lightweight HTTP/HTTPS interception proxy with real-time traffic firewall and domain block.",
    author='machphy',
    author_email='rajeevsharmamachphy@gmail.com',
    url='https://github.com/machphy/mad-proxy',
    packages=find_packages(),
    install_requires=[
        'mitmproxy>=7.0.0',  # example dependency
        # add other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
    ],
)
