# 1. Define a function max()that takes two numbers as arguments and returns the largest of them.
# Use the if then­ else construct available in Python. (It is true that Python has the max()function built it
# but writing it yourself is nevertheless a good exercise.)
def max(a,b):
    if(a>b):
        print("a is largest!")
        # return  a;
    else:
        # return  b;
        print(f"{b} is largest!")

a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
max(a,b)
# print(max(a,b))

