from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect

from config.settings import BASE_URL, TITLE, DESCRIPTION
from app.models import Url


class CreateAPIView(APIView):
    def post(self, request, *args, **kwargs):
        url = Url.objects.create(original=request.data['original'], shortened=request.data['shortened'])
        context = {'shortened': f'{BASE_URL}/{url.shortened}', 'title': TITLE, 'description': DESCRIPTION}
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
