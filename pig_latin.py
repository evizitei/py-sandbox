word = raw_input("Give me a word...")
first_letter = word[0]
translation = ""

removed = False
for letter in word:
  if removed:
    translation += letter
  else:
    removed = True

translation += first_letter
translation += "ay"
print translation
