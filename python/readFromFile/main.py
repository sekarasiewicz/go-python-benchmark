def read_from_file():
    f = open("test.txt", "r")
    f.read()

def benchmark(func):
    import time
    start = time.time_ns()
    func()
    end = time.time_ns()
    result = (end - start)
    return result

if __name__ == "__main__":
    times = []
    for _ in range(10):
        times.append(benchmark(read_from_file))
    print(sum(times) / len(times))