from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('item/<int:id>/', views.item_detail, name='item_detail'),
    path('buy/<int:id>/', views.create_checkout_session, name='create_checkout_session'),
    path('pay/<int:id>/', views.create_payment_intent, name='create_payment_intent'),
    path('success/', views.payment_success, name='payment_success'),
]