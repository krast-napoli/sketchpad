from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('mysketchpad.urls')),
    path('events', TemplateView.as_view(template_name='event_list.html')),
]
