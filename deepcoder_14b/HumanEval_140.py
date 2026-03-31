import re

text = input("Enter the text: ")
result = re.sub(r' +', lambda x: '-' if len(x.group()) > 1 else '_', text)
print(result)