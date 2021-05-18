#I have created this file

from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request,'index.html')

def analyze(request):
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover =request.POST.get('newlineremover','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')


    if removepunc == "on":
        analyzed=""
        punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose': 'Removed punctuations', 'analyzed_text': analyzed}
        djtext=analyzed


    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params = {'purpose': 'Converted to Upper case', 'analyzed_text': analyzed}
        djtext = analyzed


    if (newlineremover == 'on'):
        analyzed = ""
        for char in djtext:
            if char!="\n" and char!="\r":
                analyzed = analyzed +char
        params = {'purpose': 'new line removed', 'analyzed_text': analyzed}
        djtext = analyzed


    if (extraspaceremover == 'on'):
        analyzed = ""
        for pos, char in enumerate(djtext):
            if not(djtext[pos] == " " and djtext[pos+1] == " "):
                analyzed = analyzed + char
        params = {'purpose': 'extra space removed', 'analyzed_text': analyzed}
        djtext = analyzed


    if(removepunc != "on" and fullcaps !='on' and newlineremover != 'on' and extraspaceremover != 'on'):
        return HttpResponse("Please select the operation")

    return render(request, 'analyze.html', params)
