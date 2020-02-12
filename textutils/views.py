#created by me
from django.http import HttpResponse
from django.shortcuts import render

def analyzer(request):
    return render(request,'analyzer.html')

def text(request):
    removepunk = request.POST.get('removepunk', 'off')
    djtext = request.POST.get('text', 'default')
    capitalize=request.POST.get('capitalize','off')
    extraspaceremover=request.POST.get('extraspaceremover','off')
    newlineremover=request.POST.get('newlineremover','off')
    params=""



    if capitalize=="on":
        analyzed = ""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'capitaliz','analyzed':analyzed}
        djtext=analyzed

    if (removepunk=="on"):
        analyzed = ""
        panchuation = '''!"#$%&'()*+,-./:;?@[\]^_`{|}~'''
        for char in djtext:
            if char not in panchuation:
                analyzed = analyzed + char

        params = {'purpose':'removepunck','analyzed': analyzed}
        djtext=analyzed

    if (extraspaceremover == "on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            # It is for if a extraspace is in the last of the string
            if char == djtext[-1]:
                if not (djtext[index] == " "):
                    analyzed = analyzed + char

            elif not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}
        djtext = analyzed

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text': analyzed}

    if ( removepunk !="on" and newlineremover != "on" and extraspaceremover != "on" and capitalize !="on" ):
        return HttpResponse("please select any operation and try again")

    return render(request, 'text.html', params)