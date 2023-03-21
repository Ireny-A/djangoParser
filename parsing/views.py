from django.shortcuts import render, redirect
from django.views import generic
from parsing.models import Note
from parsing.parse_bmw import ParserBMW
from parsing.parse_audi import ParserAu
from parsing.parse_mercedes import ParserMerc


def home(request):
    if request.method == 'POST':
        brand = request.POST.get("brand")
        print(f"brand: {brand}")
        if brand == "BMW":
            ParserBMW().main()
        elif brand == "Audi":
            ParserAu().main()
        elif brand == "Mercedes":
            ParserMerc().main()
        else:
            print("No brand passed")
        # p.delete()
        return redirect('view')
    else:
        return render(request, 'home.html')


def view_rez(request):
    notes = Note.objects.all()
    return render(request, 'view_rez.html', {'notes': notes})
