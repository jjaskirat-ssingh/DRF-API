from django.contrib import admin
from django.urls import include, path

# from core.views import test_view
from core.views import TestView

urlpatterns = [ 
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    # path('', test_view, name='test')
    path('', TestView.as_view(), name='test')
]