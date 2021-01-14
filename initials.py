name=input("What is your name")
initials=name.split(" ")
for word in initials:
  if word != "":
   print(word[0].upper())
