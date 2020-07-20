from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.

def post_list(request):
    #now = datetime.datetime.now()

    data1 = datetime.datetime.now()
    data2 = datetime.datetime(2000, 10, 8)

    diff = data1 - data2

    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600

    html = f"<html><body><p>Илья Дорошенко</p> <p><strong>Пи-До-Рас</strong> уже " \
           f"{days} дней, {seconds // 3600} часов, {(seconds % 3600) // 60} минут, {(seconds % 60)} секунд.</p>" \
           f"</body></html>"
    return HttpResponse(html)
    #return render(request, 'blog/post_list.html', {})