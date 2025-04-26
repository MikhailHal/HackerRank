"""
For this question, you will write a program that, given a positive integer M and a list of integers L,
outputs the list element M links away from the end of the list. 
For this program, we will use 1-indexing.
That means mth_to_last(1) is the "1st-to-last" element, or simply the last element in the list.

(len(L) - M)番目の値を表示すればいい
"""

M = int(input("Enter the M : "))
L = [-1] + list(map(int, input("Enter the L : ").split()))
targetIndex = len(L) - M

if M > len(L)-1:
    print("NIL")
    exit()
print(L[targetIndex])

"""
-1, 5, 2, 1, 8, nil

M = 2
L = 6
targetIndex = 3
"""