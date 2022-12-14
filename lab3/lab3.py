import datetime as dt


class Record:

    def __init__(self, amount, comment, date=None):
        self.amount = amount
        self.comment = comment
        if date is None:
            self.date = dt.date.today()
        else:
            self.date = dt.datetime.strptime(date, '%d.%m.%Y').date()


class Calculator:

    def __init__(self, limit):
        self.limit = limit
        self.records = []
        self.today = None
        self.week_ago = None

    def add_record(self, record):
        self.records.append(record)

    def get_today_stats(self):
        self.update_dates()
        day_stats = []
        for record in self.records:
            if record.date == self.today:
                day_stats.append(record.amount)
        return sum(day_stats)

    def get_week_stats(self):
        self.update_dates()
        week_stats = []
        for record in self.records:
            if self.week_ago <= record.date <= self.today:
                week_stats.append(record.amount)
        return sum(week_stats)

    def get_today_limit_balance(self):
        limit_balance = self.limit - self.get_today_stats()
        return limit_balance

    def update_dates(self):
        self.today = dt.date.today()
        self.week_ago = self.today - dt.timedelta(7)


class CaloriesCalculator(Calculator):

    def get_calories_remained(self):
        calories_remained = self.get_today_limit_balance()
        if calories_remained > 0:
            message = (f'Сегодня можно съесть что-нибудь ещё, но с общей '
                       f'калорийностью не более {calories_remained} кКал')
        else:
            message = 'Хватит есть!'
        return message


class CashCalculator(Calculator):
    USD_RATE = 61.0
    EURO_RATE = 62.0
    RUB_RATE = 1

    def get_today_cash_remained(self, currency):
        currencies = {'usd': ('USD', CashCalculator.USD_RATE),
                      'eur': ('Euro', CashCalculator.EURO_RATE),
                      'rub': ('руб', CashCalculator.RUB_RATE)}
        cash_remained = self.get_today_limit_balance()
        if cash_remained == 0:
            return 'Денег нет, держись'
        if currency not in currencies:
            return f'Валюта {currency} не поддерживается'
        name, rate = currencies[currency]
        cash_remained = round(cash_remained / rate, 2)
        if cash_remained > 0:
            message = f'На сегодня осталось {cash_remained} {name}'
        else:
            cash_remained = abs(cash_remained)
            message = (
                f'Денег нет, держись: твой долг -{cash_remained} 'f'{name}')
        return message


cash_calculator = CashCalculator(1000)
cash_calculator.add_record(Record(amount=145, comment='кофе',))
cash_calculator.add_record(
    Record(amount=300, comment='Серёге за обед', date='08.11.2019'))
cash_calculator.add_record(
    Record(amount=3000, comment='бар в Танин др', date='25.10.2022'))
print(cash_calculator.get_today_cash_remained('rub'))
limit = 2500
calories_calculator = CaloriesCalculator(limit)
calories_calculator.add_record(
 Record(amount=300, comment='обед во вкусно и точка',))
calories_calculator.add_record(Record(amount=200, comment='кофе с пончиком',))
print(calories_calculator.get_today_stats())
