# 7. Define a function reverse()that computes the reversal of a string. 
# For example, reverse("I am testing")should return the string "gnitset ma I".

def calc_reverse():  # without parameter
    str_value = input("Enter a string :")
    return str_value[::-1]  #using slicing method
print(calc_reverse())


def calc_reverse(string):  # with parameter
    return string[::-1]  #using slicing method
print(calc_reverse(" i am aman"))
