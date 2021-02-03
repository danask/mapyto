from django.shortcuts import render, redirect
from .mapyto_api import Mapyto

#Index view
def index(request):
    #Handle the form
    if request.method == 'POST':
        #Get the rows from the form
        rows = request.POST['rows_number']

        #Redirect to the API page
        return redirect(f"/mapyto&rows={rows}")

    #Basic render
    else:
        return render(request, "index.html")


#MaPyto API view
def mapyto_api(request, rows):
    #Handle the form
    if request.method == 'POST':

        i = rows
        adresses_list = []

        #Create a list with all of the addresses
        while i:
            adresses_list.append(request.POST.get(f"{rows - i}"))
            i -= 1

        #Use the API
        mp = Mapyto(adresses_list, mode="django")

        #Redirect to the Google Maps itinerary
        return redirect(mp.url)

    #Basic render
    else:
        rows = [i for i in range(rows)]
        return render(request, "mapyto.html", context={"rows": rows})