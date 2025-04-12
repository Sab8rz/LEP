from django.shortcuts import render


def index(request):
    return render(request, 'lep/lep_form.html')