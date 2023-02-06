from django.urls import path
from . import views

urlpatterns = [
    path("", views.render_qrcode_template, name="qrcode"),
    path("events/", views.render_events, name="events"),
    path("qrgen/", views.generate_bar_code, name="qrcode-generator"),
]
