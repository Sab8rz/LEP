from django.shortcuts import render
from .forms import LepCalculateForm
from .utils import LepCalculator
from django.views.generic import FormView


# class Index(FormView):
#     form_class = LepCalculateForm
#     template_name = 'lep/lep_form.html'
#
#     def form_valid(self, form):
#         data = form.cleaned_data
#         calc = LepCalculator(**data)
#         res = calc.calculate_all()
#         return render(self.request, 'lep/result.html', {'result': res})


def index(request):
    return render(request, 'lep/index.html')
