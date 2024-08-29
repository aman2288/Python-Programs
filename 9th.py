# 9.Write a function is_member()that takes a value (i.e. a number, string, etc) x and a list of values a and returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the in operator does, but for the sake of the exercise you should pretend Python did not have this operator.)

def is_member():
    a = [1, 23, 43, 54, 56, 78]
    x = int(input("Enter the value: "))
    idx = 0
    while idx < len(a):
        if a[idx] == x:
            return True
        idx += 1
    return False
print(is_member())


