import re

t = "__one__ __two__ __three__"
found = re.findall("__.*?__", t)
for find in found:
    print(find)
    
