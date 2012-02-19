from models import InventoryEntry, Inventory 

class InventoryProcessor:
    def add(self, name, items, ttype):
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