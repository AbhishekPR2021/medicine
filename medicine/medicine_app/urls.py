from django.urls import path

from medicine_app import views
app_name='medicine_app'
urlpatterns=[
    path('',views.home,name='home'),
    path('<slug:c_slug>/', views.home, name='products_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.ProdCatDetail, name='product_details')

]