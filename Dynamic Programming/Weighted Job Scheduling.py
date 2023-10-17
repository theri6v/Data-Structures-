# Python3 program for weighted job scheduling
# using Dynamic Programming

# Importing the following module to sort array
# based on our custom comparison function
from functools import cmp_to_key

# A job has start time, finish time and profit


class Job:

	def __init__(self, start, finish, profit):

		self.start = start
		self.finish = finish
		self.profit = profit

# A utility function that is used for sorting
# events according to finish time


def jobComparator(s1, s2):

	return s1.finish < s2.finish

# Find the latest job (in sorted array) that
# doesn't conflict with the job[i]. If there
# is no compatible job, then it returns -1


def latestNonConflict(arr, i):

	for j in range(i - 1, -1, -1):
		if arr[j].finish <= arr[i - 1].start:
			return j

	return -1

# The main function that returns the maximum possible
# profit from given array of jobs


def findMaxProfit(arr, n):

	# Sort jobs according to finish time
	arr = sorted(arr, key=cmp_to_key(jobComparator))

	# Create an array to store solutions of subproblems.
	# table[i] stores the profit for jobs till arr[i]
	# (including arr[i])
	table = [None] * n
	table[0] = arr[0].profit

	# Fill entries in M[] using recursive property
	for i in range(1, n):

		# Find profit including the current job
		inclProf = arr[i].profit
		l = latestNonConflict(arr, i)

		if l != -1:
			inclProf += table[l]

		# Store maximum of including and excluding
		table[i] = max(inclProf, table[i - 1])

	# Store result and free dynamic memory
	# allocated for table[]
	result = table[n - 1]

	return result


# Driver code
values = [(3, 10, 20), (1, 2, 50),
		(6, 19, 100), (2, 100, 200)]
arr = []
for i in values:
	arr.append(Job(i[0], i[1], i[2]))

n = len(arr)

print("The optimal profit is", findMaxProfit(arr, n))


