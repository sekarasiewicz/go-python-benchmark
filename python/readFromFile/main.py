def read_from_file():
    f = open("test.txt", "r")
    f.read()

def benchmark(func):
    import time
    start = time.time_ns()
    func()
    end = time.time_ns()
    print(end - start)

if __name__ == "__main__":
    benchmark(read_from_file)