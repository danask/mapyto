from django.shortcuts import render, redirect
from .mapyto_api import Mapyto


def index(request):
    if request.method == 'POST':
        rows = request.POST['rows_number']
        return redirect(f"/mapyto&rows={rows}")

    else:
        return render(request, "index.html")


def mapyto_api(request, rows):
    if request.method == 'POST':

        i = rows
        adresses_list = []

        while i:
            adresses_list.append(request.POST.get(f"{rows - i}"))
            i -= 1

        mp = Mapyto(adresses_list, mode="django")

        return redirect(mp.url)


    else:
        rows = [i for i in range(rows)]
        return render(request, "mapyto.html", context={"rows": rows})