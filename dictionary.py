# x = dict()
# y = {}

x = {
    "name": "Jenny",
    "age": 20,
}

print(x)
print(x["name"])
print(x["age"])

y = {
    0: "Rose",
    1: "Hi",
    "age": 20,
}

print(y[0])

print("name" in x)

print(x.keys())
print(x.values())

for key in x:
    print("key: " + str(key))
    print("value: "+ str(x[key]))

x["school"] = "Hanbit"

print(x)