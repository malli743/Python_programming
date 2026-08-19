'''
Greatest Common Divisor of Strings

For two strings s and t, we say "t divides s" if and only if s = t + t + t + ... + t + t (i.e., t is concatenated with itself one or more times).

Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.

 

Example 1:

Input: str1 = "ABCABC", str2 = "ABC"

Output: "ABC"

Example 2:

Input: str1 = "ABABAB", str2 = "ABAB"

Output: "AB"
'''
Program 
------

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""
        def gcd(len1 ,len2):
            while len2:
                len1, len2 = len2, len1 % len2
            return len1
        return str1[:gcd(len(str1), len(str2))]


'''
Approaach:
---------
The problem requires finding the longest string X that satisfies the following conditions:
 for the given strings str1 and str2:

->X can be repeated to construct str1.
->X can be repeated to construct str2.
This means str1 and str2 must have the same structure of characters.

Valid example:
str1 = "ABC"
str2 = "ABCABC"

Invalid example:
str1 = "AB"
str2 = "ABCABC"

How do we check if the character structures are the same?
It's simple. Just create str1 + str2 and str2 + str1.

str1 + str2 = str2 + str1
valid: "ABCABCABC" = "ABCABCABC"
invalid: "ABABCABC" = "ABCABCAB"
If we have a valid case, we can create the same strings, if not, we can't find X, so

return ""
Let's continue with the valid example above.

When multiple strings are given, determining whether they share a common repeating pattern requires identifying the length of the repeating pattern for each string.

For example,

str1 = "ABCABC" → The repeating pattern is "ABC" with a length of 3.
str2 = "ABC" → The repeating pattern is "ABC" with a length of 3.

str1 = "ABABAB" → The repeating pattern is "AB" with a length of 2.
str2 = "ABAB" → The repeating pattern is "AB" with a length of 2.
In this case, the length of the common repeating pattern X must divide both len(str1) and len(str2).

Furthermore, since we need to return the largest string, we must return the string with the maximum length that divides both strings, which corresponds to the greatest common divisor (GCD) of their lengths.

"ABCABC" = 6
"ABC" = 3
GCD(6, 3) = 3(= ABC)
"ABABAB" = 6
"ABAB" = 4
GCD(6, 4) = 2(= AB)


We have to divide both lengths of the two strings with X.
We have to return the largest string X
We notice that we should use GCD.

'''