# method of add elements on list
# append : add one element
a = [10, 20, 30]
a.append(500)
print(a)
print(len(a))

b = []
b.append(10)
print(b)

c = [10,20,30]
c.append([500, 600])
print(c)
print(len(c))

# extend : extend after added list
d = [10, 20, 30]
d.extend([500,600])
print(d)
print(len(d))

# insert : add elemets in specific index
e = [10, 20, 30]
e.insert(2, 500)
print(e)
print(len(e))
# use pattern
# insert(0, element) : add element to the beginning of the list
f = [10, 20, 30]
f.insert(0, 500)
print(f)
# insert(len(list), element) : add element to the finishing of the list
g = [10, 20, 30]
g.insert(len(g), 500)
print(g)
# insert can make nested list
h = [10, 20, 30]
h.insert(1, [500, 600])
print(h)
print(len(h))
# insert can add elements in middle
i = [10, 20, 30]
i[1:1] = [500, 600]
print(i)

# remove elements on list
# pop : remove finishing of the list or element of specific index
j = [10, 20, 30]
j.pop()
print(j)

k = [10, 20, 30]
k.pop(1)
print(k)

l = [10, 20, 30]
del l[1]
print(l)
# remove : remove specific element
m = [10, 20, 30]
m.remove(20)
print(m)

n = [10, 20, 30, 20]
n.remove(20)
print(n)

# get index of specific value on list
# if there are multiple identical values, find the first index
o = [10, 20, 30, 15, 20, 40]
print(o.index(20))

# count number of specific values
p = [10, 20, 30, 15, 20, 40]
print(p.count(20))

# reverse order of list
q = [10, 20, 30, 15, 20, 40]
q.reverse()
print(q)

# sorting of elements on list
# sort() or sort(reverse=False) : Ascending (from minimum to maximum)
# sort(reverse=True) : Descending (from maximum to minimum)
r = [10, 20, 30, 15, 20, 40]
r.sort()
print(r)

# sort method and function sorted
s = [10, 20, 30, 15, 20, 40]
s.sort()    # sort by changing the contents of s
print(s)
t = [10, 20, 30, 15, 20, 40]
print(sorted(t))    # create the new sorted list 

# clear all elements on list
u = [10, 20, 30]
u.clear()
print(u)
v = [10, 20, 30]
del v[:]
print(v)

# Manipulating lists with slice
w = [10, 20, 30]
w[len(w):] = [500]
print(w)

# assign on the other variable
x = [0, 0, 0, 0, 0]
y = x       # same perfently
print(y)
print(x is y)
y[2] = 99
print(x)

# To make list a and b completely two, you need to copy all the elements with the copy method.
ab = [0, 0, 0, 0, 0]
bc = ab.copy()
print(ab is bc)
print(ab == bc)
bc[2] = 99
print(ab)
print(bc)

# print out all elements with for loop
# for variable in list:
#   code
cd = [38, 21, 53, 62, 19]
for i in cd:
    print(i)

# print out index and elements with for loop
# for index, elements in enumerate(list):
de = [38, 21, 53, 62, 19]
for index, value in enumerate(de):
    print(index, value)

for index, value in enumerate(de, start=1):
    print(index, value)

# print out elements with index on for loop
for i in range(len(de)):
    print(de[i])

# print out elements with while loop
ef = [38, 21, 53, 62, 19]
i = 0
while i < len(ef):
    print(ef[i])
    i += 1

# get minimum and maximum
fg = [38, 21, 53, 62, 19]
smallest = fg[0]
for i in fg:
    if i < smallest:
        smallest = i
print(smallest)

largest = a[0]
for i in fg:
    if i > largest:
        largest = i
print(largest)

fg.sort()
print(fg[0])

fg.sort(reverse=True)
print(fg[0])

print(min(fg))  # use function min()
print(max(fg))  # use function max()

# sum elements
gh = [10, 10, 10, 10, 10]
x = 0
for i in gh:
    x += i
print(x)

print(sum(gh))  # use function sum()