import os
from uuid import uuid4
from django.db import models
from ckeditor.fields import RichTextField
from django.conf import settings


def path_and_rename(instance, filename):
    upload_to = 'images'
    ext = filename.split('.')[-1]
    if instance.pk:
        filename = '{}.{}'.format(instance.pk, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)


class Contributor(models.Model):
    name = models.CharField(max_length=255, null=False)
    description = models.TextField()
    path = models.CharField(max_length=255, null=False)

class Page(models.Model):
    name = models.CharField(max_length=100, null=False)
    title = models.CharField(max_length=100, null=False)
    content = RichTextField()
    image1 = models.ImageField(upload_to=path_and_rename, null=True, default=None)
    image2 = models.ImageField(upload_to=path_and_rename, null=True, default=None)

    @property
    def pdf_file(self):
        pdf_path = os.path.join(settings.MEDIA_ROOT, "pdfs", str(self.pk)+".pdf")
        pdf_url = os.path.join(settings.MEDIA_URL, "pdfs", str(self.pk)+".pdf")
        png_path = os.path.join(settings.MEDIA_ROOT, "pngs", str(self.pk)+".png")
        png_url = os.path.join(settings.MEDIA_URL, "pngs", str(self.pk) + ".png")

        if os.path.exists(pdf_path):
            return pdf_url
        elif os.path.exists(png_path):
            return png_url
        else:
            return None

    def __unicode__(self):
        return self.name+" / "+self.title
