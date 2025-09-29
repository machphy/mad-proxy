from setuptools import setup, find_packages

setup(
    name='mad_proxy',
    version='0.2',  # bump the version for new release
    description='A local HTTP/HTTPS proxy with custom detection and blocking policies.',
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
