import string

paragraph = str(input())
words = list(paragraph.split(' '))
count = 0

for i in range(len(words)):
    if words[i].strip(string.punctuation) == 'the':
        count = count + 1
print(count)