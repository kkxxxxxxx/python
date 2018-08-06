# 变量赋值
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

# cars 数量
print("There are", cars, "cars available.")
# drivers 数量
print("There are only",drivers, "drivers available.")
# cars 空车数量
print("There will be", cars_not_driven, "empty cars today.")
# people 可搭载数量 
print("We can transport", carpool_capacity, "people today.")
# passengers 数量 
print("We have", passengers, "to carpool today.")
# 平均搭载数量
print("We need to put about", average_passengers_per_car, "in each car.")
