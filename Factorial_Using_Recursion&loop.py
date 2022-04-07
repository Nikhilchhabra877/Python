##### Developed by Nikhil#######

##### Using for loop ####
def fact_(num):
    global fact
    if num < 0:
        return "Enter the non-negative integer"
    elif num == 0 or num == 1:
        return 1
    else:
        fact = 1
        for i in range(1, num + 1):
            fact = fact * i
        return fact


#####Using Recursion ####
def fact_(num):
    if num == 1:
        return num
    elif num < 0:
        return "Enter the positive integer"
    elif num == 0:
        return 1
    else:
        return num * fact_(num - 1)
