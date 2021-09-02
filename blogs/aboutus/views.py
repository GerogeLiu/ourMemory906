from django.shortcuts import render

# Create your views here.

def about_us(request):
    return render(request, "aboutus/aboutus2.html")


def introduce2(request):
    return render(request, "aboutus/detail/bosi.html")

def introduce(request, name):
    print(name)
    return render(request, f"aboutus/detail/{name}.html")