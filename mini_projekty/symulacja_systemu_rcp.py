"""
Koncepcja:
1. Mamy pracownika pracownik ma
"""
import datetime
from typing import List


class IdGenerator:
    def __init__(self):
        self.last_id = 0

    def __next__(self):
        self.last_id += 1
        return self.last_id

    def __iter__(self):
        return self

    def set_last_id(self, external_last_id: int):
        self.last_id = external_last_id


global_id_generator = IdGenerator()


class WorkDay:
    def __init__(self):
        self._currant_date = None
        self._check_in_hour = None
        self._check_out_hour = None


class WorkCard:
    def __init__(self):
        self.worked_days: List[WorkDay] = []
        self.current_Day = None

    def save_to_file(self):
        """this method will overwrite existing file and write all data about worked_days"""
        pass

    def save_current_day(self):
        """After checkout save current day to list and append it to work card file."""
        pass

    def calculate_salary_to_pay(self, salary_per_hour: float) -> float:
        """There can be also passed range of dates or use some constant to calculate salary daily or weekly or monthly."""
        pass


class Employee:
    def __init__(self):
        self.id = next(global_id_generator)
        self.work_card = WorkCard()
        self.current_Day = WorkDay()
        self.salary_per_hour = 0

    def check_in(self):
        self.current_Day._currant_date = datetime.date.today()
        self.current_Day._check_in_hour = datetime.datetime.now().time()

    def check_out(self):
        self.current_Day._check_out_hour = datetime.datetime.now().time()
        self.work_card.save_current_day()


class GeneralManager(Employee, WorkDay):
    def __init__(self):
        super().__init__()
        WorkDay.__init__(self)

    def check_in(self):
        super().check_in()
        print("Manager checked in.")

