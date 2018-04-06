"""
Setting up URL Dispatcher:
I added the from django.http import HttpResponse
I created the index function with a return of HttpResponse and some
HTML code.
See urls.py and settings.py

Setting up templates:
Changed the return from index function to render the index.html
file in templates.
Created class and list for treasures


"""

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html', {'treasures': treasures})


class Treasure:
    def __init__(self, name, value, material, location, img_url):
        self.name = name
        self.value = value
        self.material = material
        self.location = location
        self.img_url = img_url
        
#pictures not loading, continue to triage.
coffee_can = 'www.noworriesdevelopment.com/assets/images/treasuregram/coffeecan.jpg'
fools_gold = 'www.noworriesdevelopment.com/assets/images/treasuregram/foolsgold.jpg'
gold_nugget = 'www.noworriesdevelopment.com/assets/images/treasuregram/goldnugget.jpg'

treasures = [
Treasure('Gold Nugget', 500.00, 'gold', "Curly's Creek, NM", gold_nugget),
Treasure("Fool's Gold", 0, 'pyrite', "Fool's Falls, CO", fools_gold),
Treasure("Coffee Can", 20.00, 'tin', "Acme, CA", coffee_can),
]
