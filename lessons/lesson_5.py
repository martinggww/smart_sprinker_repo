# # # # # def watering_advice(temp, raining) -> str:
# # # # #     message = None
# # # # #     if raining:
# # # # #         message = "Don't water"
# # # # #     elif temp >= 30:
# # # # #         message = "Water recommended"
# # # # #     else:
# # # # #         message = "skip"
# # # # #     return message
# # # # #
# # # # # temp = 50
# # # # # raining = False
# # # # #
# # # # # message = watering_advice(temp, raining)
# # # # # print (message)
# # # #
# # # # def subtract(a, b):
# # # #     temp = a -b
# # # #
# # # #     return temp
# # # #
# # # # a = 17
# # # # b = 10
# # # # x, y = 27, 10
# # # # result = subtract(a, b)
# # # # print(result)
# # # # result_2 = subtract(x, y)
# # # # print(result_2)
# # #
# # # def fun(a, b):
# # #     if a > b:
# # #         return a + b
# # #     elif a <= b:
# # #         return a -b
# # #     else:
# # #         return None
# #
# #
# # def fun(a, b):
# #     print (a)
# #     print (b)
# #     temp = a + b
# #     print (temp)
# #     print (a -b)
# #
# # fun(100, 88)
#
# # write a function called print_full_name
# # Three parameters: first_name, last_name, age
# # return this person's full name and age
# # For example: Shuo, Huang, 40 -> "My name is Shuo Huang, I am 40"
#
# first_name = input("What is you first name?")
# last_name = input("What is you last name?")
# age = input("What is your age?")
#
# def print_full_name(first_name, last_name, age):
#     result = f'My name is {first_name} {last_name}, I am {age}.'
#     return result
# # Use this print_full_name function, first name is Janice, last name is Huang, her age is 30
# # print the result on the terminal
# result = print_full_name("Janice", "Huang", 30)
# print(result)
from os import supports_dir_fd


# write a function, called full_address
# This function has 2 parameters: street_name, zip_code
# if the zip_code is 22101 or 22102, print the full address, which has format street_name + zip_code
# if the zip_code is not as above, return "I don't know where you are"
# Iterate(Loop) above function call 3 times.

def full_address(street_name,zip_code) -> str:
    result = ""
    if zip_code == "22101" or zip_code == "22102":
        result = f'{street_name} {zip_code}'
    else:
        result = "I don't know where you are"
    return result

for i in range(3):
    street_name = input("What is your street name?")
    zip_code = input("What is your zip code?")

    result = full_address(street_name,zip_code)
    print(result)


