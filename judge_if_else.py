korean, english, mathematics, science = map(int, input().split())
average = (korean+english+mathematics+science) // 4

if 0 <= korean <= 100 and 0 <= english <= 100 and 0 <= mathematics <= 100 and 0 <= science <= 100:
    if average >= 80:
        print('Pass')
    else:
        print('Fail')
else:
    print('Wrong Score')
