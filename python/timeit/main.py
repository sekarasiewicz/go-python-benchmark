def test():
    """Some test function"""
    lst = []
    for i in range(100):
        lst.append(i)

if __name__ == '__main__':
    import timeit
    print(timeit.timeit("test()", setup="from __main__ import test"))