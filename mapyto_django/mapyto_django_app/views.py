from django.shortcuts import render, redirect
from .mapyto_api import Mapyto

#Index view
def index(request):
    #Handle the form
    if request.method == 'POST':
        #Get the rows from the form and prevent XSS
        try:
            rows = int(request.POST['rows_number'])
        except ValueError:
            return render(request, "index.html", context={"error": True})

        #Check if rows is greater than or equal to 3
        if rows <= 2:
            return render(request, "index.html", context={"error": True})
        else:
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
            adress = request.POST.get(f"{rows - i}")

            adresses_list.append(adress)
            i -= 1

        #Use the API and handle errors
        try:
            mp = Mapyto(adresses_list, mode="django")
        except AttributeError:
            rows = [i for i in range(rows)]
            return render(request, "mapyto.html", context={"rows": rows, "error": True})

        #Send the URL to the page
        return render(request, "mapyto.html", context={"url": mp.url})

    #Basic render
    else:
        rows = [i for i in range(rows)]
        return render(request, "mapyto.html", context={"rows": rows})