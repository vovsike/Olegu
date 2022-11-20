import math
import json


f = open("input.json")

objects = json.load(f)

def volume(object):
    if object["shape"] == "Sphere":
        r = int(object["radi"])
        return (4/3)*math.pi*(r*r*r)
    if object["shape"] == "Parallelepiped":
        a, b, c = int(object["a"]), int(object["b"]), int(object["c"])
        return a*b*c
    if object["shape"] == "Tetrahedron":
        a = int(object["a"])
        return (a*a*a)/(6*(math.sqrt(2)))

def area(object):
    if object["shape"] == "Sphere":
        r = int(object["radi"])
        return 4*math.pi*r*r
    if object["shape"] == "Parallelepiped":
        a, b, c = int(object["a"]), int(object["b"]), int(object["c"])
        return (2*a*b)+(2*b*c)+(2*a*c)
    if object["shape"] == "Tetrahedron":
        a = int(object["a"])
        return math.sqrt(3)*a*a

for object in objects:
    object["volume"] = (volume(object))

for object in objects:
    object["area"] = (area(object))

def cocktailSort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n-1
    while (swapped==True):

        swapped = False

        for i in range (start, end):
            if (a[i]["area"] > a[i+1]["area"]) :
                a[i], a[i+1]= a[i+1], a[i]
                swapped=True

        if (swapped==False):
            break
        swapped = False

        end = end-1

        for i in range(end-1, start-1,-1):
            if (a[i]["area"] > a[i+1]["area"]):
                a[i], a[i+1] = a[i+1], a[i]
                swapped = True

        start = start+1

cocktailSort(objects)

data_out = json.dumps(objects, indent=4)

with open("output.json", "w") as outfile:
    outfile.write("There are a total of " + str(len(objects)) + " objects. They are sorted by area \n")
    outfile.write(data_out)