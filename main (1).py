def leapYear(year) :
	if(year % 4==0 and year % 100!=0 or year % 400 ==0) :
		return True
	else:
		return False
int(input("Enter the number:"))
if leapyear(year) :
	print("{} is a leapyear:",format(year))
print("{} is not a leapyear:",format("year"))