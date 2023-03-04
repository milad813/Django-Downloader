import requests
from django.conf import settings
import os
from django.shortcuts import render

def index_view(request):
    return render(request, 'index.html')

def download_view(request):
    url = request.POST.get('url')
    print(url)
    filename = url.split('/')[-1]
    response = requests.get(url)
    file_path = os.path.join(settings.MEDIA_ROOT, filename)
    with open(file_path, 'wb') as f:
        f.write(response.content)
    download_url = request.build_absolute_uri(settings.MEDIA_URL + filename)
    return render(request, 'download.html', {'download_url': download_url})