from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.db.models import Q
from django.urls import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.loader import render_to_string
from .models import Propiedades , Images



# Create your views here.

# MANTEINANCE VIEW



# INDEX VIEW ( LANDING PAGE )
def index(request):
    return render(request,"gopesa_app/index.html")
"""
def properties(request):

    return render(request,"principal/properties.html")
"""

#  ABOUT PAGE
def about(request):
    return render(request,"gopesa_app/about.html")

#  CONTACT  PAGE
def contact(request):
    return render(request,"gopesa_app/contact.html")

def manteinance(request):
    return render(request,"gopesa_app/manteinance.html")
#  PROPERTIES PAGE ( DISPLAYS LISTS OF PROPERTIES AVAILABLE.)
def properties(request):
    properties_list = Propiedades.activo.all()
    paginator = Paginator(properties_list, 5) # PAGINATION FOR BETTER RESULTS.
    page = request.GET.get('page')
    # VALIDATIONS FOR INCORRECT URLS
    try:
        propiedad = paginator.page(page)
    except PageNotAnInteger:
        propiedad = paginator.page(1)
    except EmptyPage:
        propiedad = paginator.page(paginator.num_pages)

        # INDEX LIMITATION RESULTS
    if page is None:
        start_index = 0
        end_index = 7
    else:
        (start_index, end_index) = proper_pagination(propiedad, index=4)

    page_range = list(paginator.page_range)[start_index:end_index]

    context = {
        'propiedad': propiedad,
        'page_range': page_range,
    }
    return render(request,"gopesa_app/properties.html",context)

# AS THE NAME SAYS, PROPER PAGINATION.
def proper_pagination(propiedad, index):
    start_index = 0
    end_index = 7
    if propiedad.number > index:
        start_index = propiedad.number - index
        end_index = start_index + end_index
    return (start_index, end_index)


# DETAILED VIEW OF AN SPECIFIC PROPERTY, CHARACTERISTICS AND MORE.
def properties_detail(request,id,slug):
    post = get_object_or_404(Propiedades,id=id,slug=slug)
    context={
        'post':post,
    }
    return render(request,'gopesa_app/agents.html',context)


#  -------------------------------- END OF PRINCIPAL:VIEWS ------------------------------
