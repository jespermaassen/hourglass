from django.shortcuts import render
from .models import Market

# Create your views here.
def index(request):
    markets = Market.objects.all()
    print(markets)
    return render(request, "polls/index.html", context)