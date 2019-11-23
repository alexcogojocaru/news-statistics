from datetime import date
import calendar

class Date:
    def __init__(self, offset=None):
        self.__year = date.today().year
        self.__month = date.today().month
        self.day = date.today().day

        if offset is not None:
            self.day = date.today().day - offset

            if self.day < 1:
                self.__month -= 1
                self.day = calendar.monthrange(self.__year, self.__month)[1] - (offset - date.today().day)
            
    def toString(self):
        dayStr = str(self.day)
        monthStr = str(self.__month)

        if self.day < 10:
            dayStr = '0' + str(self.day)

        if self.__month < 10:
            monthStr = '0' + str(self.__month)

        return str(self.__year) + '-' + monthStr + '-' + dayStr

    def addDay(self, day):
        lastDay = calendar.monthrange(self.__year, self.__month)[1]

        self.day += day
        if self.day > lastDay:
            self.__month += 1
            self.day = (self.day - day) % lastDay

    def substractDay(self, day):
        self.day -= day

        if self.day < 1:
            self.__month -= 1
            lastDay = calendar.monthrange(self.__year, self.__month)[1]

            self.day = lastDay + self.day