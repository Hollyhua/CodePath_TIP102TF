# Problem 10: Eeyore's House
'''
Eeyore has collected two piles of sticks to rebuild his house and needs to choose pairs of sticks whose lengths are the right proportion. Write a function good_pairs() that accepts two integer arrays pile1 and pile2 where each integer represents the length of a stick. The function also accepts a positive integer k. The function should return the number of good pairs.

A pair (i, j) is called good if pile1[i] is divisible by pile2[j] * k. Assume 0 <= i <= len(pile1) - 1 and 0 <= j <= len(pile2) - 1

def good_pairs(pile1, pile2, k):
	pass
Example Usage

pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
good_pairs(pile1, pile2, k)

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
good_pairs(pile1, pile2, k)
Example Output:

5
2

================================================================
    1.	Questions:
	•	Can there be duplicate stick lengths in either pile?
	•	Are both piles guaranteed to have at least one stick?
	2.	Explanation:
I need to find how many pairs (i, j) satisfy the condition that the stick in pile1 at index i is divisible by pile2[j] * k. For each pair, I check if pile1[i] is divisible by the product of pile2[j] and k.
	3.	Pseudocode:
	•	Initialize a counter for good pairs.
	•	For each stick in pile1:
	•	For each stick in pile2:
	•	Check if pile1[i] % (pile2[j] * k) == 0.
	•	If true, increment the counter.
	•	Return the total count of good pairs.
	4.	Python Implementation:

'''

def good_pairs(pile1, pile2, k):
    count = 0
    for i in range(len(pile1)):
        for j in range(len(pile2)):
            if pile1[i] % (pile2[j] * k) == 0:
                count += 1
    return count

# Example usage:
pile1 = [1, 3, 4]
pile2 = [1, 3, 4]
k = 1
print(good_pairs(pile1, pile2, k))  # Output: 5

pile1 = [1, 2, 4, 12]
pile2 = [2, 4]
k = 3
print(good_pairs(pile1, pile2, k))  # Output: 2