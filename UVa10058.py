import re

from sys import stdin


VERB = "(hate|love|know|like)s?"
NOUN = "(tom|jerry|goofy|mickey|jimmy|dog|cat|mouse)"
ARTICLE = "(a|the)"
ACTOR = f"({NOUN}|{ARTICLE} {NOUN})"
ACTIVE_LIST = f"{ACTOR}( and {ACTOR})*"
ACTION = f"{ACTIVE_LIST} {VERB} {ACTIVE_LIST}"
STATEMENT = f"{ACTION}( , {ACTION})*"

for line in stdin:
    if re.fullmatch(STATEMENT, line.strip()):
        print("YES I WILL")
    else:
        print("NO I WON'T")
