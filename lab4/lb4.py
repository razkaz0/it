import pytest
import sys
sys.path.append('../lab3')
from lab3 import Record, CashCalculator, CaloriesCalculator


@pytest.fixture()
def cal_calc():
    limit = 2500
    calories_calculator = CaloriesCalculator(limit)
    calories_calculator.add_record(
        Record(amount=300, comment='Мороженное'))
    calories_calculator.add_record(
        Record(amount=150, comment='Хот-дог', ))
    return calories_calculator.get_calories_remained()


@pytest.fixture()
def cash_calc():
    cash_calculator = CashCalculator(1000)
    cash_calculator.add_record(Record(amount=150, comment='Перевод денег'))
    cash_calculator.add_record(Record(amount=500, comment='Заправка маш'))
    return cash_calculator.get_today_cash_remained()


def test_cashCalc(cash_calc):
    assert cash_calc == 'Денег осталось (Валюта: Руб)'


def test_CalCalc(cal_calc):
    
    assert cal_calc == 'Калорий осталось: 2050.'