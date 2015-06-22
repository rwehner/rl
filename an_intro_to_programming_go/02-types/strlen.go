package main

import "fmt"

func main() {
	mystr := "this is a longish string, but exactly how long?"
	mylen := len(mystr)
	fmt.Println(mystr)
	fmt.Println("it is", mylen, "characters long.")
}
