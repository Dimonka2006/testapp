import sys
print(sys.version)

import pip
file_descriptor = r'C://Py311//requirements.txt'
with open(file_descriptor, 'r') as file:
    content = file.read()
    print(content)
