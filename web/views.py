from django.shortcuts import render

def home(request):
    # later you’ll call your foxtrot code here
    context = {"message": "Foxtrot is running through Django!"}
    return render(request, "web/home.html", context)
# Create your views here.
