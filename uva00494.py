import re
import sys

for line in sys.stdin:
    print(len(re.findall(r"[a-zA-Z]+", line)))
