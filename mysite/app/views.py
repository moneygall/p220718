from django.shortcuts import render, redirect
from django.views import View
import requests
import json
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator

#++++++++++++++++++++++++++++++++++++++
# 初期画面
#++++++++++++++++++++++++++++++++++++++
class IndexView(View):
    template_name = "app/index.html"
    
    def get(self, request,*args, **kwargs):
        context={
            "title": "webhookTest"
        }
    
        return render(request, self.template_name, context)    

#--------------------------------------------------------------------
# データ送信
#--------------------------------------------------------------------    
def SendData(request):
    webhook_url = "http://127.0.0.1:5000/webhook"
    data = {
        "name": "kazutaka",
    }

    r= requests.post(webhook_url, data = json.dumps(data), headers={
        'Content-Type': 'application/json'
    })
    
    return redirect("/")

#++++++++++++++++++++++++++++++++++++++
# データ受信
#++++++++++++++++++++++++++++++++++++++
@method_decorator(csrf_exempt, name='dispatch')
class RecieveDataView(View):
    template_name = "app/recieve.html"
    
    def get(self, request,*args, **kwargs):
        context={
            "title": "webhookRecieveTest",
            "message": "ここに名前を表示したい"
        }
    
        return render(request, self.template_name, context)    
    
    def post(self, request,*args, **kwargs):
        data= json.loads(request.body)
        name= data["name"]
        print(name)

        context={
            "title": "webhookRecieveTest",
            "message": name
        }
    
        return render(request, self.template_name, context)    
