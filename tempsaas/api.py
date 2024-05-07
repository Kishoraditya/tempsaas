from rest_framework import routers
from rest_framework.response import Response
from rest_framework.views import APIView
from wagtail.core.models import Page

class PageAPIViewSet(APIView):
    def get(self, request):
        pages = Page.objects.all()
        data = []
        for page in pages:
            data.append({
                'id': page.id,
                'title': page.title,
                'slug': page.slug,
                # Add any other fields you want to expose
            })
        return Response(data)

router = routers.DefaultRouter()
router.register(r'pages', PageAPIViewSet, basename='pages')
