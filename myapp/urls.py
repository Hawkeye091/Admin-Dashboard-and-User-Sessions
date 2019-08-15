from myapp import views
from django.urls import path
from django.conf.urls import url
app_name='myapp'

urlpatterns = [
    url(r'^register/$',views.register,name='register'),
    url(r'^user_login/$',views.user_login,name='user_login'),
]