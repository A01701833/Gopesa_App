from django.urls import path
from gopesa_app import views
from django.conf.urls import url
#------------------------------------------ END OF IMPORTING LIBRARIES ------------------------------

# APPLICATION NAME

app_name = 'gopesa_app'

# URL PATTERNS FOR APPLICATION "GOPESA_APP"
urlpatterns =[
    path('',views.index,name='index'),
    
    path('properties/',views.properties,name='properties'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('properties/<int:id>/<slug:slug>',views.properties_detail, name="properties_detail")
]
#------------------------------------------ END OF URLS ------------------------------
