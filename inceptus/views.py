import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.urls import reverse

from library.search_engine.SearchEngine import SearchEngine
from library.search_engine.SearchResult import SearchResult


def index(request):
    return render(request, 'inceptus/index.html')


def query(request):
    q = request.GET.get('query', None)
    searchEngine = SearchEngine(q)
    data = searchEngine.searchResults
    # one = SearchResult("Ariana Grande - Wikipedia", "http://www.wikipedia.org", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium adipisci aspernatur illo")
    # two = SearchResult("Ariana Grande - Wikipedia", "http://www.wikipedia.org", "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Accusantium adipisci aspernatur illo")
    # data = [one, two, one, one, one, one, one, two, one, one, one, one]
    return render(request, 'inceptus/results.html', {'data': data, 'query': q})
    # return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def results(request):
    q = request.GET['query']
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiii")
    print(q)
    print("iiiiiiiiiiiiiiiiiiiiiiiiiiii")
    # searchEngine = SearchEngine("The Umbrella Academy")
    # data = searchEngine.searchResults
    return render(request, 'inceptus/index.html')


def search(request):
    searchEngine = SearchEngine("The Umbrella Academy")
    results = searchEngine.searchResults

    resultsDict = {}
    searchResults = []

    for result in results:
        title = result.title
        link = result.link
        extract = result.extract

        resultsObject = {
            "title": title,
            "link": link,
            "extract": extract
        }

        searchResults.append(resultsObject)

    lengthObject = {
        "length": len(searchResults)
    }
    resultsDict["length"] = lengthObject
    resultsDict["results"] = searchResults

    return JsonResponse(resultsDict)
