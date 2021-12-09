package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
)

func check(e error) {
	if e != nil {
		panic(e)
	}
}

func readLines(fileName string) []int {
	file, err := os.Open(fileName)
	check(err)
	defer file.Close()
	scanner := bufio.NewScanner(file)
	var lines []int
	// optionally, resize scanner's capacity for lines over 64K, see next example
	for scanner.Scan() {
		out, err := strconv.Atoi(scanner.Text())
		check(err)
		lines = append(lines, out)
	}

	check(scanner.Err())

	return lines
}

func main() {
	var lines = readLines("./input")
	fmt.Print(len(lines))

	var numIncr = 0
	for i, l := range lines {
		if i == 0 {
			continue
		}

		fmt.Print(fmt.Sprint(l) + "	")

		if lines[i-1] < l {
			fmt.Print("+1")
			numIncr++
		}

		fmt.Println("	" + fmt.Sprint(numIncr))
	}

	fmt.Println(numIncr)
}
