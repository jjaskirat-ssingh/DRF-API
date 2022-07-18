from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken.views import obtain_auth_token

# from core.views import test_view
from core.views import TestView

urlpatterns = [ 
    path('api-auth/', include('rest_framework.urls')),
    path('rest-auth/', include('rest_auth.urls')),
    path('admin/', admin.site.urls),
    # path('', test_view, name='test')
    path('', TestView.as_view(), name='test'),
    path('api/token/', obtain_auth_token, name='obtain-token')
]
