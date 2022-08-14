from django.shortcuts import render
import fractions
from .models import FractionalValue


# Create your views here.

def index(request):
    return render(request, 'index.html')


def fractionS(request):
    val1 = float(request.POST["radius"])
    res = val1
    frac = str(res)
    fractionalvalue = fractions.Fraction(frac).limit_denominator(5555500)

    if request.method == 'POST':

        #res = request.POST.get('radius')
        #frac = str(res)
        #fractionalvalue = fractions.Fraction(frac).limit_denominator(5555500)

        name = res
        answer = fractionalvalue       
        fracRc = FractionalValue(name=name,answer=answer)
        fracRc.save()
        return render(request, 'index.html', {'fraction': answer, 'value':name})

    return render(request, 'index.html', {'value':res, 'fraction': fractionalvalue})

def about(request):
    return render(request, 'about.html')
