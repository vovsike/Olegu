import random
import json


n = int(input("Number of elements"))

def random_shape():
    possible_shapes=["Sphere","Parallelepiped","Tetrahedron"]
    return random.choice(possible_shapes)

to_json = []

for i in range(n):
    shape = random_shape()
    if shape =="Sphere":
        object = {
            "shape" : shape,
            "radi" : random.randint(1,20),
            "density" : random.randint(1,20),
            "volume": "",
            "area": ""
        }
    if shape =="Parallelepiped":
        object = {
            "shape" : shape,
            "a": random.randint(1,20),
            "b": random.randint(1,20),
            "c": random.randint(1,20),
            "density": random.randint(1,20),
            "volume": "",
            "area" :""
        }
    if shape =="Tetrahedron":
        object = {
            "shape" : shape,
            "a": random.randint(1,20),
            "density": random.randint(1,20),
            "volume": "",
            "area" :""
        }
    to_json.append(object)

json_file = json.dumps(to_json)


with open("input.json", "w") as outfile:
    outfile.write(json_file)