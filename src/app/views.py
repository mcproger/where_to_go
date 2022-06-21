from django.http import HttpResponse, HttpRequest
from django.shortcuts import render


def main(request: HttpRequest) -> HttpResponse:
    return render(request, 'main.html')
