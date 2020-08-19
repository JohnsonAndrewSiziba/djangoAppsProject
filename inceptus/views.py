import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

from library.search_engine.SearchEngine import SearchEngine


def index(request):
    return HttpResponse("Hello, world. You're at the polls index.")


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
