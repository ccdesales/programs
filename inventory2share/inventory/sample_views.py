import sys

from django.template import RequestContext
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render_to_response
from django.http import HttpResponse
from util.customforms import InventoryForm, ContactForm
import MySQLdb
import datetime
import sqlite3
import logging

from inv.models import Item, Inventory, InventoryEntry

logger = logging.getLogger(__name__)

from django.forms import ( 
	ModelForm,
	Select, 
	Textarea,
	RadioSelect,
	SelectMultiple, 
	ModelMultipleChoiceField, 
	CheckboxSelectMultiple
)
	

class InvForm(ModelForm):
	class Meta:
		model = Inventory
		fields = ('name', 'items')
		widgets = {
			#'items': Select(),
			#'items': RadioSelect(),
			#'items': SelectMultiple(),
            #'items': Textarea(attrs={'cols': 80, 'rows': 20}),
            'items': CheckboxSelectMultiple(),
        }

class ItemForm(ModelForm):
	class Meta:
		model = Item
				
class InvEntryForm(ModelForm):
	class Meta:
		model = InventoryEntry

def inventario(request):
	items = Item.objects.all()	
	now = datetime.datetime.now()
	
	#form = ContactForm()
	#form = ContactForm(request.POST)
	#form = InventoryForm(request.POST)
	
	#form = InvForm(request.POST)
	form = InvForm()
	itemsForm = ItemForm()
	entryform = InvEntryForm()
	
	initialData = dict(current_date=now, items=items, form=form, entryform=entryform, itemsForm=itemsForm)
	csrfContext = RequestContext(request, initialData)
	return render_to_response('inventario.html', csrfContext)


def add_inventario(request):
	items = Item.objects.all()
	return render_to_response('added_inventario.html', {'items': items})

def home(request):
	conn = sqlite3.connect('/home/desales/PROGRAMS/inventario/inventory/db.db3')
	c = conn.cursor()
	c.execute('select * from inv_item')
	for row in c:
		print >>sys.stderr, row

	now = datetime.datetime.now()
	#return render_to_response('current_datetime.html', {'current_date': now})
	return render_to_response('home.html', {'current_date': now})


def inventario1(request):
	items = Item.objects.all()
	
	#form = ContactForm()
	#form = ContactForm(request.POST)
	form = InventoryForm(request.POST)
	
	if form.is_valid():
		message = form.cleaned_data
		print >>sys.stderr,  message
	
	print >>sys.stderr,  "-------------------------------------------------------------------"
	print >>sys.stderr, form.as_p()
	
	initialData = dict(items=items, form=form)
	csrfContext = RequestContext(request, initialData)
	return render_to_response('inventario.html', csrfContext)
	
def inventario2(request):
	items = Item.objects.all()	
	now = datetime.datetime.now()
	
	#form = ContactForm()
	#form = ContactForm(request.POST)
	#form = InventoryForm(request.POST)
	
	form = InvForm(request.POST)
	
	initialData = dict(current_date=now, items=items, form=form)
	csrfContext = RequestContext(request, initialData)
	return render_to_response('inventario.html', csrfContext)

def get_time(request):
	now = datetime.datetime.now()
	html = "<html><body>It is now %s.</body></html>" % now
	return HttpResponse(html)

def use_sqlite(request):
	conn = sqlite3.connect('/home/desales/PROGRAMS/inventario/inventory/db.db3')
	c = conn.cursor()
	c.execute('select * from inv_item')
	for row in c:
		print >>sys.stderr, row

	now = datetime.datetime.now()
	#return render_to_response('current_datetime.html', {'current_date': now})
	return render_to_response('home.html', {'current_date': now})

def current_datetime3(request):
	now = datetime.datetime.now()
	t = get_template('current_datetime.html')
	html = t.render(Context({'current_date': now}))
	return HttpResponse(html)
	
def current_datetime4(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})
	
def book_list(request):
	db = MySQLdb.connect(user='root', db='pizza_shop', passwd='tutibm44', host='localhost')
	cursor = db.cursor()
	cursor.execute('select * from PERSON')
	names = [row[1] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html', {'names': names})

def use_mysql(request):
	#url(r'^inventario/json_test.json/$', json_test),
	db = MySQLdb.connect(user='root', db='pizza_shop', passwd='tutibm44', host='localhost')
	cursor = db.cursor()
	cursor.execute('select * from PERSON')
	names = [row[1] for row in cursor.fetchall()]
	db.close()
	return render_to_response('book_list.html', {'names': names})

def json_test(request):
    initialData = dict()
    csrfContext = RequestContext(request, initialData)
    return render_to_response('test.json', csrfContext)

def home(request):
    conn = sqlite3.connect(settings.DB_NAME)
    c = conn.cursor()
    c.execute('select * from inv_item')
    for row in c:
        print >>sys.stderr, row

    now = datetime.datetime.now()
    csrfContext = RequestContext(request, {'current_date': now})
    return render_to_response('home.html', csrfContext)

def inventario_view(request, inv_id):
    inv_id = int(inv_id)
    inv = Inventory.objects.get(pk=inv_id)
    
    entries = InventoryEntry.objects.filter(inventory=inv_id) # Alternative: (inventory=inv)     
    print >>sys.stderr, entries.query #display SQL
        
    initialData = dict(
        inv    = inv,
        view = inv.ttype.name,
        entries    = entries
    )
    csrfContext = RequestContext(request, initialData)
    return render_to_response('inventario_view.html', csrfContext)