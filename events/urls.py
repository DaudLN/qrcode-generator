from django.urls import path
from . import views

urlpatterns = [
    path("events/", views.render_events, name="events"),
    path("qrcode/", views.render_qrcode_template, name="qrcode"),
    path("qrgen/", views.generate_bar_code, name="qrcode-generator")

]
