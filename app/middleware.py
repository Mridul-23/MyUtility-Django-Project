from django.shortcuts import render
from django.urls import resolve
from django.http import Http404

class Handle404Middleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_exception(self, request, exception):
        if isinstance(exception, Http404):
            try:
                resolve(request.path)
            except Http404:
                return self.handle_undefined_path(request)
        return None

    def handle_undefined_path(self, request):
        context = {
            'undefined_path': request.path,
        }
        return render(request, '404.html', context, status=404)
