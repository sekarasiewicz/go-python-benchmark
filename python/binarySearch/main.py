import random

def binary_search(item_list, item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item :
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

def generateSlice(n): 
	s = []
	for _ in range(n): 
		s.append(random.randint(0, 1e9))
	
	return s

def benchmark(func):
    import time
    arr = generateSlice(10000)
    start = time.time_ns()
    func(arr, 6)
    end = time.time_ns()
    print(end - start)

if __name__ == "__main__":
    benchmark(binary_search)
    