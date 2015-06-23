package main

import "fmt"
import "sort"

func main() {
	// How do you access the 4th element of an array or slice?
	x := [5]int{1, 2, 3, 4, 5}
	fmt.Println(x[3])

	// What is the length of this slice?
	xx := make([]int, 3, 9)
	fmt.Println(len(xx))

	//   These:                 V    V    V
	xxx := [6]string{"a", "b", "c", "d", "e", "f"}
	fmt.Println(xxx[2:5])

	// Find the smallest number in this list
	nums := []int{48, 96, 86, 68, 57, 82, 63, 70, 37, 34, 83, 27, 19, 97, 9, 17}
	sort.Ints(nums)
	fmt.Println(nums[0])
}
