from .import views
from django.urls import path

urlpatterns = [
    path("", views.index, name="class"),
    path("register", views.register, name="register"),
    path("product/<int:id>", views.product, name="product")
]