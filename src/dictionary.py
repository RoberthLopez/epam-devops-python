class Dictionary:
  def __init__(self):
    self.dictionary = {}

  def newentry(self, word, description):
    if (type(word) != str or type(description) != str):
      print("First and second param should be a string")
      return
    self.dictionary[word] = description
  
  def look(self, word):
    if word in self.dictionary:
      return self.dictionary[word]
    else:
      return f"Can't find entry for {word}"