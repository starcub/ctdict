from django.template import Context, loader, RequestContext
from ctdict.dict.models import Word
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404

def index(request):
    latest_words = Word.objects.all().order_by('addedTime')[:10]
    t = loader.get_template('dict/index.html')
    c = Context({
        'latest_words': latest_words,
        })
    return render_to_response('dict/index.html',
                          c,
                          context_instance=RequestContext(request))

    
def term(request, word):
    newWord = Word.objects.filter(term=word)
    meaning = newWord[0].meaning
    example = newWord[0].example
    t = loader.get_template('dict/term.html')
    c = Context({
        'newWord': newWord,
        'meaning': meaning,
        'example': example,
        })
    return HttpResponse(t.render(c))
    
def meaning(request, term):
    return HttpResponse("You'are looking %s" % term)