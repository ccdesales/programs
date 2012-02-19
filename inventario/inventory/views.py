import sys
import datetime
import sqlite3
import logging
import collections
import settings

from django.template import RequestContext
from django.shortcuts import render_to_response

from util.customforms import InventoryForm
from util.transfer_objects import InvEntryTO

from inv.util import InventoryProcessor
from inv.models import (
    Item, 
    Inventory, 
    InventoryEntry, 
    InventoryType,
)

logger = logging.getLogger(__name__)

#Helper functions

def _get_inventory_params(request, form):
    """Extract data from form. Some bits come already validated
    by Django, but other must be validated as the display of them
    is highly customised"""
    name  = form.cleaned_data['name']
    ttype = form.cleaned_data['ttype']
    items = form.cleaned_data['items']
    
    ditems = dict()
    for item in items:
        to = InvEntryTO()
        to.item = item
        to.is_exist     = request.POST.get("isexist_%s"     % item.id, False)
        to.is_reorder   = request.POST.get("isreorder_%s"   % item.id, False)
        to.qty_exist    = request.POST.get("qty_exist_%s"   % item.id)
        to.qty_reorder  = request.POST.get("qty_reorder_%s" % item.id)
        ditems[item] = to

    return name, ditems, ttype

def _build_categories(items):
    """Fetch categories for display  
    in inventory creation page."""
    categories = collections.OrderedDict()
    for item in items:
        myitems = categories.get(item.category, [])
        myitems.append(item)
        categories[item.category] = myitems 
    return categories  

def inventario_view(request, inv_id):
    inv_id = int(inv_id)
    inv = Inventory.objects.get(pk=inv_id)
    
    entries = InventoryEntry.objects.filter(inventory=inv_id) # Alternative: (inventory=inv)
        
    initialData = dict(
        inv    = inv,
        view = inv.ttype.name,
        entries    = entries
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventario_view.html', csrfContext)

def inventario_pick(request):
    invs = Inventory.objects.all()
    initialData = dict(invs=invs)
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventario_pick.html', csrfContext)

def inventario(request):    
    if request.method == 'POST': # If the form has been submitted...
        form = InventoryForm(request.POST) # A form bound to the POST data
        if form.is_valid():
            proc  = InventoryProcessor()
            name, ditems, ttype = _get_inventory_params(request, form)
            proc.add(name, ditems, ttype)
            csrfContext = RequestContext(request, {})
            return render_to_response('added_inventario.html', csrfContext)
    else:
        form = InventoryForm() # An unbound form
    
    items           = Item.objects.all().order_by('category')
    categories      = _build_categories(items)
    
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
    return render_to_response('inventario.html', csrfContext)

def home(request):
    csrfContext = RequestContext(request, {})
    return render_to_response('home.html', csrfContext)
