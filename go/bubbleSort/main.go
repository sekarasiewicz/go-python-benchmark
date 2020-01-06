package bubbleSort

func bubbleSort(sorting []int) {
	size := len(sorting)
	if size < 2 {
		return
	}
	for i := 0; i < size; i++ {
		for j := size - 1; j >= i+1; j-- {
			if sorting[j] < sorting[j-1] {
				sorting[j], sorting[j-1] = sorting[j-1], sorting[j]
			}
		}
	}
}
