from django.contrib import admin
from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.todoView, name='todo'),
                  path('search', views.search, name='search'),
                  path('update/<int:id>', views.updateTodo, name='update'),
                  path('delete/<int:id>', views.delete, name='delete'),
                  path('add', views.add, name='add'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
