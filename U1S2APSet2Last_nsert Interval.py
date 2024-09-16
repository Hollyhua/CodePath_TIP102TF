# Problem 6: Insert Interval
''' 
Implement a function insert_interval() that accepts an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. The function also accepts an interval new_interval = [start, end] that represents the start and end of another interval.

Insert new_interval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

You don't need to modify intervals in-place. You can make a new array and return it.

def insert_interval(intervals, new_interval):
    pass
Example Usage

intervals = [[1, 3], [6, 9]]
new_interval = [2, 5]
insert_interval(intervals, new_interval)

intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval = [4, 8]
insert_interval(intervals, new_interval)
Example Output:

[[1, 5], [6, 9]]
[[1, 2], [3, 10], [12, 16]]
================================================================

    1.	Questions:
	•	Are the intervals always sorted in ascending order by their start values?
	•	What should be done if the new interval overlaps with multiple existing intervals?
	2.	Explanation:
I need to insert a new interval into a list of already sorted, non-overlapping intervals. If the new interval overlaps with any existing intervals, I must merge them.
	3.	Pseudocode:
	•	Initialize an empty list for the result.
	•	Loop through the intervals:
	•	If the current interval ends before the new interval starts, add it to the result.
	•	If the current interval starts after the new interval ends, add the new interval and the rest of the intervals.
	•	If the current interval overlaps with the new interval, merge them.
	•	Add the merged interval if it hasn’t been added already.
	•	Return the result list.
	4.	Python Implementation:

'''

def insert_interval(intervals, new_interval):
    result = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that end before the new interval starts
    while i < n and intervals[i][1] < new_interval[0]:
        result.append(intervals[i])
        i += 1
    
    # Merge all overlapping intervals with the new interval
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    result.append(new_interval)  # Add the merged interval
    
    # Add the remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1
    
    return result

# Example usage:
intervals1 = [[1, 3], [6, 9]]
new_interval1 = [2, 5]
intervals2 = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
new_interval2 = [4, 8]
print(insert_interval(intervals1, new_interval1))  # Output: [[1, 5], [6, 9]]
print(insert_interval(intervals2, new_interval2))  # Output: [[1, 2], [3, 10], [12, 16]]