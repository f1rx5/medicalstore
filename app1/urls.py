from unicodedata import name
from django.urls import path,include
from . import views
urlpatterns=[
    path('home/',views.home,name='home'),
    path('medicine/',views.addmedicine,name='addmedicine'),
    path('billing/',views.billing,name='billing'),
    path('medbilling/',views.medbilling,name='medbilling'),
    path('stock/',views.stock,name='stock'),
    path('update/<str:id>',views.update,name='update'),
]