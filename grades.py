def sum(grades):
  total = 0
  for grade in grades:
    total += grade
  return total

def average(grades):
  return sum(grades)/float(len(grades))

def varience(grades):
  avg = average(grades)
  varience = 0
  for grade in grades:
    varience += (avg - grade) ** 2
  return varience / float(len(grades))

def standard_deviation(grades):
  return varience(grades) ** 0.5

grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]

print "SUM: " + str(sum(grades))
print "AVG: " + str(average(grades))
print "VAR: " + str(varience(grades))
print "STD_DEV: " + str(standard_deviation(grades))
