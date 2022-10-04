import calendar

def isLeap(year):
  if calendar.isleap(year):
    return "Es bisiesto"
  return "No es bisiesto"


print(isLeap(2000))