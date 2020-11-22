from django.urls import path

from . import views

urlpatterns = [path("", views.LineChartsView.as_view(), name="plot")]