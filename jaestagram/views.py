from django.shortcuts import render
from rest_framework.views import APIView


class Sub(APIView):
    def get(self, request):
        print("get으로")
        return render(request, "myinstagram/main.html")

    def post(self, request):
        print("post로")
        return render(request, "myinstagram/main.html")