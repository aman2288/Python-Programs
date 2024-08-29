# 10. Define a function generate_n_chars() that takes an integer nand a character c and returns a string, ncharacters long, consisting only of c:s. 
# Example :- generate_n_chars(5,"x")should return the string "xxxxx".

def generate_n_chars(n, c):
    result = ""
    for _ in range(n):
        result += c
    return result
print(generate_n_chars(4,"x"))

# def generate_n(n,c):
#     return n*c
# print(generate_n(5,"R"))
