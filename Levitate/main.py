spell = "Wingardium Leviosa"
user_input = input()
if user_input in spell:
    print(spell.find(user_input))
else:
    print('-1')
