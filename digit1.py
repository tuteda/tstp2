import re

line = "123 hi 34 hello.567 unchi"
m = re.findall("\d", line, re.IGNORECASE)
print(m)
