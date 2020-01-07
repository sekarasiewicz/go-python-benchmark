import random
def test():
    """Some test function"""
    lst = []
    for i in range(100):
        lst.append(i)

def generateSlice(n): 
	s = []
	for _ in range(n): 
		s.append(random.randint(0, 1e9))
	
	return s

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))