#This module finds the smallest number x for which 1x,2x,3x,4x,5x,6x
#have the same digits

def perm():
    for i in range(10000000):
'''converts each int into a string to be sorted'''
        one = str(i)
        two = str(2*i)
        three = str(3*i)
        four = str(5*i)
        five = str(5*i)
        six = str(6*i)
'''sorts the strings from earlier'''
        one_sorted = sorted(one)
        three_sorted = sorted(three)
        four_sorted = sorted(four)
        five_sorted = sorted(five)
        six_sorted = sorted(six)
        two_sorted = sorted(two)
        
        if two_sorted == three_sorted == four_sorted == five_sorted == six_sorted:
            print one, two, three, four, five, six 
