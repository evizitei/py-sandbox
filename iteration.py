messages = ["Hello world!", "okay...", "that's fine"]

for message in messages:
  if message.find("!") >= 0:
    print "Stop Shouting!!"
  else:
    print message
