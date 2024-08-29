# Define a function that computes the length of a given list or string.
#  (It is true that Python has the len()function built in,
#  but writing it yourself is nevertheless a good exercise.)

l = [12,32,345,54,45,"Aman",43,54]
def len_of_list(l):

    print(f"length of this list is {len(l)}")
#     return len(l) 
# print(len_of_list(l))
len_of_list(l)

# without len function

def calc_len(l):
    length = 0
    for i in l:
        length += 1
    return length

print(calc_len([1, 2, 3, 4, 5]))  

