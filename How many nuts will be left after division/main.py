# reads squirrels and nuts numbers
total_squirrels = int(input())
total_nuts = int(input())

total_leftover_nuts = total_nuts % total_squirrels
print(total_leftover_nuts)
