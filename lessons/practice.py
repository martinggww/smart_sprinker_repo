#write a function which loop from 1 to 100
#if the number is odd, print "Hello, I am {}"
#if the number is even, print "World, I am {}"
# if num % 2 == 0 ---> even
# if a number % 2 != 0 --> odd number

# def my_function():
#     for i in range(1,101):
#         if i % 2 == 0:
#             print(f'Hello, I am {i}')
#         elif i % 2 != 0:
#             print(f'World, I am {i}')
# my_function()

# Write a function that continuously accept input from the terminal
# then print like "ith input: ...."
# if the input is "stop", end the execution

# 1: hello
# 2: world
# 3: lucas
# stop
# def next_function():
#     index = 1
#     while True:
#
#         word = input("Please input a word")
#         if word == "stop":
#             break
#         else:
#             print(f'{index}: {word}')
#         index += 1
# next_function()

# function call function
def long_fellow():
    print ("This is long fellow middle school")

def cooper():
    print ("This is cooper middle school")

def mclean_high():
    print ("This is mclean high school")

def langley_high():
    print ("This is langley high school")

if __name__ == '__main__':
    # ask user to input a zip code,
    # if the zip code is 22101, call long_fellow() and mclean()
    # if the zip code is 22102, print cooper and langley_high()

    zip_code = input("What is your zip code?")
    if zip_code == "22101":
        long_fellow()
        mclean_high()
    elif zip_code == "22102":
        cooper()
        langley_high()
