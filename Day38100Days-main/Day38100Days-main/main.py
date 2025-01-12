def rainbowize(sentence):
  """Transform the sentence into a rainbow-ized string."""
  colors = {
      'r': "\033[31m",  # Red
      'g': "\033[32m",  # Green
      'b': "\033[34m",  # Blue
      'y': "\033[33m",  # Yellow
      'p': "\033[35m"   # Purple
  }
  reset = "\033[0m"
  output = ""
  current_color = reset

  for char in sentence:
      if char.lower() in colors:
          current_color = colors[char.lower()]
      elif char == ' ':
          current_color = reset

      output += f"{current_color}{char}"

  output += reset  # Ensure color is reset at the end
  return output

if __name__ == "__main__":
  print("\033[0mWelcome to the Rainbow-izer!\033[0m")
  user_input = input("Enter a sentence: ")
  print(rainbowize(user_input))
