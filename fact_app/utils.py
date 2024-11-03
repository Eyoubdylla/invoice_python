from django.core.paginator import (Paginator, EmptyPage, PageNotAnInteger)
from .models import Invoice
def pagination(request, invoices):
     # default page
        default_page = 1
        page = request.GET.get('page',default_page)
        #paginate item
        items_per_page = 5
        paginator = Paginator(invoices, items_per_page)
        try:
            items_page = paginator.page(page)
            
        except PageNotAnInteger :
            items_page = paginator.page(default_page)
        except EmptyPage :
            items_page = paginator(paginator.num_pages)
        return items_page

def get_invoice(pk):
    """get invoice  function"""
    obj=Invoice.objects.get(pk=pk)
    articles = obj.article_set.all()
    context = {
        'obj':obj,
        'articles' : articles
    }
    return context
    
       
    