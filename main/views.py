from django.shortcuts import render, redirect
from pytube import YouTube
import os
from django.http import HttpRequest
import mimetypes
from django.http.response import HttpResponse
import unidecode

# Create your views here.


def home(request):
    if request.method == "POST":
        if request.POST["type"] == 'mp3':
            try:
                link = request.POST['link']
                yt = YouTube(link)
                vid = yt.streams.filter(only_audio=True).first()
                downloaded_file = vid.download('main\\tmp\\')
                base, ext = os.path.splitext(downloaded_file)
                new_file = base + '.mp3'
                os.rename(downloaded_file, new_file)

            except:
                os.remove(downloaded_file)
        elif request.POST["type"] == 'mp4':
            try:
                link = request.POST['link']
                yt = YouTube(link).streams.get_highest_resolution()

                new_file = yt.download('main\\tmp\\')

            except:
                os.remove(downloaded_file)

        htmlname = new_file.split("\\")[-1]
        #I dont know why but downloader has problem with diacritic(ˇ)
        filename = unidecode.unidecode(htmlname)
        filepath = new_file
        path = open(filepath, 'rb')
        mime_type, _ = mimetypes.guess_type(filepath)
        response = HttpResponse(path, content_type=mime_type)
        response['Content-Disposition'] = "attachment; filename=%s" % filename
        return response

    return render(request, 'main/home.html', {})
