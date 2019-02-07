from django.urls import path
from . import views

urlpatterns = [
    path(' ',views.board,name="os"),
    path('new/',views.new, name="new"),
    path('create/',views.create, name="create"),
    path('<int:post_id>',views.detail,name="detail"),
]