import json

trabajadores = [{'nombre': 'Jack', 'edad': '25'}, {'nombre': 'Rose', 'edad': '24'}]
with open('nombre_de_archivo.json', 'w') as archivo:
    json.dump(trabajadores, archivo)
    