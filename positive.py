def two_positive(a, b, c):
  """
  Returns True if there are exactly two positive numbers among a, b, and c.

  Args:
    a: The first number.
    b: The second number.
    c: The third number.

  Returns:
    True if there are exactly two positive numbers among a, b, and c, False otherwise.
  """

  # Count the number of positive numbers.
  count_positive = 0
  if a > 0:
    count_positive += 1
  if b > 0:
    count_positive += 1
  if c > 0:
    count_positive += 1

  # Return True if the count is equal to 2.
  return count_positive == 2
