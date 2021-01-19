
string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0

for i in string:
    if i in ('a', 'e', 'i', 'o', 'u'):
        count = count + 1
print(count)
