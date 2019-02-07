from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.board,name="django"),
    path('new/', views.new, name="dj_new"),
    path('create/',views.create,name="dj_create"),
    path('<int:post_id>',views.detail,name="dj_detail"),
]