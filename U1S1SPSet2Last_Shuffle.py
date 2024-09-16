# Problem 12: Shuffle
'''
Write a function shuffle() that accepts a list cards of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn]. Return the list in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(cards):
	pass
Example Usage

cards = ['Joker', 'Queen', 2, 3, 'Ace', 7]
shuffle(cards)

cards = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
shuffle(cards)

cards = [10, 10, 2, 2]
shuffle(cards)
Example Output:

['Joker', 3, 'Queen', 'Ace', 2, 7]
[9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
[10, 2, 10, 2]
================================================================

1.	Questions:
	•	Can the list have an odd number of elements, or will it always be even?
	•	Should the output maintain the type of elements (e.g., integers, strings)?
	2.	Explanation:
The list is divided into two halves. I want to combine the two halves by alternating elements from each half.
	3.	Pseudocode:
	•	Split the list into two halves.
	•	Create a new list.
	•	Loop through the elements of both halves, adding one element from the first half and one from the second half at each step.
	•	Return the new shuffled list.
	4.	Python Implementation:
'''

def shuffle(cards):
    n = len(cards) // 2
    first_half = cards[:n]
    second_half = cards[n:]
    shuffled = []
    
    for i in range(n):
        shuffled.append(first_half[i])
        shuffled.append(second_half[i])
    
    return shuffled

# Example usage:
cards1 = ['Joker', 'Queen', 2, 3, 'Ace', 7]
cards2 = [9, 2, 3, 'Joker', 'Joker', 3, 2, 9]
cards3 = [10, 10, 2, 2]

print(shuffle(cards1))  # Output: ['Joker', 3, 'Queen', 'Ace', 2, 7]
print(shuffle(cards2))  # Output: [9, 'Joker', 2, 3, 3, 2, 'Joker', 9]
print(shuffle(cards3))  # Output: [10, 2, 10, 2]
	