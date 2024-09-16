# Problem 6: Merge Intervals
'''
Write a function merge_intervals() that accepts an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge_intervals(intervals):
	pass
Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merge_intervals(intervals)

intervals = [[1, 4], [4, 5]]
merge_intervals(intervals)
Example Output:

[[1, 6], [8, 10], [15, 18]]
[[1, 5]]

================================================================

	1.	Questions:
	•	Are the intervals guaranteed to be sorted by their start values?
	•	What happens if an interval is fully contained within another interval?
	2.	Explanation:
I need to merge overlapping intervals. If two intervals overlap, they should be combined into one larger interval. Intervals that do not overlap remain as they are.
	3.	Pseudocode:
	•	Sort the intervals by their start values.
	•	Initialize an empty list for merged intervals.
	•	Iterate over the sorted intervals, merging them if they overlap.
	•	Return the merged list of intervals.
	4.	Python Implementation:

'''

def merge_intervals(intervals):
    if not intervals:
        return []
    
    intervals.sort(key=lambda x: x[0])  # Sort by start of the interval
    merged = [intervals[0]]  # Initialize with the first interval
    
    for i in range(1, len(intervals)):
        last = merged[-1]
        if intervals[i][0] <= last[1]:  # Overlap, merge intervals
            last[1] = max(last[1], intervals[i][1])
        else:
            merged.append(intervals[i])  # No overlap, add new interval
    
    return merged

# Example usage:
intervals1 = [[1, 3], [2, 6], [8, 10], [15, 18]]
intervals2 = [[1, 4], [4, 5]]
print(merge_intervals(intervals1))  # Output: [[1, 6], [8, 10], [15, 18]]
print(merge_intervals(intervals2))  # Output: [[1, 5]]