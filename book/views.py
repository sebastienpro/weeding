import os

import PIL

from PIL import Image
from PIL import ImageFilter
from book.forms import PageForm
from book.models import Page
from django.shortcuts import render, redirect
from mariage import settings


def home(request):
    pages = Page.objects.all().order_by("-pk")
    return render(request, "home.html", {'pages': pages, 'menu': 'home'})


def add_page(request):
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")
        else:
            return render(request, "add_page.html", {'form':form})
    else:
        form = PageForm()
        return render(request, "add_page.html", {"form": form})


def page_edit(request, page_id):
    page = Page.objects.get(pk=page_id)
    if request.method == "POST":
        form = PageForm(request.POST, request.FILES)
        if form.is_valid():
            page.name = form.cleaned_data["name"]
            page.title = form.cleaned_data["title"]
            page.content = form.cleaned_data["content"]
            if form.cleaned_data["image1"]:
                page.image1 = form.cleaned_data["image1"]
            if form.cleaned_data["image2"]:
                page.image2 = form.cleaned_data["image2"]
            page.save()
            return redirect("home")
        else:
            return render(request, "add_page.html", {'form': form})
    else:
        form = PageForm(instance=page)
        return render(request, "add_page.html", {'form': form})


def preview(request, page_id):
    page = Page.objects.get(pk=page_id)
    return render(request, "preview.html", {'page': page, 'image1': page.image1, 'image2': page.image2})


def _resize_image(image):
    new_image = image.name.replace("images/", "resized/")
    pil_image = Image.open(image.file)
    pil_image.thumbnail((600,600), PIL.Image.ANTIALIAS)
    pil_image.save(os.path.join('./media/', new_image))
    return os.path.join(settings.MEDIA_URL, new_image)


def photos(request):
    return render(request, "photos.html", {'menu': 'photos'})


def _generate_html_for_pdf(page):
    html_template = """<table width="900" style="font-family:tahoma, geneva, sans-serif;">
                <tr>
                    <td width="300"><img src='../%s' width="300"></td>
                    <td style="text-align: center"><h1>%s</h1></td>
                </tr>
                <tr height="20"><td colspan="2"></td></tr>
                <tr>
                    <td colspan='2'>
                        <table width='100%%'>
                            <tr>
                                <td width='80'></td>
                                <td>%s</td>
                                <td width='300' valign='bottom'>
                                    <img src='../%s' width="300">
                                </td>
                            </tr>
                        </table>
                    </td>
                </tr>
                <tr><td colspan="2" style="text-align: center; color:#337ab7; font-size: 30px">%s</td></tr>
            </table>"""%(page.image1.url, page.title, page.content, page.image2.url, page.name)
    return html_template