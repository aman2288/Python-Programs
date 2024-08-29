# 8.Define a function is_palindrome()that recognizes palindromes 
# (i.e. words that look the same writtenbackwards).
# Example :- is_palindrome("radar")should return True.

def is_palindrome():
    value = input("Enter a value :")
    print(f"given value is : {value}") 
    print(f"reversed value is : {value[::-1]}")
    if value == value[::-1]:
       return  "True"

    else:
        return"False"
print(f"this value is palindrom : {is_palindrome()}")
