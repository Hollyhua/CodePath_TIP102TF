# Problem 12: Thistle Hunt
'''
Pooh, Piglet, and Roo are looking for thistles to gift their friend Eeyore. Write a function locate_thistles() that takes in a list of strings items and returns a list of the indices of any elements with value "thistle". The indices in the resulting list should be ordered from least to greatest.

def locate_thistles(items):
	pass
Example Usage

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)

============================================================================

    1.	Questions:
	•	Are all elements in the list always strings?
	•	Should we consider case sensitivity for the word “thistle”?
	2.	Explanation:
I need to find all the positions in the list where the value is exactly “thistle” and return the list of those indices.
	3.	Pseudocode:
	•	Create an empty list to store the indices.
	•	Loop through the items, checking if each item equals “thistle”.
	•	If an item matches, append its index to the list.
	•	Return the list of indices.
	4.	Python Implementation:
'''

def locate_thistles(items):
    indices = []
    for i, item in enumerate(items):
        if item == "thistle":
            indices.append(i)
    return indices

# Example usage:
items1 = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
items2 = ["book", "bouncy ball", "leaf", "red balloon"]
print(locate_thistles(items1))  # Output: [0, 3]
print(locate_thistles(items2))  # Output: []
	