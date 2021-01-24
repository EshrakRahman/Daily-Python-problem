n = 1
gust_list = []
while n > 0:
    gust_list.append(input())
    if '.' in gust_list:
        gust_list.pop()
        break
print(gust_list)
print(len(gust_list))
