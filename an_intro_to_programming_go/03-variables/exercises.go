package main

import "fmt"

func main() {
	// Two ways to define variables
	var myVar string = "longish way"
	myNextVar := "short way"
	fmt.Println("This var was defined in the", myVar+".")
	fmt.Println("This var was defined in the", myNextVar+".")

	// Add to a var and re-assign
	x := 5
	x += 1
	fmt.Println("x is", x)

	// Convert to Celsius
	fmt.Print("Enter degrees in Fahrenheit: ")
	var fahrenheitInput float64
	fmt.Scanf("%f", &fahrenheitInput)
	fmt.Println(fahrenheitInput, "degrees Fahrenheit is", fahrenheitToCelsius(fahrenheitInput), "degrees Celsius.")

	// Convert feet to meters
	fmt.Print("Enter length in feet: ")
	var feetInput float64
	fmt.Scanf("%f", &feetInput)
	fmt.Println(feetInput, "feet is", feetToMeters(feetInput), "meters.")
}

func fahrenheitToCelsius(degreesF float64) float64 {
	return ((degreesF - 32) * 5 / 9)
}

func feetToMeters(feet float64) float64 {
	return (feet * 0.3048)
}
