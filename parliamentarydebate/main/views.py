from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import teams,adjudicators
from .forms import IndependentAdjudicatorCreationsForm,institutionCreationsForm,crossOpenCreationsForm
from django.utils.html import strip_tags
# Create your views here.
def home(request):
    return render(request,'main/pd.html')


def registerInstitute(request):
        instituteForm = institutionCreationsForm(request.POST or None)
        if request.method == 'POST':
            if instituteForm.is_valid():
                result = instituteForm.save(commit=False)
                result.save()
        else:
           instituteForm = institutionCreationsForm()
        return render(request, 'main/form1.html', {'InstituteForm': instituteForm, })

def registerAdjudicators(request):
        adjudicatorsForm = IndependentAdjudicatorCreationsForm(request.POST or None)
        if request.method == 'POST':
            if adjudicatorsForm.is_valid():
                result = adjudicatorsForm.save(commit=False)
                result.save()
        else:
           adjudicatorsForm = IndependentAdjudicatorCreationsForm()
        return render(request, 'main/form2.html', {'AdjudicatorsForm': adjudicatorsForm, })

def registerCrossOpen(request):
        crossopenForm = crossOpenCreationsForm(request.POST or None)
        if request.method == 'POST':
            if crossopenForm.is_valid():
                result = crossopenForm.save(commit=False)
                result.save()
        else:
           crossopenForm = crossOpenCreationsForm()
        return render(request, 'main/form3.html', {'CrossopenForm': crossopenForm, })
