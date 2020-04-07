# Create Dictionary Basic form
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux)
# If duplicated the key?
# lux = {'health': 490, 'health': 800, 'mana': 334, 'melee': 550, 'armor': 18.72}
# print(lux['health']) If duplicated the key, use the last value.

# Dictionary Keys able to use almost datatype except, list and dictionary.
x = {100: 'hundred', False: 0, 3.5: [3.5, 3.5]}
print(x)

# x = {[10, 20]: 100}
# print(x)

# Traceback (most recent call last):
#   File "dictionary_dojang.py", line 11, in <module>
#     x = {[10, 20]: 100}
# TypeError: unhashable type: 'list'

# x = {{'a': 10}: 100}
# print(x)

# Traceback (most recent call last):
#   File "dictionary_dojang.py", line 18, in <module>
#     x = {{'a': 10}: 100}
# TypeError: unhashable type: 'dict'

# Create blank Dictionary
x = {}
print(x)
y = dict()
print(y)

# Create Dictionary with 'dict'
# Dictionary = dic(key1=value1, key2=value2, ...)
lux1 = dict(health=490, mana=334, melee=550, armor=18.72)
print(lux1)
# Dictionary = dict(zip([key1,key2,...],[value1,value2,...])) : with function zip()
lux2 = dict(zip(['health','mana','melee','armor'],[490,334,550,18.72]))
print(lux2)
# Dictionary = dict([(key1,value1),(key2,value2),....]) : Create Dictionary with tuples (key,value) format
lux3 = dict([('health',490),('mana',334),('melee',550),('armor',18.72)])
print(lux3)
# Dictionary = dict({key1:value1, key2:value2, ....}) : Create with {} in dict
lux4 = dict({'health':490,'mana':334,'melee':550,'armor':18.72})
print(lux4)

# How to contact key of dictionary
# Dictionary[key]
lux = {'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}
print(lux['health'])
print(lux['armor'])

# If do not assign a key to the dictionary, It means all of Dictionary
print(lux)

# Assign values on keys of Dictionary
lux['health'] = 2037
lux['mana'] = 1184
print(lux)

# If assigning values to the keys that does not exist, add that keys and assigns values
lux['mana_regen'] = 3.28
print(lux)

# If try to get the value from the nonexistent key?
# print(lux['attack_speed']) # attack_speed is nonexistent key

# Traceback (most recent call last):
#   File "dictionary_dojang.py", line 63, in <module>
#     print(lux['attack_speed']) # attack_speed is nonexistent key
# KeyError: 'attack_speed'

# Check Dictionary for Key
# Key 'in' Dictionary
print('health' in lux)
print('attack_speed' in lux)

# Verify that no specific key exists
# Key 'not in' Dictionary
print('health' not in lux)
print('attack_speed' not in lux)

# Obtain the number of keys in Dictionary
# len(Dictionary)
print(len(lux))
print(len({'health': 490, 'mana': 334, 'melee': 550, 'armor': 18.72}))