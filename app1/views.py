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
    views = BeautifulSoup(requests.get("https://www.youtube.com/channel/UCWJIPkkittn7HkKlbTwPriQ/about").content,'html.parser').find(class_="about-stat").get_text()
    print("\n\n\n\n\n\n\n")
    print(type(views))
    print("\n\n\n\n\n\n\n\n")
    #return HttpResponse("Hello World!")
    return render(request,'index.html',{'subsc':subc,'views':views})