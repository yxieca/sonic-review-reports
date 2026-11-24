#!/usr/bin/env python3
"""Bind only this pilot's report backlink after GitHub assigns its PR URL."""
import argparse
from pathlib import Path
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--url', required=True)
args = parser.parse_args()
u = urlparse(args.url)
parts = u.path.strip('/').split('/')
if (u.scheme != 'https' or u.netloc != 'github.com' or u.query or u.fragment
        or len(parts) != 4 or parts[:3] != ['yxieca', 'sonic-review-reports', 'pull']
        or not parts[3].isdigit() or int(parts[3]) < 1):
    parser.error('Expected the assigned yxieca/sonic-review-reports pull-request URL')
root = Path(__file__).resolve().parents[1]
paths = [root / 'reports/sonic-mgmt/28850.md', root / 'action-drafts/sonic-mgmt-28850.md']
for path in paths:
    text = path.read_text()
    if 'REPORT_PR_URL' not in text:
        raise SystemExit('Expected unbound pilot placeholder: ' + str(path.relative_to(root)))
for path in paths:
    path.write_text(path.read_text().replace('REPORT_PR_URL', args.url))
print('Bound pilot report and drafts to', args.url)
