from library.search_engine.Search import Search
from library.search_engine.SearchResult import SearchResult
from library.search_engine.src import makeLink


class Bing(Search):
    prevLength = 0
    currLength = 0

    def __init__(self, query, prevLength):
        self.prevLength = prevLength
        super().__init__(query)

    def generateSearchLink(self):
        # todo
        #     1. generate search link: joiners and replace special chars
        #     2. results page link
        #     3. return the link fully formed
        link = "http://www.bing.com/search?q={}&ie=utf-8&oe=utf-8".format(makeLink(self.query))
        link = self.resultsPageLink(link)
        return link

    def resultsPageLink(self, currLink):
        if self.prevLength != 0:
            extension = "&first=" + str(self.prevLength + 1)
            o = currLink + extension
            return o
        else:
            return currLink

    def makeSearchResults(self, data):
        results = data.find_all('li', attrs={'class': 'b_algo'})
        self.currLength = len(results)
        for result in results:
            try:
                link = result.find('h2').find('a').get('href')
                if link in self.linksCollection:
                    continue
                self.linksCollection.append(link)
                title = result.find('h2').find('a').contents[0]
                extract = result.select("p")[0].text.strip()
                # print("Title: ", title)
                # print("Link: ", link)
                # print("Extract: ", extract)
                new = SearchResult(title, link, extract)
                self.results.append(new)
            except Exception:
                pass


# b = Bing("guardians of the galaxy", 0)
# b.makeSearches()
