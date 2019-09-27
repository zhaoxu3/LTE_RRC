"""WebShow URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
admin.autodiscover()
from django.urls import re_path,path,include
from django.conf.urls import url
from goldenap import views
from WebShow import search2,search
#urlpatterns = patterns('',(r'^admin/',include(admin.site.urls)),
urlpatterns = [
    #path('goldenap/',include('goldenap.urls')), #即插即用
    url(r'^admin/', admin.site.urls),
    url('^search-form/$',search.search_form),
    url('^show/$',views.show),
    url('^search/$',search.search),
    url(r'^search-post/$', search2.search_post),
    #path('',r'^admin/',include(admin.site.urls)),
    re_path('',views.index)
]
urlpatterns += staticfiles_urlpatterns()
#******已经测试成功模式****************
