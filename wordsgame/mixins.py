from django.shortcuts import render
from django.http import HttpResponse
import json

class GameMixin:
    model = None
    template = None

    def get(self, request):
        #words = self.model.objects.all()
        return render(request, self.template)
    
    def post(self, requset):
        word = self.model.objects.order_by('?').first()
        return HttpResponse(json.dumps({'word':word.body,'c': word.correct}))