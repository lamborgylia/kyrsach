from django.shortcuts import render, redirect, get_object_or_404
from .models import ConsumerAccount
from django.http import HttpResponse
from .models import *


def index(request):
    return render(request, 'billing/index.html')

def consumers_list(request):
    consumers = ConsumerAccount.objects.all()
    return render(request, 'billing/consumers_list.html', {'consumers': consumers})

def add_consumer(request):
    if request.method == 'POST':
        account_number = request.POST.get('account_number')
        full_name = request.POST.get('full_name')
        address = request.POST.get('address')
        section_code = request.POST.get('section_code')

        ConsumerAccount.objects.create(
            account_number=account_number,
            full_name=full_name,
            address=address,
            section_code=section_code
        )
        return redirect('consumers_list')
    return render(request, 'billing/add_consumer.html')

def delete_consumer(request, consumer_id):
    consumer = get_object_or_404(ConsumerAccount, id=consumer_id)
    consumer.delete()
    return redirect('consumers_list')

def run_query(request):
    # Логика для выполнения запросов к базе данных
    if request.method == 'POST':
        # Пример запроса, который можно выполнить
        query = request.POST.get('query')
        result = None  # Здесь будет результат выполнения запроса
        try:
            result = YourModel.objects.raw(query)  # Например, выполнение SQL-запроса
        except Exception as e:
            result = str(e)

        return render(request, 'billing/run_query_result.html', {'result': result})
    return render(request, 'billing/run_query.html')