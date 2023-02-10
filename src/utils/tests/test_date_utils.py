import unittest
import pandas as pd
from utils.date_utils import last_day_of_month, business_days, days_in_month

class TestLastDay(unittest.TestCase):
    def test_standard_month(self):
        result = last_day_of_month(pd.Timestamp('2021-01-01'))
        self.assertEqual(result, pd.Timestamp('2021-01-31'))
        
    def test_leap_year(self):
        result = last_day_of_month(pd.Timestamp('2020-02-01'))
        self.assertEqual(result, pd.Timestamp('2020-02-29'))
        
    def test_end_of_month(self):
        result = last_day_of_month(pd.Timestamp('2021-01-31'))
        self.assertEqual(result, pd.Timestamp('2021-01-31'))
        
    def test_end_of_month_leap_year(self):
        result = last_day_of_month(pd.Timestamp('2020-02-29'))
        self.assertEqual(result, pd.Timestamp('2020-02-29'))
        
    

class TestBusinessDays(unittest.TestCase):
    def test_both_weekdays(self):
        result = business_days(pd.Timestamp('2021-01-01'), pd.Timestamp('2021-01-05'))
        self.assertEqual(result, 4)
        
    def test_both_weekends(self):
        result = business_days(pd.Timestamp('2021-01-02'), pd.Timestamp('2021-01-03'))
        self.assertEqual(result, 0)
        
    def test_start_weekend(self):
        result = business_days(pd.Timestamp('2021-01-02'), pd.Timestamp('2021-01-06'))
        self.assertEqual(result, 3)
        
    def test_end_weekend(self):
        result = business_days(pd.Timestamp('2021-01-01'), pd.Timestamp('2021-01-03'))
        self.assertEqual(result, 2)
        


class TestDaysInMonth(unittest.TestCase):
    def test_both_in_month(self):
        result = days_in_month(1, pd.Timestamp('2021-01-08'), pd.Timestamp('2021-01-30'))
        self.assertEqual(result, 22)
        
    def test_start_in_month(self):
        result = days_in_month(1, pd.Timestamp('2021-01-08'), pd.Timestamp('2021-02-21'))
        self.assertEqual(result, 23)

    def test_end_in_month(self):
        result = days_in_month(1, pd.Timestamp('2020-12-01'), pd.Timestamp('2021-01-19'))
        self.assertEqual(result, 19)
    
    def test_neither_in_month(self):
        result = days_in_month(1, pd.Timestamp('2020-12-01'), pd.Timestamp('2021-02-28'))
        self.assertEqual(result, 31)

if __name__ == '__main__':
    unittest.main()