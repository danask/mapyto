from django.shortcuts import render, redirect
from .mapyto_api import Mapyto


#MaPyto API view
def mapyto_api(request):
    #Handle the form
    if request.method == 'POST':

        i = 0
        number = request.POST.get("numb")
        addresses_list = []

        #Create a list with all of the addresses
        while i < int(number):
            address = request.POST.get(f"address_{i}")

            addresses_list.append(address)
            i += 1

        #Use the API and handle errors
        try:
            mp = Mapyto(addresses_list, mode="django")
        except AttributeError:
            addresses_list = [[i,addresses_list.index(i)] for i in addresses_list]
            return render(request, "mapyto.html", context={"content": addresses_list, "i": len(addresses_list), "error": True})

        #Send the URL to the page
        return render(request, "mapyto.html", context={"url": mp.url})

    #Basic render
    else:
        return render(request, "mapyto.html")