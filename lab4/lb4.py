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
    cash_calculator.add_record(Record(amount=500, comment='Заправка машины'))
    return cash_calculator.get_today_cash_remained('rub')


def test_cashCalc(cash_calc):
    assert cash_calc == 'На сегодня осталось 350.0 руб'


def test_CalCalc(cal_calc):
    
    assert cal_calc == (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более 2050 кКал')