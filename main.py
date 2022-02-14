import random
#Part A
weeks = 16
classes = 5
classes_per_week = 3
tuition = 6000
cost_per_week = ((tuition / classes) / weeks)
cost_per_class = ((cost_per_week) / (classes_per_week)) 
print("Cost per week:", cost_per_week)
print("Cost per class:", cost_per_class)
print(weeks, type(weeks))
print(classes, type(classes))
print(classes_per_week, type(classes_per_week))
print(tuition, type(tuition))
print(cost_per_class, type(cost_per_class))
print(cost_per_week, type(cost_per_week))

new_list = [17, 5.94, "chicken", 9, 0.35, "mango", "aluminum"]
randomized = random.choice(new_list)
print(randomized)

#Part B
