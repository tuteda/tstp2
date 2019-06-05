import re

text = "The ghost that says boo haunts the loo"
found = re.findall(" .oo", text)

print(found)
