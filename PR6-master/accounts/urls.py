from django.contrib import admin
from django.urls import path

from accounts import views
from django.urls import path, include


urlpatterns = [

    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('accounts.urls')),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('', include('blog.urls'))

]