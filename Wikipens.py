import wikipedia

def wikipen(query):
    try:
        pagefound=True
        results=wikipedia.search(query,[0])  
        page=wikipedia.page(results)
        tittle=page.title
        url=page.url
        summary=wikipedia.summary(results,sentences=6)
        image=page.images
    except:
        pagefound=False
        tittle=query
        url="https://en.wikipedia.org/wiki/"+query
        summary="no summary can be found"
        image=["no images found"]
    return tittle,url,summary,image,pagefound

def suggestions(query,num_results):
    try:
        results=wikipedia.search(query,results=num_results)
    except:
        results=["No results found"]
    return results


def contenttor(query):
    try:
        pagefound=True
        page=wikipedia.page(query)
        cont=page.content
        url=page.url
        tittle=page.title
    except:
        pagefound=False
        tittle=query
        url="https://en.wikipedia.org/wiki/"+query
        cont="cannot scrape the content of this page"
    return tittle,url,cont,pagefound