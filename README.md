# Python Code Challenges

This repository contains Python programs that address three code challenges. Each challenge has a corresponding Python function. Below, you'll find descriptions of the challenges, explanations of the functions, and example usage.

## Challenge 1: Converting 12-hour Time to 24-hour Time

### Description:
This program converts a 12-hour time format (e.g., "8:30 am" or "8:30 pm") to a 24-hour time format (e.g., "0830" or "2030").

### Function: `convert_to_24_hour(hour, minute, period)`
- Input: 
  - `hour` (integer): An hour value in the range of 1 to 12.
  - `minute` (integer): A minute value in the range of 0 to 59.
  - `period` (string): Either "am" or "pm".
- Output: A four-digit string representing the time in 24-hour format (e.g., "0830").

### Example Usage:
print(convert_to_24_hour(8, 30, "am"))  # Output: "0830" (8:30 AM in 24-hour format)
print(convert_to_24_hour(2, 45, "pm"))  # Output: "1445" (2:45 PM in 24-hour format)""


## Challenge 2: Identifying Two Positive Numbers

### Description:
This program checks if exactly two out of three integers are positive numbers (greater than zero).

### Function: `two_positive(a, b, c)`

- Input: Three integers, a, b, and c.
- Output: True if exactly two of them are positive, otherwise False.
### Example Usage:
`` print(two_positive(2, 4, -3))  # Output: True``
`` print(two_positive(-4, 6, 8))  # Output: True``

## Challenge 3: Consonant Value
### Description:
This program calculates the highest value of consonant substrings in a lowercase string. Consonants are any letters of the alphabet except "aeiou". Each letter is assigned a value from 1 to 26 (a = 1, b = 2, ..., z = 26).

### Function: `solve(word)`
- Input: A lowercase string containing only alphabetic characters.
- Output: The highest value of consonant substrings.
### Example Usage:

``print(solve("zodiacs"))  # Output: 26``
``print(solve("strength"))  # Output: 57``
Feel free to use and modify these Python programs to solve the respective challenges. If you have any questions or need further assistance, please don't hesitate to ask.


