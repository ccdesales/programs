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
from inventory.views import ParameterExtractor
from inventory.inv.util import InventoryProcessor, DataPreprocessor
from django.http import HttpResponse
from django.utils import simplejson
from django.views.decorators.csrf import csrf_exempt
from inventory.inv.models import ShoppingList, ShoppingListEntry

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

def shoppinglist_view(request, sl_id):
    sl_id = int(sl_id)
    shoppinglist = ShoppingList.objects.get(pk=sl_id)    
    entries = ShoppingListEntry.objects.filter(shopping_list=sl_id) # Alternative: (inventory=inv)
    results = DataPreprocessor().build_result_tree(entries)
        
    #items           = Item.objects.all().order_by('category')
    #categories      = _build_categories(items)
    
    initialData = dict(
        sl      = shoppinglist,
        entries = entries,
        results = results,
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('shoppinglist_view.html', csrfContext)


def shoppinglist_pick(request):
    sls = ShoppingList.objects.all()
    initialData = dict(sls=sls)
    csrfContext = RequestContext(request, initialData)
    return render_to_response('shoppinglist_pick.html', csrfContext)

@csrf_exempt
def shoppinglist_add(request):
    if request.is_ajax():
        entries = ParameterExtractor().get_shoppinglist_params(request)
        proc  = InventoryProcessor()
        sl_id = proc.add_shopping_list(entries)
        to_json = {
            "shopping_list": sl_id,        
        }
    return HttpResponse(simplejson.dumps(to_json), mimetype='application/json')

def shoppinglist(request):
    items           = Item.objects.all().order_by('category')
    categories      = _build_categories(items)

    initialData = dict(
        items          = items, 
        categories     = categories, 
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('shoppinglist_new.html', csrfContext)
