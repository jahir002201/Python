import re

pattern = r'\d+'
text = "There are 42 apples"
matches = re.findall(pattern, text)
print(matches)  