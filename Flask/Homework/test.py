import json

json_string = """
    {
      "name": "Anna",
      "city": "Brno",
      "language": ["czech", "english", "Python"],
      "age": 26
    }
"""

data = json.loads(json_string)

with open('test.txt', mode='w', encoding='utf-8') as file_: # kontext manager
    data = json.dumps(data, ensure_ascii=False, indent=2)
    file_.write(data)

with open('test.txt') as file_:
    new = json.loads(file_.read())