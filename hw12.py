'''
Created on 11/2/19
@author:   Nicholas Cali
Pledge:    I pledge my honor that I have abided by the Stevens Honor System.

CS115 - Hw 11 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''

        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
        '''Returns a new object with the same month, day,
            year as the calling object (self).
        '''
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
         '''Decides if self and d2 represent the same calendar date,
            whether or not they are the in the same place in memory.'''
         return self.year == d2.year and self.month == d2.month and self.day == d2.day


    def tomorrow(self): #fix the one test case
        '''returns the one calender day after the date it originally represented'''
        d = Date(self.month, self.day, self.year)
        if self.month == 12 and self.day == 31:
            self.month = 1
            self.day = 1
            self.year += 1
        elif self.month == 2 and self.day == 28 and d.isLeapYear() == True:
            self.day += 1
        elif self.day >= DAYS_IN_MONTH[self.month]:
            self.day = 1
            self.month += 1
        else:
            self.day += 1
          
            

    def yesterday(self):
        '''returns the previous day'''
        if self.day == 1:
            if self.month == 1:
                self.year -= 1
                self.month = 12
                self.day = 31
            else:
                self.day = DAYS_IN_MONTH[self.month -1]
                self.month -= 1
        else:
            self.day -= 1
            

    def addNDays(self, N):
        '''changes the object that it represents N calender days after the
            days represented
        '''
        a = 0
        for x in range(N):
            print(self)
            self.tomorrow()
        print(self)


    def subNDays(self, N):
        '''returns days before the date called'''
        a = 0
        for x in range(N):
            print(self)
            self.yesterday()
        print(self)


    def isBefore(self, d2):
        '''returns true or false if called object is before d2'''
        if self.year < d2.year:
            return True
        if self.month < d2.month and self.year == d2.year:
            return True
        if self.day < d2.day and self.year == d2.year and self.month == d2.month:
            return True
        else:
            return False

    def isAfter(self, d2):
        ''' returns false or true if the called object is after d2'''
        if self.equals(d2) == False and self.isBefore(d2) == False:
            return True
        return False

    def diff(self, d2):
        '''returns the number of days between self and d2'''
        s = 1
        c = -1
        a = Date(self.month, self.day, self.year)
        while a.isBefore(d2):
            c += 1
            s = -1
            a.tomorrow()
        while a.isAfter(d2):
            c += 1
            a.yesterday()
        return s * c


    def dow(self):
        '''returns a string of all the days of the week along with there dates'''
        DAYS_IN_WEEK = ["Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        u = Date(11, 19, 2017)
        if u.isAfter(self):
            if abs(u.diff(self)) % 7 == 0:
                return 'Sunday'
            elif abs(u.diff(self)) % 7 == 6:
                     return 'Monday'
            elif abs(u.diff(self)) % 7 == 5:
                     return 'Tuesday'
            elif abs(u.diff(self)) % 7 == 4:
                     return 'Wednesday'
            elif abs(u.diff(self)) % 7 == 3:
                     return 'Thursday'
            elif abs(u.diff(self)) % 7 == 2:
                     return 'Friday'
            return 'Saturday'
        if u.isBefore(self):
            if abs(u.diff(self)) % 7 == 0:
                return 'Sunday'
            elif abs(u.diff(self)) % 7 == 6:
                     return 'Saturday'
            elif abs(u.diff(self)) % 7 == 5:
                     return 'Friday'
            elif abs(u.diff(self)) % 7 == 4:
                     return 'Thursday'
            elif abs(u.diff(self)) % 7 == 3:
                     return 'Wednesday'
            elif abs(u.diff(self)) % 7 == 2:
                     return 'Tuesday'
            return 'Monday'
            
            

            



 
