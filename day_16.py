import json

# JSON is a syntax for storing and exchanging data. JSON is text, written with JavaScript object notation.
# Python has a built-in package called json, which can be used to work with JSON data.

# Convert JSON string in Python using the json.loads() method.

x = '{"name": "Dileep", "age": 30, "department": "Science"}'

x_file = json.loads(x)
print(x_file["name"])
print(x_file["age"])
print(x_file["department"])
