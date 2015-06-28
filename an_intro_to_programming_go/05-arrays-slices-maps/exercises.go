package main

import "fmt"
import "sort"
import "strings"

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

	// naive alternative to the above
	smallest := nums[0]
	for _, value := range nums {
		if value < smallest {
			smallest = value
		}
	}
	fmt.Println(smallest)

	// simple map-based frequency counter
	// probably a better way to do this exists in the stdlib
	text := "one one two three one one four five six nine eight eight four three seven ten one two four four eight six"
	words := strings.Fields(text)
	counter := make(map[string]int)
	for _, word := range words {
		if _, ok := counter[word]; ok {
			counter[word] += 1
		} else {
			counter[word] = 1
		}
	}
	for word, wordCount := range counter {
		fmt.Println(word, ":", wordCount)
	}
}
