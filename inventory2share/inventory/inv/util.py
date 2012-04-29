from models import InventoryEntry, Inventory 
from inventory.inv.models import ShoppingList, ShoppingListEntry

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