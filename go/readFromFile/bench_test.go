package readfromfile

import (
	"testing"
)

func BenchmarkReadFromFile(b *testing.B) {
	for n := 0; n < b.N; n++ {
		readfromfile()
	}
}
