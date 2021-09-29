from django.shortcuts import render
from datetime import date

from .models import * 


def index(request):
    if request.method == "POST":
        time_frame = request.POST.get('time_frame')
        print(time_frame)
        date_to = date.today()
        if time_frame == '1month':
            if date_to.month -1 < 1:
                date_from = date(date_to.year-1, 12 + date_to.month-1, date_to.day)
            else:
                    date_from = date(date_to.year, date_to.month-1, date_to.day)
        elif time_frame == '3month':
            if date_to.month -3 < 1:
                date_from = date(date_to.year-1, 12 + date_to.month-3, date_to.day)
            else:
                    date_from = date(date_to.year, date_to.month-3, date_to.day)
        elif time_frame == '6month':
            if date_to.month -6 < 1:
                date_from = date(date_to.year-1, 12 + date_to.month-6, date_to.day)
            else:
                    date_from = date(date_to.year, date_to.month-6, date_to.day)
        elif time_frame == '1year':
            date_from = date(date_to.year-1, date_to.month, date_to.day)
        elif time_frame == 'alltime':
            date_from = date(date_to.year-5, date_to.month, date_to.day)
        else:
            if date_to.month -1 < 1:
                date_from = date(date_to.year-1, 12 + date_to.month-1, date_to.day)
            else:
                date_from = date(date_to.year, date_to.month-1, date_to.day)
               
        final_time = date_from - date_to
        
        query = Order.objects.filter(time__gte=date_from, time__lte=date_to)

        print(query)
    


    return render(request, 'base.html')