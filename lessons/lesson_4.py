#
# # for day in range(1,8):
# #     print("Day", day)
# #
# # n = 3
# # while n > 0:
# #     print(n)
# #     n -= 10
# #
#
# n = 0
# while n >= 0:
#     n += 1
#     if n == 10:
#         print("I am 10")
#         continue
#     if n == 11:
#         print("I am 11")
#         continue
#     if n == 12:
#         print("I am 12")
#         break
#
#
# print("I exit loop")

temp = [22, 24, 35, 28, 31, 29, 26]
# find all temperatures that is hotter than 30 degrees, and print it
# for i in range(0, 8):
#     if temp[i] > 30:
#         print(temp[i])


# Use while statement, loop this array
# if the temperature is hotter than 30, print it
# And break the loop when you find the 1st >=30 temprate day

i = 0
while True:
    if temp[i] > 30:
        print(temp[i])
        break
    i += 1
    if i == len(temp) - 1:
        break

