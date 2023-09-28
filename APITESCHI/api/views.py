from django.shortcuts import render
from rest_framework.views import APIView

class Home(APIView):
    template_name="index.html"
    def get(self, request):
        return render (request, self.template_name)

class Forgot(APIView):
    template_name="forgot.html"
    def get(self, request):
        return render (request, self.template_name)
