def calc_tip(bill, percentage):
  return bill * (float(percentage)/float(100))

print "tipping $53.34 at 15%: " + str(calc_tip(53.34, 15))
print "tipping $87.04 at 20%: " + str(calc_tip( 87.04, 20))
