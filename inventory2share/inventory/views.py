import logging
import collections
import settings

from django.utils import simplejson
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
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from inventory.util.transfer_objects import ShoppingListEntryTO
from inventory.inv.models import ShoppingList, ShoppingListEntry

logger = logging.getLogger(__name__)

#Helper functions

class ParameterExtractor:
    def get_inventory_params(self, request, form):
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
    
    def get_shoppinglist_params(self, request):
        DEFAULT_QUANTITY = 1
        json_data = simplejson.loads(request.raw_post_data)
        entries = []
        for ii in json_data["items"]:
            category_id, item_id = ii.split("_")
            to = ShoppingListEntryTO()
            to.item_id, to.qty = item_id, DEFAULT_QUANTITY
            entries.append(to)
        return entries

class DataPreprocessor:
    def build_categories(self, items):
        """Fetch categories for display  
        in inventory creation page."""
        categories = collections.OrderedDict()
        for item in items:
            myitems = categories.get(item.category, [])
            myitems.append(item)
            categories[item.category] = myitems 
        return categories  
    def build_result_tree(self, entries):
        """Built result tree for a category 
        based display of InventoryItem result"""
        res = collections.OrderedDict()
        for entry in entries:
            print entry
            val = res.get(entry.item.category, [])
            val.append(entry)
            res[entry.item.category] = val
        return res

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

def inventory_pick(request):
    invs = Inventory.objects.all()
    initialData = dict(invs=invs)
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventory_pick.html', csrfContext)

def shoppinglist_pick(request):
    sls = ShoppingList.objects.all()
    initialData = dict(sls=sls)
    csrfContext = RequestContext(request, initialData)
    return render_to_response('shoppinglist_pick.html', csrfContext)

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

def home(request):
    csrfContext = RequestContext(request, {})
    return render_to_response('home.html', csrfContext)
