from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

from .forms import SearchForm
from .services import YtInfo
from pytube import Caption


# Create your views here.
def index(request):
    form = SearchForm()
    return render(request, 'index.html', {'form': form})


def download(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            url = form.cleaned_data['url']
            service = YtInfo(url)
            info = service.yt_info()
            return render(request, 'video.html', {'info': info, 'url': url})
    else:
        form = SearchForm()
    return render(request, 'index.html', {'form': form})


def caption_to_srt(request):
    url = request.GET.get('caption_url')
    caption = Caption({"baseUrl": url, "name": {"simpleText": "a"}, "languageCode": "b"})
    response = HttpResponse(content_type='text/srt')
    response['Content-Disposition'] = 'attachment; filename="caption.srt"'
    response.write(caption.generate_srt_captions())
    return response
