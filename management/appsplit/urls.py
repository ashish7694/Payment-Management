
from django.urls import path
from .views import *
# from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView

urlpatterns = [
    path("home/", home, name='home'),
    path("login/", login, name='login'),
    path('logout/', logout_view, name='logout'),
    path('add_transaction/', add_transaction, name='add_transaction'),
    path('transaction_success/', transaction_success, name='transaction_success'),
    # path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    # path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
]
