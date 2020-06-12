from django.shortcuts import render,redirect
from .forms import countryForm
import requests
from .converter import Currency

def index(request):
    form = countryForm()
    context = {
        'form':form
    }
    return render(request,'index.html',context)



def calculate(request):
    if request.method == "POST":
        form = countryForm(request.POST)
        if form.is_valid():
            fromCountry = form.cleaned_data['fromCountry']
            toCountry = form.cleaned_data['toCountry']
            amount = float(form.cleaned_data['amount'])
            fromCountry = Currency.getCurrency(fromCountry)
            toCountry = Currency.getCurrency(toCountry)
            url = 'https://free.currconv.com/api/v7/convert?q={}_{}&compact=ultra&apiKey=2ef6570e6f4b53d31407'.format(fromCountry,toCountry)
            key = fromCountry+'_'+toCountry
            json_data = requests.get(url).json()
            rate = json_data[key]
            result = format(rate * amount,'.2f')        
            context={
                'result':result
            }
            return render(request,'index.html',context)
    else:
        return redirect('/')