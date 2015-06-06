my_num = 2**1000

mystring = str(my_num)

def sum_string(string_1):
    newsum = sum(int(i) for i in string_1)
    return newsum