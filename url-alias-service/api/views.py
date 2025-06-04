from django.db.models import Count
from django.shortcuts import get_object_or_404, redirect
from rest_framework import generics, status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import ShortLink, ClickStat
from .serializers import ShortLinkSerializer


class RedirectView(APIView):
    permission_classes = []

    def get(self, request, short_id):
        link = get_object_or_404(ShortLink, short_id=short_id)
        if not link.is_active or link.is_expired():
            return Response({'error': 'Link inactive or expired.'}, status=403)
        ClickStat.objects.create(link=link)
        return redirect(link.original_url)


class CreateShortLinkView(generics.CreateAPIView):
    queryset = ShortLink.objects.all()
    serializer_class = ShortLinkSerializer
    permission_classes = [IsAuthenticated]

    def post(self, request):
        serializer = ShortLinkSerializer(data=request.data)
        if serializer.is_valid():
            short_link = serializer.save()
            return Response({
                'short_url': f'http://127.0.0.1:8000/{short_link.short_id}/',
                'data': serializer.data
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ListShortLinksView(generics.ListAPIView):
    serializer_class = ShortLinkSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        queryset = ShortLink.objects.all()
        is_active = self.request.query_params.get('active')
        if is_active in ['true', 'false']:
            queryset = queryset.filter(is_active=(is_active == 'true'))
        return queryset


class DeactivateLinkView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request, short_id):
        link = get_object_or_404(ShortLink, short_id=short_id)
        link.is_active = False
        link.save()
        return Response({'status': 'deactivated'})


class StatsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        stats = (
            ClickStat.objects
            .values('link__short_id', 'link__original_url')
            .annotate(clicks=Count('id'))
            .order_by('-clicks')
        )
        data = [
            {
                'short_id': row['link__short_id'],
                'original_url': row['link__original_url'],
                'clicks': row['clicks']
            } for row in stats
        ]
        return Response(data)
