single_quotes = 'I don\'t like having to escape characters'
first_letter = single_quotes[0]
lowered = single_quotes.lower()
uppered = single_quotes.upper()
lower_letter = lowered[0]
length = len(single_quotes)

#simple print
print single_quotes
print lowered
print uppered

#concatenation
print single_quotes + " " +lower_letter + " " + uppered[0]

#interpolation
print "Maybe %s should go home.  %s usually hate parties..." %(first_letter, first_letter)

#console input
day = raw_input("What day is it?")
print "Today is %s" % (day)
