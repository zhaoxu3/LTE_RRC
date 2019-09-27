from django.shortcuts import render,render_to_response
from  goldenap import models
from django.http import JsonResponse
from django.shortcuts import HttpResponse
from django.http import HttpResponse
# Create your views here.
"""
list = [{'ie_data_id':1,'ap_name':'AC88U','phy_type':'2.4g_11n',\
        'ie_beacon':'2929dd','ie_probe':'fffff','ie_auth':'000000','ie_assoc':'EEEEE'}]
"""
"""
def index(request):
    return HttpResponse("hello world")
"""
d={'1.htldxhzj.duapp.com': 9398,
 'gtxapi.cdn.duapp.com': 79496,
 'www.xxx.com': 2477070,
 'www.baidu.com': 1465,
 'www.bing.com': 777,
 'www.aaa.com': 1113101,
 'www.ccc.net.cn': 922,
 'www.zhanimei.ga': 29847,
 'www.zhanimei.ml': 40155,
 'www.zhasini.ml': 373436}



def show(request):
    categories = d.keys()
    data = d.values()
    return render_to_response('show.html', {'user': request.user, 'categories': categories, 'data': data})


def index(request):
    list = models.IeData.objects.all()
    return render(request,'index.html',{'form':list})