def main(arr):
    if len(arr) == 2:
        return

    for passnum in range(len(arr)-1,0,-1):
        for i in range(passnum):
            if arr[i]>arr[i+1]:
                temp = arr[i]
                arr[i] = arr[i+1]
                arr[i+1] = temp

if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    main(arr)
    print(arr)