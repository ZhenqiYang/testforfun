from django.shortcuts import render,redirect # 导入重定向函数
from datetime import date
from django.http import HttpResponse,HttpResponseRedirect

from django.shortcuts import render
from django.conf import settings
from django.http import HttpResponse,JsonResponse

from Dublin_map.models import BookInfo,Bus_Locations







def index(request):

    return HttpResponse('hello World !')


def static_test(request):
    print(settings.STATICFILES_FINDERS)
    return render(request, 'Dublin_map/test.html',{'city':'Paris'})


def static_money(request):
    return render(request, 'Dublin_map/money.html',{'money':'dollars'})




def database(request):
    books = BookInfo.objects.filter(btitle ="47")
    return render(request, 'Dublin_map/database.html', {'books':books})


def bus_stop(request):
    stops = Bus_Locations.objects.all()

    return render(request, 'Dublin_map/bus_stop.html', {'stops':stops})





def create(request):
    b = BookInfo()
    bb='999y'
    bbdate="1385-01-25"
    b.btitle = bb
    b.bpub_date = bbdate
    b.save()
    return HttpResponse('ok')
    # return HttpResponseRedirect('/index')
    # return redirect('/index')


def delete(request, bid):

    book = BookInfo.objects.get(id=3)
    book.delete()
    # return HttpResponseRedirect('/index')
    return redirect('Dublin_map/test.html')


def btitle(request):

    btitle = BookInfo.objects.get(btitle='47')


    return render(request, 'Dublin_map/btitle.html', {'btitle':'btitle'})



def send_json(request):
    stops = Bus_Locations.objects.filter()

    stop_list = []
    for stop in stops:
        stop_list.append((stop.stop_id,stop.stop_name,stop.latitude, stop.longitude))

    return JsonResponse({'data':stop_list})

# def send_json1(request):
#     stops = Bus_Locations.objects.filter()
#
#     stop_dic =[]
#     for stop in stops:
#         sop={"id": stop.stop_id, "name": stop.stop_name, "latitude": stop.latitude, "longitude": stop.longitude}
#         dd=stop_dic.append(sop)
#         ddd={dd}
#     return JsonResponse(ddd)
#







