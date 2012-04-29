'''
Created on Jan 30, 2012

@author: desales
'''

import collections

from django.template.context import RequestContext
from django.shortcuts import render_to_response

from models import (
    Item, 
)

#TODO: Duplicated method, factor it ASAP!
def _build_categories(items):
    """Fetch categories for display  
    in inventory creation page."""
    categories = collections.OrderedDict()
    for item in items:
        myitems = categories.get(item.category, [])
        myitems.append(item)
        categories[item.category] = myitems 
    return categories 


def shoppinglist(request):
    items           = Item.objects.all().order_by('category')
    categories      = _build_categories(items)

    initialData = dict(
        items          = items, 
        categories     = categories, 
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('shoppinglist_new.html', csrfContext)
