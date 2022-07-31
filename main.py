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

def insertion(items,left=0,right=None):
	if right is None:
		right = len(items) - 1

	for i in range(left + 1, right + 1):
		key_item = items[i]
		j = i - 1
		while j >= left and items[j] > key_item:
			items[j + 1] = items[j]
			j -= 1
		items[j + 1] = key_item
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

def tim(items):
	min_run = 32
	n = len(items)

	for i in range(0,n,min_run):
		insertion(array, i, min((i + min_run - 1), n - 1))

	size = min_run
	while size < n:
		for start in range(0,n,size*2):
			midpoint = start + size - 1
			end = min((start + size * 2 - 1), (n-1))
			merged_array = mrg(
				left=items[start:midpoint + 1],
				right=items[midpoint + 1:end + 1]
			)
			array[start:start + len(merged_array)] = merged_array
		size *= 2
	return items
			

array = [random.randint(1,10) for i in range(100)]

if __name__ == "__main__":
	print("race between sorting algs:")
	howlong(alg="bubble", array=array)
	time.sleep(1)
	howlong(alg="insertion", array=array)
	time.sleep(1)
	howlong(alg="selection", array=array)
	time.sleep(1)
	howlong(alg="merge", array=array)
	time.sleep(1)
	howlong(alg="quick", array=array)
	time.sleep(1)
	howlong(alg="tim", array=array)
	time.sleep(1)