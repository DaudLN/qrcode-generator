from django.http import HttpResponse, JsonResponse
from django.shortcuts import render
import qrcode

from . import models
# Create your views here.

def events_view(request):
    context = return_context()
    return JsonResponse(context)

def render_events(request):
    context = return_context()
    return render(request, "events/main.html", context)


def render_qrcode_template(request):
    qrcodes = list(models.QRCodeImage.objects.all().values())
    context = dict(qrcodes=qrcodes)
    return render(request, "events/qrcode.html", context)


def generate_bar_code(request):

    import uuid
    id = uuid.uuid4()
    url = request.POST.get("url")
    context = None
    origin = request.META['HTTP_ORIGIN']
    if(models.QRCodeImage.objects.filter(url=url)):
        image_url = list(models.QRCodeImage.objects.filter(url=url).values())
        context = dict(image_url=image_url[0], origin=origin)

    else:
        qrcode_image = qrcode.make(url)
        image = qrcode_image.save(f"media/image-{id.hex}.png")
        qrimage_url = f"image-{id.hex}.png"
        qrcode_model = models.QRCodeImage(url=url, image=qrimage_url)
        qrcode_model.save()
        image_url = list(models.QRCodeImage.objects.filter(image=qrimage_url).values())
        context = dict(image_url=image_url[0], origin=origin)
    return JsonResponse(context)
