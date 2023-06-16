price = 123
bonus = 23
bonus_granted = True

if bonus_granted:
    price -= bonus

print(price)

print(price if bonus_granted else price - bonus)

rating = 5

if rating == 5:
    print('very good')
elif rating == 4:
    print('good')
else:
    print('weak')

print('very good' if rating == 5 else 'good' if rating == 4 else 'weak')

