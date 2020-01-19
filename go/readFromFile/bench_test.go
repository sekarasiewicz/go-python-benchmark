package readfromfile

import (
	"testing"
)

func BenchmarkReadFromFile(b *testing.B) {
	b.StopTimer()
	readfromfile()
	b.StartTimer()
}
