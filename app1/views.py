from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup

# Create your views here.


def index(request):
    print('here')
    content = requests.get("https://www.youtube.com/channel/UCWJIPkkittn7HkKlbTwPriQ").content
    soup = BeautifulSoup(content,'html.parser')
    subc = soup.find(class_="yt-subscription-button-subscriber-count-branded-horizontal").get_text()
    print("printing")
    print(subc)
    #return HttpResponse("Hello World!")
    return render(request,'index.html',{'subsc':subc})