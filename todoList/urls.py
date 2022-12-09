from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.todoView, name='todo'),
                  path('search_task', views.search, name='search_task'),
                  path('update_task/<int:id>', views.updateTodo, name='update_task'),
                  path('delete_task/<int:id>', views.delete, name='delete_task'),
                  path('addTask', views.add, name='addTask'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
