from django.shortcuts import render, redirect
from .mapyto_api import Mapyto


#MaPyto API view
def mapyto_api(request):
    #Handle the form
    if request.method == 'POST':

        i = 0
        number = request.POST.get("numb")
        adresses_list = []

        #Create a list with all of the addresses
        while i < int(number):
            adress = request.POST.get(f"adress_{i}")

            adresses_list.append(adress)
            i += 1

        #Use the API and handle errors
        try:
            mp = Mapyto(adresses_list, mode="django")
        except AttributeError:
            rows = [i for i in range(1, int(number))]
            return render(request, "mapyto.html", context={"rows": rows, "index": len(rows)+1, "error": True})

        #Send the URL to the page
        return render(request, "mapyto.html", context={"url": mp.url})

    #Basic render
    else:
        return render(request, "mapyto.html")