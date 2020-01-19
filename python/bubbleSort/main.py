import random

def main(arr):
    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

def generate_slice(n): 
	s = []
	for _ in range(n): 
		s.append(random.randint(0, 1e9))
	
	return s

def benchmark(func):
    import time
    arr = generateSlice(1000)
    start = time.time_ns()
    func(arr)
    end = time.time_ns()
    print(end - start)

if __name__ == "__main__":
    benchmark(main)
    