package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"time"
)

func main() {
	// Define the endpoint of the receiver_app.py
	url := "http://127.0.0.1:5000/"

	// Create a struct to hold the time data
	data := struct {
		Time string `json:"time"`
	}{
		Time: time.Now().Format("2006-01-02 15:04:05"),
	}

	// Convert struct to JSON
	jsonData, err := json.Marshal(data)
	if err != nil {
		fmt.Println("Error marshalling data:", err)
		return
	}

	// Send POST request with JSON data
	resp, err := http.Post(url, "application/json", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Println("Error sending POST request:", err)
		return
	}
	defer resp.Body.Close()
	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println("Response body:", string(body))

	// Print response from server
	fmt.Println("Response status:", resp.Status)
}
