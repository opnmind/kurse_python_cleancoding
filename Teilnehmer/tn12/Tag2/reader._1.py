"""
Script IP finder

Erklärung

Aufrufbeispiel

Verweise
"""
import re

LOG_PATH = "/home/coder/Workspace/kurse_python_cleancoding/Materialien/Sample.log"

with open(LOG_PATH, "r") as fd:
    log_text = fd.read()
print(len(log_text))
ips = []
matches = re.findall(r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b", log_text)

for match in matches:
    print(match)
    ips.append(str(match))

print(ips)