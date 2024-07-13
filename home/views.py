from django.shortcuts import render, redirect
from .models import Product
from django.http import JsonResponse
from .forms import QuoteRequestForm
from django.core.mail import send_mail
from django.conf import settings


def homepage(request):
    return render(request, 'index.html')


def index_view(request):
    fish_feed = Product.objects.filter(category='fish')
    cattle_feed = Product.objects.filter(category='cattle')
    chicken_feed = Product.objects.filter(category='chicken')
    context = {
        'fish_feed': fish_feed,
        'cattle_feed': cattle_feed,
        'chicken_feed': chicken_feed,
    }
    return render(request, 'index.html', context)

def get_quote(request):
    if request.method == 'POST':
        form = QuoteRequestForm(request.POST)
        if form.is_valid():
            form.save()
            # Send email
            send_mail(
                'New Quote Request',
                f"Name: {form.cleaned_data['name']}\nEmail: {form.cleaned_data['email']}\nPhone: {form.cleaned_data['phone']}\nMessage: {form.cleaned_data['message']}",
                settings.DEFAULT_FROM_EMAIL,
                [settings.ADMIN_EMAIL],
                fail_silently=False,
            )
            return JsonResponse({'success': True, 'message': 'Your request has been submitted successfully.'})
        else:
            return JsonResponse({'success': False, 'message': 'There was an error submitting your request.'})
    else:
        form = QuoteRequestForm()
    return render(request, 'index.html', {'form': form})