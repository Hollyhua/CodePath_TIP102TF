# Problem 10: Exposing Superman
''' Metropolis has a population n, with each citizen assigned an integer id from 1 to n. There's a rumor that Superman is an ordinary citizen among this group.

If Superman is an ordinary citizen, then:

Superman trusts nobody.
Everybody (except for Superman) trusts Superman.
There is exactly one citizen that satisfies properties 1 and 2.
Write a function expose_superman() that accepts a 2D array trust where trust[i] = [ai, bi] representing that the person labeled ai trusts the person labeled bi. If a trust relationship does not exist in trust array, then such a trust relationship does not exist.

Return the label of Superman if he is hiding amongst the population and can be identified, or return -1 otherwise.

def expose_superman(trust, n):
    pass
Example Usage

n = 2
trust = [[1, 2]]
expose_superman(trust, n)

n = 3
trust = [[1, 3], [2, 3]]
expose_superman(trust, n)

n = 3
trust = [[1, 3], [2, 3], [3, 1]]
expose_superman(trust, n)
Example Output:

2
3
-1

================================================================
    1.	Questions:
	•	Can Superman be identified when there is no trust at all, i.e., an empty trust array?
	•	Is it possible to have more than one citizen satisfying the conditions, or is there guaranteed to be one or none?
	2.	Explanation:
The goal is to identify a single citizen (Superman) who trusts no one, but is trusted by everyone else. We track the trust relationships to find the citizen who has zero outbound trust but is trusted by all other citizens.
	3.	Pseudocode:
	•	Create two arrays to track:
	•	How many people each citizen trusts.
	•	How many people trust each citizen.
	•	Loop through the trust relationships, updating the arrays accordingly.
	•	Find the citizen who trusts nobody but is trusted by exactly n-1 people.
	•	If such a person exists, return their ID. Otherwise, return -1.
	4.	Python Implementation:

'''

def expose_superman(trust, n):
    trust_counts = [0] * (n + 1)  # Array to track how many people trust a person
    trusted_by = [0] * (n + 1)    # Array to track how many trust a person
    
    for a, b in trust:
        trust_counts[a] += 1   # Person a trusts someone
        trusted_by[b] += 1     # Person b is trusted by someone
    
    for i in range(1, n + 1):
        if trust_counts[i] == 0 and trusted_by[i] == n - 1:
            return i
    return -1

# Example usage:
trust1 = [[1, 2]]
n1 = 2
print(expose_superman(trust1, n1))  # Output: 2

trust2 = [[1, 3], [2, 3]]
n2 = 3
print(expose_superman(trust2, n2))  # Output: 3

trust3 = [[1, 3], [2, 3], [3, 1]]
n3 = 3
print(expose_superman(trust3, n3))  # Output: -1