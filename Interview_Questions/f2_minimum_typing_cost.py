"""
You are given a string s. You need to build this string from left to right using the minimum number of operations. You are allowed to perform the following two actions:
Type a single character
Cost = 1
Copy-paste a substring
You may copy any substring that already exists in the part of the string you have built so far.
Pasting the substring (of any length) costs 1
Your goal is to construct the entire string s with the minimum total cost.

✅ Example 1:
Input:
abcabc
Explanation:
Type 'a', 'b', 'c' → cost = 3
Substring "abc" already exists → copy-paste → cost = 1
Output: 4

✅ Example 2:
Input:
mississippi
Explanation (one possible sequence):
m → type → 1
i → type → 1
s → type → 1
s → copy → 1
iss → copy → 1
i → copy → 1
p → type → 1
p → copy → 1
i → copy → 1
Output: 9
"""

def minTypingCost(s)->int:
    i = 0
    built = ""
    n = len(s)
    count = 0
    while i<n:
        longest_sub_legth = 0
        for length in range(1,n-i+1):
            if s[i:i+length] in built:
                longest_sub_legth = length
            else:
                break
        
        if longest_sub_legth>0:
            count += 1
            built += s[i:i+longest_sub_legth]
            i += longest_sub_legth
        else:
            count+=1
            built += s[i]
            i += 1
    return count

print(minTypingCost("abcabc"))  
print(minTypingCost("mississippi")) 
print(minTypingCost("aaaa"))  
print(minTypingCost("aaaaaabaaa")) 
print(minTypingCost("aaaaaabbaaa")) 
print(minTypingCost("bbbb"))  