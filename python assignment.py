# Assignment given and its solution below
# 1.  Write a Python program to print the following string in a specific format below:
#
# Twinkle, twinkle, little star,
# 	How I wonder what you are!
# 		Up above the world so high,
# 		Like a diamond in the sky.
# Twinkle, twinkle, little star,
# 	How I wonder what you are


# 2.  Write a Python program that calculates the area of a circle based on the radius entered by the user

# 3. Use string concatenation and the len() function to find the length of a certain  movie #star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

# todo: calculate how long this name is – Enter your code here


# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
# print(name_length)
driving_license_character_limit = 28

# 4. # use at least 5 string functions to modify the string below.

text = 'this is just a sentence'
# Example - print(text.upper())


# 5. The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

# decrease the rainfall variable by 10% to account for runoff


# add the rainfall variable to the reservoir_volume variable


# increase reservoir_volume by 5% to account for stormwater that flows
# into the reservoir in the days following the storm


# decrease reservoir_volume by 5% to account for evaporation


# subtract 2.5e5 cubic metres from reservoir_volume to account for water
# that's piped to arid regions.


# print the new value of the reservoir_volume variable (1 mark)


# 6. Fix the error
days = 30
print(days + 'days in some months')


# 7. write code To check if the phrase "wife" is in a string. Tip: Use the 'in' keyword

shortText = "We are looking for a wife."


# 1.
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")
print("\t\tUp above the world so high,")
print("\t\tLike a diamond in the sky.")
print("Twinkle, twinkle, little star,")
print("\tHow I wonder what you are")

# 2.
import math

radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2

print(f"The area of the circle with radius {radius} is {area:.2f}.")


# 3.
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

full_name = given_name + " " + middle_names + " " + family_name

name_length = len(full_name)

driving_license_character_limit = 28
if name_length <= driving_license_character_limit:
    print("The name fits within the driving license character limit.")
else:
    print("The name is too long for a driving license.")

# 4.
text="this is just a sentence"
print(text.lower())
print(text.replace("just", "this"))
print(text.capitalize())
print(text.title())
print(text.split())

# 5.
# The current volume of a water reservoir (in cubic metres)
reservoir_volume = 4.445e8
# The amount of rainfall from a storm (in cubic metres)
rainfall = 5e6

rainfall *= 0.9

reservoir_volume += rainfall

reservoir_volume *= 1.05

reservoir_volume *= 0.95

reservoir_volume -= 2.5e5

print(reservoir_volume)


# 6.
days = 30
print(str(days) + ' days in some months')

# 7.
shortText = "We are looking for a wife."
if "wife" in shortText:
    print("The phrase 'wife' is in the string.")
else:
    print("The phrase 'wife' is not in the string.")


