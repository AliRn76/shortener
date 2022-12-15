from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect

from config.settings import BASE_URL, TITLE, DESCRIPTION
from app.serializers import CreateSerializer
from app.models import Url


class CreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CreateSerializer(data=request.data)
        context = {'title': TITLE, 'description': DESCRIPTION}
        if serializer.is_valid():
            url = Url.objects.create(**serializer.validated_data)
            context['shortened'] = f'{BASE_URL}/{url.shortened}'
        else:
            context['shortened'] = 'Invalid URL'
        return render(request, 'index.html', context=context)

    def get(self, request, *args, **kwargs):
        context = {'title': TITLE, 'description': DESCRIPTION}
        return render(request, 'index.html', context=context)


class RedirectAPIView(APIView):
    def get(self, request, url, *args, **kwargs):
        url = Url.objects.filter(shortened=url).last()
        if url:
            return redirect(to=url.original)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
