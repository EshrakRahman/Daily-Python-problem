# reads number of days will be stayed
number_of_days = abs(int(input()))
# reads food cost per day
food_cost_per_day = abs(int(input()))
# reads only one way flight cost
one_way_flight_cost = abs(int(input()))
# reads one night hotel cost only
one_night_hotel_cost = abs(int(input()))

total_food_cost = food_cost_per_day * number_of_days
flight_cost = one_way_flight_cost * 2
# number of nights equal the duration of days minus one
hotel_cost = (number_of_days - 1) * one_night_hotel_cost

total_vacation_cost = total_food_cost + flight_cost + hotel_cost
print(total_vacation_cost)
