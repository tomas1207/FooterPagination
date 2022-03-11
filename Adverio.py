


def call_around(around,current_page):
        listofaroundpages = list(range(max(current_page - around,2), current_page + around+1)) 
        
        return listofaroundpages

def boundaties_call(boundaries,page_list):
        max_page = page_list[boundaries * -1:]
        min_page = page_list[0: boundaries]
        lista = max_page
        lista.extend(min_page)
        lista.sort()
        return lista

def get_limts(page_list,max,min):
        max_page = page_list[max]
        min_page = page_list[min]
        return [min_page,max_page]
        

def build_list(page_list,pagination):
        pagecalc =get_limts(page_list,-1,0)

        pagecalc.extend(call_around(pagination["around"],pagination["current_page"]))
        pagecalc.sort()
        pagecalc.extend(boundaties_call(pagination["boundaries"], page_list))
        pagecalc.sort()
        setofpages = set(pagecalc)
        listofpages = list(setofpages)
        listofpages.sort()
        return listofpages

def check_list(pagination):
        if pagination["total_pages"] <= 0:
                return "Invalid Number of pages"
        elif pagination["current_page"] > pagination["total_pages"]:
                return "Invalid current page"
        elif pagination["boundaries"] < 0 or pagination["around"] < 0:
                return "Boundaries or around are bellow 0"
        else:
                return build_list(list(range(1,pagination["total_pages"]+1)), pagination)
        


pagination = {
        "current_page":10,
        "total_pages":500000,
        "boundaries":2,
        "around":2,
        }
print(check_list(pagination))
