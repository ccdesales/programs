import collections

from django.utils import simplejson

from models import (
    InventoryEntry, 
    Inventory,
) 
from inventory.inv.models import (
    ShoppingList, 
    ShoppingListEntry,
)

from inventory.util.transfer_objects import (
    ShoppingListEntryTO, 
    InvEntryTO,
)

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

class InventoryProcessor:
    def add_inventory(self, name, items, ttype):
        inv = Inventory.objects.create(name=name, ttype=ttype)
        for item, to in items.items():
            kwargs = dict(
                        item                = item, 
                        inventory           = inv,
                        isexist             = to.is_exist,
                        isreorder           = to.is_reorder,
            )
            if to.qty_exist: 
                kwargs['exist_quantity'] = to.qty_exist        
            if to.qty_reorder: 
                kwargs['reorder_quantity'] = to.qty_reorder
            entry = InventoryEntry(**kwargs)
            entry.save()
        return inv.id
    
    def add_shopping_list(self, entries, name='Default'):
        sl = ShoppingList.objects.create(name=name)
        for to in entries:
            entry = ShoppingListEntry(item_id=to.item_id, quantity=to.qty, shopping_list=sl)
            entry.save()
        return sl.id
    
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
