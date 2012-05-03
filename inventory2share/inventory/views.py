import logging
import collections
import settings

from django.template import RequestContext
from django.shortcuts import render_to_response

from util.customforms import InventoryForm
from inv.util import InventoryProcessor
from inv.models import (
    Item, 
    Inventory, 
    InventoryEntry, 
    InventoryType,
)
from inventory.inv.util import ParameterExtractor

logger = logging.getLogger(__name__)

#Helper functions



def home(request):
    csrfContext = RequestContext(request, {})
    return render_to_response('home.html', csrfContext)
