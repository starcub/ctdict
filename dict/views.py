from django.template import Context, loader
from ctdict.dict.models import Word, Defination
from django.http import HttpResponse

def index(request):
    latest_words = Word.objects.all().order_by('createdTime')[:5]
    t = loader.get_template('dict/index.html')
    c = Context({
        'latest_words': latest_words,
        })
    return HttpResponse(t.render(c))
    
def term(request, word):
    pk = Word.objects.filter(term=word)
    newWord = Defination.objects.filter(ofWord=pk[0].id)
    meaning = newWord[0].meaning
    t = loader.get_template('dict/term.html')
    c = Context({
        'newWord': newWord,
        'meaning': meaning,
        })
    return HttpResponse(t.render(c))
    
def meaning(request, term):
    return HttpResponse("You'are looking %s" % term)
