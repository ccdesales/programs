class InvEntryTO:
    item = None
    is_exist = False
    is_reorder = False
    qty_exist = 0
    qty_reorder = 0
        
    def __str__(self):
        return "<item=%s, is_exist=%s, is_reorder=%s, qty_exist=%s, qty_reorder=%s>" % (self.item, self.is_exist, self.is_reorder, self.qty_exist, self.qty_reorder)
    
class ShoppingListEntryTO:
    item_id = None
    qty = 0
        
    def __str__(self):
        return "<item_id=%s, qty=%s>" % (self.item_id, self.qty)
    def __repr__(self):
        return "<item_id=%s, qty=%s>" % (self.item_id, self.qty)