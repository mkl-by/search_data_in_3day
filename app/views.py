from django.http import HttpResponse
from django.shortcuts import render

from .models import Purchases, User
from django.db.models import Count, TimeField, Sum
from django.db.models.functions import TruncHour

import datetime


def index(request):
    """отправляем все данные имеющиеся в таблице, сделано для наглядности"""
    if User.objects.all().exists():
        date_all = Purchases.objects.all().order_by('date').values()
        return render(request, 'app/start.html', {'date_all': date_all})
    else:
        return HttpResponse('<h1>Sorry!!! No data in database (что-то пошло не так - перезапустите сервер)</h1>')


def answer(request):
    """
        Возвращает данные о количестве покупателей, покупок, и общей сумме покупок
    за каждый час последних 3 суток
    """
    # last data in base
    start_data = Purchases.objects.order_by('date').last()
    var_list = []
    for dd in range(3):  # подставляем количество дней необходимых для проверки (3)
        delta = datetime.timedelta(days=dd)
        stop_d = start_data.date - delta
        result = Purchases.objects.filter(date__day=stop_d.day).\
            annotate(hour=TruncHour('date', output_field=TimeField()),).\
            values('hour').annotate(exp=Count('user_id', distinct=True)).\
            annotate(idd=Count('id')).annotate(s=Sum('money'))
        var_list.append({'datas': stop_d.strftime('%d-%m-%Y'), 'date_al1': result})

    return render(request, 'app/end.html', {'date_all1': var_list})
