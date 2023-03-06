import datetime
import random
import string
from django.shortcuts import render

from urlshortner.forms import CreateNewShortURL
from .models import priyanka

# Create your views here.
def home(request):
    return render(request,'home.html')

def redirect(request ,url):
    current_obj=priyanka.objects.filter(short_url=url)
    if len(current_obj)==0:
        return render(request,'pagenf.html')
    context={'obj':current_obj[0]}
    return render(request,'redirect.html',context)

def create(request):
    if request.method == 'POST':
        form=CreateNewShortURL(request.POST)
        if form.is_valid():
            original_website = form.cleaned_data['original_url']
            random_chars_list = list(string.ascii_letters)
            random_chars=''
            for i in range(6):
                random_chars += random.choice(random_chars_list)
            while len(priyanka.objects.filter(short_url=random_chars)) != 0:
                for i in range(6):
                    random_chars += random.choice(random_chars_list)
            d = datetime.datetime.now()
            s = priyanka(original_url=original_website, short_url=random_chars, time_date_created=d)
            s.save()
            return render(request, 'uncreated.html', {'chars':random_chars})
    
    else:
        form=CreateNewShortURL()
        context={'form': form}
        return render(request, 'create.html', context)