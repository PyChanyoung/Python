# 20200406 12:55
def chat(name1, name2, age):
    print("%s: Hi, How old are you" %name1)
    print("%s: Me? I'm %d" %(name2, age))

chat("Alex", "Yoon", 10)
chat("Cheol", "Yeong", 30)

def dsum(a, b):
    result = a + b
    return result

d = dsum(2, 4)
print(d)