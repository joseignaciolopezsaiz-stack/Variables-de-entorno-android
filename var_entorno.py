import os
import json
print(os.name)
#print(os.environ.get("TERMINFO"))
#print(os.environ["TERMINFO"])
diccionario = {}
for item in os.environ:
    #print(item)
    #print(os.environ[item])
    diccionario[item]= os.environ.get(item)
print(diccionario)
with open("data2.json", "w") as f:
    f.write(json.dumps(diccionario, indent=4))


