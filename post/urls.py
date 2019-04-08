from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.home,name='home'),
    path('report/',views.report,name='report'),
    path('details/<int:report_id>',views.reportdetail,name='detail'),
    path('request/',views.requestitem,name='request')
]
