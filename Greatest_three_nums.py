'''
Greatest of three numbers
-------------------------
Given three numbers a, b and c. Find the greatest number among them.

Examples:

Input: a = 10, b = 3, c = 2
Output: 10
Explanation: 10 is greatest among the three 
Input: a = -4, b = -3, c = -2
Output: -2
Explanation: -2 is greatest among the three
Constraints:
-109≤ a, b, c ≤109

Programme
---------
'''
a = int(input())
b = int(input())
c = int(input())

# code here
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)