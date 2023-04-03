# define a dictionary with conversion factors for various measurement scales
conversion_factors = {
    'g': 1,
    'kg': 1000,
    'oz': 28.35,
    'lb': 453.59,
    # add any other measurement scales you want to support
}

# define a list to store the weights of each food item
food_weights = []

# define a function to convert the weight of each food item to grams
def convert_to_grams(weight, unit):
    conversion_factor = conversion_factors[unit]
    return weight * conversion_factor

# prompt the user to enter the weight of each food item and its measurement scale
while True:
    weight_input = input("Enter the weight and unit of measurement of a food item (e.g. 100 g): ")
    weight, unit = weight_input.split()
    weight = float(weight)
    food_weights.append(convert_to_grams(weight, unit))
    response = input("Do you want to add another food item? (y/n): ")
    if response.lower() == 'n':
        break

# prompt the user to enter the number of portions
num_portions = int(input("Enter the number of portions: "))

# prompt the user to enter the desired calorie restriction per portion (if applicable)
calorie_restriction = None
calories_per_portion = None
max_weight_per_portion = None
actual_weight_per_portion = None
total_calories = None

response = input("Do you want to set a calorie restriction per portion? (y/n): ")
if response.lower() == 'y':
    calorie_restriction = int(input("Enter the desired calorie restriction per portion: "))
    total_calories = int(input("Enter the total number of calories in all food items: "))

    # calculate the total number of calories in all food items
    total_calories = sum([int(input(f"Enter the number of calories in food item {i}: ")) for i in range(1, len(food_weights) + 1)])

    # calculate the total number of calories per portion
    calories_per_portion = total_calories / num_portions

    # calculate the maximum weight of food that can be consumed per portion
    max_weight_per_portion = (calorie_restriction / calories_per_portion) * sum(food_weights)

    # calculate the actual weight of food that can be consumed per portion, accounting for any excess weight
    actual_weight_per_portion = min(max_weight_per_portion, sum(food_weights) / num_portions)

else:
    actual_weight_per_portion = sum(food_weights) / num_portions

# output the total weight of all food items and the actual weight of food that can be consumed per portion
print("Total weight of all food items:", sum(food_weights), "g")
if calorie_restriction is not None:
    print("Actual weight of food per portion (with calorie restriction):", actual_weight_per_portion, "g")
    print("Total calories in all food items:", total_calories)
    print("Total calories per portion:", calories_per_portion)
    print("Maximum weight of food per portion:", max_weight_per_portion, "g")
else:
    print("Actual weight of food per portion:", actual_weight_per_portion, "g")
