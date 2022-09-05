class Solution:
    def daysBetweenDates(self, date1: str, date2: str) -> int:
        """
            #leapyear
        """
        def isLeapYear(year):
            return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

        def daysSince1971(date):
            monthDays = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
            parse = date.split("-")
            year = int(parse[0])
            month = int(parse[1])
            days = int(parse[2])
            for i in range(1971,year):
                days += 366 if isLeapYear(i) else 365
            for i in range(1,month):
                days += monthDays[i] +1 if isLeapYear(year) and i == 2 else monthDays[i]
            return days
        return abs(daysSince1971(date1) - daysSince1971(date2));
