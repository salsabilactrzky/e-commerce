from django.shortcuts import render

def show_main(request):
    context = {
        'name' : 'Vintage Bag',
        'price': 'Rp1500000',
        'description': 'Tas vintage branded bekas yang masih bagus',
        'category' : 'Tas',
        'condition' : 'Good condition, tidak ada cacat',
        'stock' : '1',
        'image' : '',
        'brand' : 'Louis Vuitton',
        'sold' : 'Sold',
    }

    return render(request, "main.html", context)