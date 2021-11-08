package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"os"
)

func main() {
	args := os.Args[1:]
	if len(args) < 1 {
		log.Fatal("No file specified")
	}
	filename := args[0]
	content, err := ioutil.ReadFile(filename)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("file: %s\n", content)
}
