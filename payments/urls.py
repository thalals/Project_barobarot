from django.urls import path
from . import views


app_name='payments'

urlpatterns = [
    path('order_list/', views.PaymentproductList.as_view(), name="order_list"), # 주문 내역 리스트 페이지
    #<int:engineer_pk> 연결 필요
    path('paymentproduct/create/<int:product_pk>/<int:user_pk>/', views.PaymentproductCreate, name="paymentproduct_create"), # 주문 아이템 생성
    path('paymentproduct/<int:pk>/',views.payment_do.as_view(), name = "payment_do"), # 주문 페이지 입장
    path('order_success/<int:user_pk>/<int:payment_pk>/', views.order_success, name="order_success") # 주문 성공 페이지 입장
]
