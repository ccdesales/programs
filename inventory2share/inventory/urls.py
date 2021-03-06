from django.conf.urls.defaults import patterns, include, url
from inventory.inv.models import Item, Unit, Category, Inventory, InventoryEntry, InventoryType

from inventory.views import home
from inventory.inv.inventory_views import (
    inventory,
    inventory_view,
    inventory_pick,
)
from inventory.inv.shopping_list_views import (
    shoppinglist,
    shoppinglist_add,
    shoppinglist_pick,
    shoppinglist_view,
)

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

admin.site.register(Item)
admin.site.register(Unit)
admin.site.register(Category)
admin.site.register(Inventory)
admin.site.register(InventoryEntry)
admin.site.register(InventoryType)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'inventory.views.home', name='home'),
    # url(r'^inventory/', include('inventory.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

    url(r'^inv/$', home),
    url(r'^inventory/$', inventory),
    url(r'^shoppinglist/$', shoppinglist),
    url(r'^inventory/view/$', inventory_pick),
    url(r'^shoppinglist/view/$', shoppinglist_pick),
    
    url(r'^inventory/view/(\d+)/$', inventory_view),
    url(r'^shoppinglist/view/(\d+)/$', shoppinglist_view),
    
    url(r'^shoppinglist/add/$', shoppinglist_add),
)
