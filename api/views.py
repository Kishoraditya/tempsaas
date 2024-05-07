from rest_framework import viewsets
from rest_framework.response import Response
from wagtail.models import Page

class PageAPIViewSet(viewsets.ViewSet):
    def list(self, request):
        pages = Page.objects.all()
        data = []
        for page in pages:
            data.append({
                'id': page.id,
                'title': page.title,
                'slug': page.slug,
            })
        return Response(data)
    
