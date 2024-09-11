from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Vintage Bag',
        'price': 'Rp1500000',
        'description': 'Tas vintage branded bekas',
        'category' : 'Tas',
        'brand' : 'Versace',
        'condition' : 'Good condition, tidak ada cacat',
        'stock' : '1',

    }

    return render(request, "main.html", context)