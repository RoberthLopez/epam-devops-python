def concatenate_letters(words_arr):
  result = ""
  for index, word in enumerate(words_arr):
    result+= word[index]
  print(result)
  return result