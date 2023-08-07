from django.shortcuts import render
from django.views.generic import ListView,TemplateView
from app.forms import *
from django.http import HttpResponse
# Create your views here.

class Trainer_List(ListView):
    model=Trainer
    template_name='Trainer_List.html'
    context_object_name='tl'
    #queryset=Trainer.objects.filter(trainer_name='naru')
    ordering=['trainer_name']
    


class TempDataRender(TemplateView):
    template_name='TempDataRender.html'
    def get_context_data(self,**kwargs):
        context=super().get_context_data(**kwargs)
        context['name']='narasimha'
        return context

class TemplateInsertData(TemplateView):
    template_name='TemplateInsertData.html'
    def get_context_data(self,**kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=TrainerForm()
        ECDO['SFO']=SFO
        return ECDO

    def post(self,request):
        SFD=TrainerForm(request.POST)
        if SFD.is_valid():
            SFD.save()

            return HttpResponse('Inserting data complete.')