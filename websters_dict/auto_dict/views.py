from django.shortcuts import render
from urllib.request import urlopen

def make_url(word):
    url = "http://www.dictionaryapi.com/api/v1/references/collegiate/xml/"
    url += word + "?key=e2595b47-f120-4361-8aa7-bb3a7eb3c5f6"
    return url




def index(request):

    if request.method == 'POST':
        word = request.POST.get('word', '').strip()
        print(word * 9)

        url = make_url(word)

        print("trying to open your url\n\n")
        html = urlopen(url)
        print("Opened! our url! Now trying to read\n\n")
        text = html.read()
        print("Read!! Yay!! Finished!\n\n")
        if type(text) != type("string"):
            text = text.decode("utf-8")


        index = text.find("def")
        index = text.find("dt", index)
        index = text.find(":", index) + 1
        end = text.find("</dt", index)

        definition = text[index : end ]
        print(definition)
        return render(request, 'auto_dict/index.html', {'word' : word, 'definition' : definition})
    
    return render(request, 'auto_dict/index.html')
