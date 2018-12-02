from __future__ import unicode_literals
from django.db import models
from django.urls import reverse

# Create your models here.


# MANAGER FOR ACTIVE PROPERTIES
class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status="activo")

# TABLE PROPIEDADES

class Propiedades(models.Model):
    objects = models.Manager()      #Our default Manager
    activo = PublishedManager()

    STATUS_CHOICES = (                  # STATUS  CHOICES FOR PROPERTY AVAILABILITY
        ('activo','Activo'),
        ('inactivo','Inactivo'),
    )
    TYPE_CHOICES = (                # TYPE CHOICES FOR PROPERTIES ( EX. IF A HOUSE IS ON SALE, THEN TYPE_CHOICES SHOULD BE SET TO "VENTA")
        ('venta','VENTA'),
        ('renta','RENTA'),

    )

    nombre = models.CharField(max_length=100)   # NAME OF PROPERTY
    slug = models.SlugField(max_length=120)     # SLUG OF PROPERTY ( SLUG  WILL BE USED FOR URL)
    descripcion = models.CharField(max_length=120) # DESCRIPTION
    ubicacion = models.CharField(max_length=100)    # PROPERTY LOCATION
    terreno = models.CharField(max_length=20)       # TOTAL AMOUNT OF M^2
    cuartos = models.CharField(max_length=20)   # ROOMS
    banos = models.CharField(max_length = 20)   # BATHROOMS
    precio = models.CharField(max_length=20)    # PRICE
    tipo = models.CharField(max_length=10, choices=TYPE_CHOICES, default='venta')  # TYPE, USING TYPE_CHOICES FOR DEFINING THE TYPE OF PROPERTY
    status =  models.CharField(max_length=10, choices=STATUS_CHOICES, default='activo') # STATUS OF THE PROPERTY ,SET TO ACTIVE BY DEFAULT, ENABLING A LOGICAL DELETION INSTEAD OF A PHYSICAL ONE.

    class Meta:
        ordering = ['-id']      #PROPERTY_LIST ORDERING, SET TO ID BY DEFAULT


    def __str__(self):
        return self.nombre              # /ADMIN DISPLAY NAME ON DATABASE.

    def get_absolute_url(self):
        return reverse("gopesa_app:properties_detail",args=[self.id,self.slug])   # URL CONSOLIDATION.

#-------------------------- END OF PROPERTY MODEL


# IMAGE MODEL

class Images(models.Model):
    post = models.ForeignKey(Propiedades,on_delete=models.PROTECT)
    image = models.ImageField(upload_to='images/',blank=True,null=True)

    def __str__(self):
        self.post.nombre + "Image"