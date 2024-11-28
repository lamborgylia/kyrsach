# Generated by Django 5.1.3 on 2024-11-24 16:23

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Benefit',
            fields=[
                ('type', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('discount_percentage', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Controller',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('full_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('code', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                ('accountant_name', models.CharField(max_length=100)),
                ('phone_number', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Tariff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConsumerAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_number', models.CharField(max_length=20, unique=True)),
                ('full_name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('has_benefit', models.BooleanField()),
                ('benefit_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='billing.benefit')),
                ('section_code', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.section')),
            ],
        ),
        migrations.CreateModel(
            name='Debt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('month_year', models.DateField()),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('consumer_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.consumeraccount')),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('number', models.AutoField(primary_key=True, serialize=False)),
                ('issue_date', models.DateField()),
                ('month_year', models.DateField()),
                ('previous_reading', models.DecimalField(decimal_places=2, max_digits=10)),
                ('current_reading', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interval', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accrued_amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_due', models.DecimalField(decimal_places=2, max_digits=10)),
                ('payment_date', models.DateField(blank=True, null=True)),
                ('payment_amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('consumer_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.consumeraccount')),
            ],
        ),
        migrations.CreateModel(
            name='MeterReading',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('meter_reading', models.DecimalField(decimal_places=2, max_digits=10)),
                ('reading_date', models.DateField()),
                ('month_year', models.DateField()),
                ('is_in_invoice', models.BooleanField()),
                ('consumer_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.consumeraccount')),
                ('controller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='billing.controller')),
            ],
        ),
    ]
