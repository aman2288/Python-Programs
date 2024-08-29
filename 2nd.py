# 2. Define a function max_of_three()that takes three numbers as arguments and returns the largest ofthem.
a = int(input("Enter the value of a :"))
b = int(input("Enter the value of b :"))
c = int(input("Enter the value of c :"))
def max_of_three(a,b,c):
    if(a>b and b>c):
         print("a is greatest!")   # return a   
    elif(b>a and b>c):
        print("b is greatest!")    # return b
    else:
        print("c is greatest!")    # return c 
max_of_three(a,b,c)
# print(max_of_three(a,b,c))