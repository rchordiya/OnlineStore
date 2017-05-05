from django.shortcuts import render
from geopy.geocoders import Nominatim
from geopy.distance import great_circle
from . models import Store



def store(request):
    store_details = Store.objects.all()
    return render(request, 'index.html', {'store_details': store_details})

def location(request):
    return render(request, 'location.html', {})

def searchedlocation(request):
    if request.method == 'GET':
        geolocator = Nominatim()
        searchthis = request.GET.get('locationentered')
        location = geolocator.geocode(searchthis)
        userEnteredSearch = (location.latitude, location.longitude)
    else:
        userEnteredSearch = ( request.POST['lat'], request.POST['long'] )
    storeList = []
    storesFromDatabase = Store.objects.all()
    for object in storesFromDatabase:
        lat= object.latitude
        long = object.longitude
        fromDatabase = (lat, long)
        myDistance = great_circle(userEnteredSearch, fromDatabase).miles
        if myDistance < 10:
            storeObject = [object.name,object.address,object.id]
            storeList.append(storeObject)

    context = {
        'storeList': storeList
    }
    return render(request, 'storedetails.html', context)

def storecontains(request, store_id):
    print("Store id: ")
    print(store_id)
    nameOfStore = ''
    iterateOverStores = Store.objects.all()
    for ourStore in iterateOverStores:
        if str(ourStore.id) == str(store_id):
            nameOfStore = ourStore.name
            break
    return render(request, 'storecontains.html', {'nameOfStore' : nameOfStore})



