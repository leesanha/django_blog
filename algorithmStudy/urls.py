from django.urls import path
from . import views

urlpatterns = [
    path('',views.board, name="algorithm"),
    path('new/',views.new, name="al_new"),
    path('create/',views.create, name="al_create"),
    path('<int:post_id>/',views.detail,name="al_detail"),
    path('more/',views.more, name="al_more"),
]