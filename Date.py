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
        return ("%d-%02d-%02d" % (self.__year, self.__month, self.day))

    def substractDay(self, day):
        if day < self.day:
            self.day -= day
        else:
            self.__month -= 1
            lastDay = calendar.monthrange(self.__year, self.__month)[1]

            day -= self.day
            while day > lastDay:
                day -= lastDay
                self.__month -= 1

                if self.__month < 1:
                    self.__month = 12
                    self.__year -= 1

                lastDay = calendar.monthrange(self.__year, self.__month)[1]
            
            self.day = lastDay - day - 1

    def getTodayDate(self):
        year = date.today().year
        month = date.today().month
        day = date.today().day

        return ("%d-%02d-%02d" % (year, month, day))
