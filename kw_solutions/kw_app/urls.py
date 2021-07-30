from django.urls import path
from kw_app import views

urlpatterns = [
    path("", views.render_index, name = "render_index")
]