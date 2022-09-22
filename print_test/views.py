from django.shortcuts import render
from django.views import View
from django_pdf_overlay.models import Document

# Create your views here.


class PrintTestView(View):
    def get(self, request, *args, **kwargs):
        doc = Document.objects.get(name='test')
        doc.render_pages(card_data={'test_image': 'media/blank-profile-picture.jpg'})
        return doc.render_as_response()
