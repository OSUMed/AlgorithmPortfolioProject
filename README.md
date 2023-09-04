# Leetcode Patterns Project

## Author

Srikanth Medicherla

## Overview

This project addresses two distinct challenges commonly seen in Leetcode problems: the minimum life points needed for Tesla in a grid and checking if a string can be converted into a palindrome within a given limit. Both problems use dynamic programming techniques.

## Implemented Features

### 1. `getTesla(M: List[List[int]]) -> int`

- Calculates the minimum life points Tesla needs to reach the destination in a grid.
- Time Complexity: O(m*n)

### 2. `checkPalindrome_1(string: str, k: int) -> bool`

- Checks if a string can be transformed into a palindrome with `k` changes using dynamic programming.
- Time Complexity: O(m*n)

### 3. `checkPalindrome_2(string: str, k: int) -> bool`

- Similar to `checkPalindrome_1`, but uses a different algorithm.
- Time Complexity: O(2^n)

## Optional Features

- A shuffle button to randomize the cards order.
- Tolerance for slight answer differences.
- Streak counters for user's correct answers.

## How to Run

1. Download the source code.
2. Navigate to the project directory.
3. Run `python main.py` to execute the code.

