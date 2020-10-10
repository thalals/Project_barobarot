from django.urls import path
from . import views


app_name='payments'

urlpatterns = [
    path('reservation/', views.PaymentproductList.as_view(), name="reservation"),
    #<int:engineer_pk> 연결 필요
    path('paymentproduct/create/<int:product_pk>/<int:user_pk>/', views.PaymentproductCreate, name="paymentproduct_create"),
    path('paymentproduct/<int:pk>/',views.payment_do.as_view(), name = "payment_do"),
    path('order_success/<int:user_pk>/<int:payment_pk>/', views.order_success, name="order_success")
]
