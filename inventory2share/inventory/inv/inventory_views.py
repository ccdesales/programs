'''
Created on Jan 30, 2012

@author: desales
'''

from django.template.context import RequestContext
from django.shortcuts import render_to_response
from django.conf import settings

from inventory.inv.models import ( 
    Inventory, 
    InventoryEntry, 
    Item, 
    InventoryType,
)

from inventory.util.customforms import InventoryForm

from inventory.inv.util import (
    InventoryProcessor, 
    ParameterExtractor,
    DataPreprocessor,
)

def inventory_view(request, inv_id):
    inv_id = int(inv_id)
    inv = Inventory.objects.get(pk=inv_id)    
    entries = InventoryEntry.objects.filter(inventory=inv_id) # Alternative: (inventory=inv)
    results = DataPreprocessor().build_result_tree(entries)
        
    #items           = Item.objects.all().order_by('category')
    #categories      = _build_categories(items)
    
    initialData = dict(
        inv     = inv,
        view    = inv.ttype.name,
        entries = entries,
        results = results,
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventory_view.html', csrfContext)

def inventory_pick(request):
    invs = Inventory.objects.all()
    initialData = dict(invs=invs)
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventory_pick.html', csrfContext)


def inventory(request):    
    if request.method == 'POST': # If the form has been submitted...
        form = InventoryForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            proc  = InventoryProcessor()
            name, ditems, ttype = ParameterExtractor().get_inventory_params(request, form)
            data = dict(
                name = name, 
                items = ditems, 
                ttype = ttype,
            )
            inv_id = proc.add_inventory(name, ditems, ttype)
            return inventory_view(request, inv_id)
    else:
        form = InventoryForm() # An unbound form
    
    items           = Item.objects.all().order_by('category')
    categories      = DataPreprocessor().build_categories(items)    
    simple_ttype    = InventoryType.objects.get(id=settings.SIMPLE_INVENTORY_ID)
    detailed_ttype  = InventoryType.objects.get(id=settings.DETAILED_INVENTORY_ID)

    initialData = dict(
                    items          = items, 
                    form           = form,
                    categories     = categories, 
                    simple_ttype   = simple_ttype,
                    detailed_ttype = detailed_ttype,
                )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventory.html', csrfContext)
