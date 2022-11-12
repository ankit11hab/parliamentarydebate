from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import teams,adjudicators,crossOpen
from .forms import IndependentAdjudicatorCreationsForm,institutionCreationsForm,crossOpenCreationsForm
from django.utils.html import strip_tags
# Create your views here.
def home(request):
    return render(request,'main/pd.html')


# def registerInstitute(request):
#         instituteForm = institutionCreationsForm(request.POST or None)
#         if request.method == 'POST':
#             if instituteForm.is_valid():
#                 result = instituteForm.save(commit=False)
#                 result.save()
#         else:
#            instituteForm = institutionCreationsForm()
#         return render(request, 'main/form1.html', {'InstituteForm': instituteForm, })

# def registerAdjudicators(request):
#         adjudicatorsForm = IndependentAdjudicatorCreationsForm(request.POST or None)
#         if request.method == 'POST':
#             if adjudicatorsForm.is_valid():
#                 result = adjudicatorsForm.save(commit=False)
#                 result.save()
#         else:
#            adjudicatorsForm = IndependentAdjudicatorCreationsForm()
#         return render(request, 'main/form2.html', {'AdjudicatorsForm': adjudicatorsForm, })

# def registerCrossOpen(request):
#         crossopenForm = crossOpenCreationsForm(request.POST or None)
#         if request.method == 'POST':
#             if crossopenForm.is_valid():
#                 result = crossopenForm.save(commit=False)
#                 result.save()
#         else:
#            crossopenForm = crossOpenCreationsForm()
#         return render(request, 'main/form3.html', {'CrossopenForm': crossopenForm, })


def updatedata(request):
    if request.method=='POST':
        if request.POST.get('contactno1') and request.POST.get('POCname') and request.POST.get('email') and request.POST.get('teamSlots') and request.POST.get('info'):
            team=teams()
            team.POCname=request.POST.get('POCname')
            team.college=request.POST.get('college')
            team.email=request.POST.get('email')
            team.contactno=request.POST.get('contactno1')
            team.teamSlots=request.POST.get('teamSlots')
            team.info=request.POST.get('info')
            team.save()
            return redirect('/')
        if request.POST.get('name') and request.POST.get('college2') and request.POST.get('contactno3') and request.POST.get('email') and request.POST.get('tourname') and request.POST.get('format') and request.POST.get('size') and request.POST.get('year') and request.POST.get('awards') and request.POST.get('outroundSpoken') and request.POST.get('pob') :
            adjudicator=adjudicators()
            adjudicator.name=request.POST.get('name')
            adjudicator.college=request.POST.get('college2')
            adjudicator.contactno=request.POST.get('contactno3')
            adjudicator.email=request.POST.get('email')
            adjudicator.TournamentName=request.POST.get('tourname')
            adjudicator.Format=request.POST.get('format')
            adjudicator.Year=request.POST.get('year')
            adjudicator.POB=request.POST.get('pob')
            adjudicator.OutroundSpoken=request.POST.get('outroundSpoken')
            adjudicator.awards=request.POST.get('awards')
            adjudicator.Size=request.POST.get('size')
            adjudicator.info=request.POST.get('info')
            adjudicator.save()
            return redirect('/')
        if request.POST.get('teamName') and request.POST.get('POCname') and request.POST.get('country') and request.POST.get('contactno2') and request.POST.get('email') and request.POST.get('info'):
            crossopen=crossOpen()
            crossopen.TeamName=request.POST.get('teamName')
            crossopen.Name_of_Poc=request.POST.get('POCname')
            crossopen.Country=request.POST.get('country')
            crossopen.contactno=request.POST.get('contactno2')
            crossopen.email=request.POST.get('email')
            crossopen.info=request.POST.get('info')
            crossopen.save()
            return redirect('/')

