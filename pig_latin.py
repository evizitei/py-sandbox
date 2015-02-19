word = raw_input("Give me a word...")
if len(word) > 0 and word.isalpha():
  word = word.lower()
  first_letter = word[0]
  midway = (word + first_letter + "ay")
  translation = midway[1:len(midway)]
  print translation
else:
  print "It's no good, sir..."
