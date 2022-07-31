import random
import time
from timeit import repeat

def howlong(alg,array):
	if alg != "sorted":
		setup_code = f"from __main__ import {alg}"
	else:
		setup_code = ""

	stmt = f"{alg}({array})"

	times = repeat(setup=setup_code, stmt=stmt, repeat=3, number=10)

	print(f"alg : {alg}, minimum time : {min(times)}")

def bubble(items):
	sorted = True
	while sorted:
		sorted = False
		for i in range(len(items)-1):
			if items[i] > items[i+1]:
				items[i],items[i+1] = items[i+1],items[i]
				sorted = True
	return items

def insertion(items):
	indexing_length = range(1,len(items))
	for i in indexing_length:
		value_to_sort = items[i]
		while items[i-1] > value_to_sort and i>0:
			items[i], items[i-1] = items[i-1], items[i]
			i = i - 1
	return items

def selection(items):
	for i in range(len(items)):
		min_idx = i
		for j in range(i+1,len(items)):
			if items[min_idx] > items[j]:
				min_idx = j

		items[i],items[min_idx] = items[min_idx],items[i]
	return items

def mrg(left,right):
	if len(left) == 0:
		return right

	if len(right) == 0:
		return left

	result = []
	index_left = index_right = 0
	while len(result) < len(left) + len(right):
		if left[index_left] <= right[index_right]:
			result.append(left[index_left])
			index_left += 1
		else:
			result.append(right[index_right])
			index_right += 1

		if index_right == len(right):
			result += left[index_left:]
			break

		if index_left == len(left):
			result += right[index_right:]
			break
	return result

def merge(items):
	if len(items) < 2:
		return items

	midpoint = len(items) // 2

	return mrg(
		left=merge(items[:midpoint]),
		right=merge(items[midpoint:])
	)

def quick(items):
	if len(items) < 2:
		return items
	
	low = []
	same = []
	high = []
	
	pivot = items[random.randint(0, len(items)-1)]

	for item in items:

		if item < pivot:
			low.append(item)
		elif item == pivot:
			same.append(item)
		elif item > pivot:
			high.append(item)

	return quick(low) + same + quick(high)

array = [random.randint(1,10) for i in range(9)]

if __name__ == "__main__":
	print(array)
	howlong(alg="bubble", array=array)
	howlong(alg="insertion", array=array)
	howlong(alg="selection", array=array)
	howlong(alg="merge", array=array)
	howlong(alg="quick", array=array)