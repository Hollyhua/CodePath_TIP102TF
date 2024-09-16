# Problem 8: Defuse the Bomb
'''
Batman has a bomb to defuse, and his time is running out! His butler, Alfred, is on the phone providing him with a circular array code of length n and key k.

To decrypt the code, Batman must replace every number. All the numbers are replaced simultaneously.

If k > 0, replace the ith number with the sum of the next k numbers.
If k < 0, replace the ith number with the sum of the previous k numbers.
If k == 0, replace the ith number with 0.
As code is circular, the next element of code[n-1] is code[0], and the previous element of code[0] is code[n-1].

Given the circular array code and an integer key k, write a function decrypt() that returns the decrypted code to defuse the bomb!

def defuse(code, k):
	pass
Example Usage:

code = [5, 7, 1, 4]
k = 3
defuse(code, k)

code = [1, 2, 3, 4]
k = 0
defuse(code, k)

code = [2, 4, 9, 3]
k = -2
defuse(code, k)
Example Output:

[12, 10, 16, 13]
[0, 0, 0, 0]
[12, 5, 6, 13]

================================================================

	1.	Questions:
	•	What should we do if k is larger than the length of the array?
	•	Should we handle cases where the circular array contains negative numbers?
	2.	Explanation:
Depending on the value of k, I need to replace each number with either the sum of the next k or previous k numbers in a circular manner. If k is 0, replace every number with 0.
	3.	Pseudocode:
	•	If k == 0, return a list of zeros.
	•	If k > 0, for each element, find the sum of the next k elements.
	•	If k < 0, for each element, find the sum of the previous k elements.
	•	Handle the circular nature by using modular arithmetic.
	4.	Python Implementation:
'''

def defuse(code, k):
    n = len(code)
    
    if k == 0:
        return [0] * n
    
    result = []
    
    for i in range(n):
        if k > 0:
            # Sum of the next k elements
            total = sum(code[(i + j) % n] for j in range(1, k + 1))
        else:
            # Sum of the previous |k| elements
            total = sum(code[(i - j) % n] for j in range(1, -k + 1))
        result.append(total)
    
    return result

# Example usage:
code1 = [5, 7, 1, 4]
k1 = 3
code2 = [1, 2, 3, 4]
k2 = 0
code3 = [2, 4, 9, 3]
k3 = -2
print(defuse(code1, k1))  # Output: [12, 10, 16, 13]
print(defuse(code2, k2))  # Output: [0, 0, 0, 0]
print(defuse(code3, k3))  # Output: [12, 5, 6, 13]