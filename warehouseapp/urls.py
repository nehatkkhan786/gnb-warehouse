from django.urls import path
from . import views

app_name = 'warehouse'

urlpatterns = [

	path('', views.homepage, name = 'homepage'),
	path('list/<int:pk>/add/', views.add_quantity, name = 'add_quantity'),
	path('list/<int:pk>/delete/', views.delete_quantity, name = 'delete_quantity'),
	path('add_product/', views.add_product, name = 'add_product'),
	

]
