from django.shortcuts import render
from django.views import View
from django_pdf_overlay.models import Document

# Create your views here.


class PrintTestView(View):
    def get(self, request, *args, **kwargs):
        doc = Document.objects.get(name='test')
        doc.render_pages(card_data={'test': 'TEST', 'test_image': 'media/student_photo/7f58f6a2-cc9d-4b9e-9415-8ce4c9156747.jpg'})
        return doc.render_as_response()
