def solve(word):
  """
  Returns the maximum value of a contiguous subsequence of non-vowels in the word.

  Args:
    word: The word.

  Returns:
    The maximum value of a contiguous subsequence of non-vowels in the word.
  """

  # Initialize the maximum value and the current value.
  max_value = 0
  current_value = 0

  # Iterate over the letters in the word.
  for letter in word:
    # If the letter is not a vowel, add its value to the current value.
    if letter not in vowels:
      current_value += ord(letter) - ord('a') + 1

    # If the current value is greater than the maximum value, update the maximum value.
    if current_value > max_value:
      max_value = current_value

    # If the letter is a vowel, reset the current value to 0.
    else:
      current_value = 0

  # Return the maximum value.
  return max_value
