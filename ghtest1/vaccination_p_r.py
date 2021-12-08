from decorators import *
from valid import *


class VaccinationPointRequest:
    def __init__(self, ID = 0, point = 'forum', time = '18:00', date = '2021-04-11', name = 'zzzzz'):
        self.set_ID(ID)
        self.set_point(point)
        self.time = validate_time(time)
        self.set_date(date)
        self.set_name(name)

    def __str__(self):
        return f"{self.ID}, {self.point}, {self.time}, {self.date}, {self.name}" 

    @validation_int
    @validation_posit
    def set_ID(self, ID):
        self.ID = ID

    @validation_point
    def set_point(self,point):
        self.point = point

    #@validation_time
    def set_time(self, time):
        self.time = validate_time(time)

    @validation_date
    def set_date(self, date):
        self.date = date

    @validation_name
    def set_name(self, name):
        self.name = name