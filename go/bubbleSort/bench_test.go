package bubbleSort

import (
	"math/rand"
	"sort"
	"testing"
)

func generateSlice(n int) []int {
	s := make([]int, 0, n)
	for i := 0; i < n; i++ {
		s = append(s, rand.Intn(1e9))
	}
	return s
}

func BenchmarkBubbleSort1000(b *testing.B) {
	for n := 0; n < b.N; n++ {
		s := generateSlice(1000)
		b.StopTimer()
		bubbleSort(s)
		b.StartTimer()
	}
}

func BenchmarkBubbleSort10000(b *testing.B) {
	for n := 0; n < b.N; n++ {
		s := generateSlice(10000)
		b.StopTimer()
		bubbleSort(s)	
		b.StartTimer()
	}
}

func BenchmarkBuildInSort100000(b *testing.B) {
	for n := 0; n < b.N; n++ {
		b.StopTimer()
		s := generateSlice(100000)
		b.StartTimer()
		sort.Ints(s)
	}
}
