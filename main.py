def text(colour, word):
  if colour == "purple":
    print("\033[35m", word, sep=" ", end="")
  elif colour == "green":
    print("\033[32m", word, sep=" ", end="")
  elif colour == "lgreen":
    print("\033[1;32m", "\033[3m", word, sep=" ", end="")
  elif colour == "blue":
    print("\033[0;34m", word, sep=" ", end="")
  elif colour == "cyan":
    print("\033[0;36m", "\033[3m", word, sep=" ", end="")
  else:
    print("\033[0m", word, sep=" ", end="")

print("~ Favorite Tech Quote", end="")
text("purple", "#7")
text("none", "~")
print()
print()
text("green", "Stop bragging about how many books you read, courses you finished, and videos you watched. Go and build something instead.")
print()
text("lgreen", "- Santiago Valdarrama")
print()
print()
text("none", "'What does that mean?' You may ask")
print()
text("blue", "It means, the key to truly mastering a subject is to put into practice what you have learned")
print()
print()
print()
text("cyan", "Source: https://twitter.com/munachidozie/status/1622332310891683841")