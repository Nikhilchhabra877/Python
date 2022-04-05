#### Using Recursion ####
def rev(s):
    if len(s) == 0:
        return s
    else:
        return rev(s[1:])  + s[0]

d = "21223"
s = rev(d)

if d==s:
    print("Palindrome")
else:
    print("Palindrome")

## Method 2 without recursion

x="121"
def pell(x):
    if int(x) < 10:
        return int(x)
    elif str(x[::-1])==x:
        return "Number is palindrome"
    else:
        return "Number is not palindrome"
## Using String concaatination

def reverse(string):
    str = ""
    for i in string:
        str = i + str
    return str