import datetime
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta

while True:
	try:
		# get date of birth from user
		bdYear = input("What year were you born?")
		bdMonth = input("What month?")
		bdDay = input("what day?")
		# format
		birthdayStr = bdYear + "-" + bdMonth + "-" + bdDay
		# parse
		dob = parse(birthdayStr)
	except ValueError:
		# noinspection PyUnboundLocalVariable
		print(birthdayStr + "is not a valid date, try again.")
	else:
		break

# calculate age and next birthday year TODO: handle leap days (and other edge cases ?)
age = relativedelta(datetime.datetime.now(), dob).years
today = datetime.date.today()
thisYearBirthday = datetime.date(today.year, dob.month, dob.day)

# if person has already had their birthday this year,
if today.year - dob.year < age:
	nextBirthdayYear = datetime.datetime.now().year
else:
	nextBirthdayYear = datetime.datetime.now().year + 1

# print
print("OK, then you will turn {} on {} {} in {}!".format(age + 1, dob.strftime("%B"), dob.day, nextBirthdayYear))

exit(0)
