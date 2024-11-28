from django.db import models

class ConsumerAccount(models.Model):
    account_number = models.CharField(max_length=20, unique=True)  # Лицевой счет
    full_name = models.CharField(max_length=100)  # ФИО
    address = models.CharField(max_length=200)  # Адрес
    section_code = models.ForeignKey('Section', on_delete=models.CASCADE)  # Код участка
    has_benefit = models.BooleanField()  # Признак льготы
    benefit_type = models.ForeignKey('Benefit', null=True, blank=True, on_delete=models.SET_NULL)  # Тип льготы

    def __str__(self):
        return f"{self.account_number} - {self.full_name}"


class Section(models.Model):
    code = models.AutoField(primary_key=True)  # Код участка
    name = models.CharField(max_length=50)  # Наименование участка
    accountant_name = models.CharField(max_length=100)  # ФИО бухгалтера
    phone_number = models.CharField(max_length=15)  # Номер телефона

    def __str__(self):
        return self.name


class Controller(models.Model):
    code = models.AutoField(primary_key=True)  # Код контроллера
    full_name = models.CharField(max_length=100)  # ФИО контроллера

    def __str__(self):
        return self.full_name


class Benefit(models.Model):
    type = models.AutoField(primary_key=True)  # Тип льготы
    name = models.CharField(max_length=50)  # Наименование
    discount_percentage = models.DecimalField(max_digits=5, decimal_places=2)  # % скидки от тарифа

    def __str__(self):
        return self.name


class Tariff(models.Model):
    start_date = models.DateField()  # Дата начала периода
    end_date = models.DateField()  # Дата окончания периода
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма тарифа

    def __str__(self):
        return f"{self.start_date} - {self.end_date}"


class MeterReading(models.Model):
    consumer_account = models.ForeignKey('ConsumerAccount', on_delete=models.CASCADE)  # Лицевой счет
    meter_reading = models.DecimalField(max_digits=10, decimal_places=2)  # Показания счетчика
    reading_date = models.DateField()  # Дата снятия показания
    month_year = models.DateField()  # Месяц и год
    controller = models.ForeignKey('Controller', on_delete=models.CASCADE)  # Код контроллера
    is_in_invoice = models.BooleanField()  # Признак участия в квитанции

    def __str__(self):
        return f"Reading for {self.consumer_account}"


class Invoice(models.Model):
    number = models.AutoField(primary_key=True)  # № квитанции
    issue_date = models.DateField()  # Дата выписки
    consumer_account = models.ForeignKey('ConsumerAccount', on_delete=models.CASCADE)  # Лицевой счет
    month_year = models.DateField()  # Месяц и год начислений
    previous_reading = models.DecimalField(max_digits=10, decimal_places=2)  # Показание за прошлый месяц
    current_reading = models.DecimalField(max_digits=10, decimal_places=2)  # Показание на текущий месяц
    interval = models.DecimalField(max_digits=10, decimal_places=2)  # Интервал показаний
    accrued_amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма начислений
    discount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма скидки
    total_due = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма к оплате
    payment_date = models.DateField(null=True, blank=True)  # Дата оплаты
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)  # Сумма оплаты

    def __str__(self):
        return f"Invoice {self.number}"


class Debt(models.Model):
    consumer_account = models.ForeignKey('ConsumerAccount', on_delete=models.CASCADE)  # Лицевой счет
    month_year = models.DateField()  # Месяц и год
    amount = models.DecimalField(max_digits=10, decimal_places=2)  # Сумма долга

    def __str__(self):
        return f"Debt for {self.consumer_account} ({self.amount})"
