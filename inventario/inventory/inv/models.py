from django.db import models

class Unit(models.Model):
	name = models.CharField(max_length=50)
	plural_name = models.CharField(max_length=50)
	
	def __str__(self):
		return self.name
	
class Category(models.Model):
	name = models.CharField(max_length=50)
		
	def __str__(self):
		return self.name
	
class Item(models.Model):
	category 	= models.ForeignKey(Category)
	unit 		= models.ForeignKey(Unit)
	name 		= models.CharField(max_length=50)
	reorder_limit = models.PositiveIntegerField(max_length=3, null=True, blank=True)
	
	def __str__(self):
		return self.name

class InventoryType(models.Model):
	name 	= models.CharField(max_length=20)

	def __str__(self):
		return self.name    

class Inventory(models.Model):
	name 	= models.CharField(max_length=30)	
	items 	= models.ManyToManyField(Item, through='InventoryEntry')
	ttype	= models.ForeignKey(InventoryType)
	
	def __str__(self):
		return self.name	
		
class InventoryEntry(models.Model):
	item 		= models.ForeignKey(Item)
	inventory 	= models.ForeignKey(Inventory)
	isexist		= models.BooleanField()
	isreorder	= models.BooleanField()
	
	exist_quantity 	 = models.PositiveIntegerField(max_length=3, null=True, blank=True)
	reorder_quantity = models.PositiveIntegerField(max_length=3, null=True, blank=True)  
	
	def __str__(self):
		return "%s %s de %s" % (self.quantity, self.item.unit, self.item.name)
