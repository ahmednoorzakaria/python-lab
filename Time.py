def convert_12_to_24(hour, minute, period):
  """
  Converts a 12-hour time to 24-hour time.

  Args:
    hour: The hour in the 12-hour time (1 to 12).
    minute: The minute in the 12-hour time (0 to 59).
    period: The period (either "am" or "pm").

  Returns:
    A four-digit string that encodes the time in 24-hour time.
  """

  if period == "am":
    return f"{hour:02d}{minute:02d}"
  else:
    hour += 12
    return f"{hour:02d}{minute:02d}"
