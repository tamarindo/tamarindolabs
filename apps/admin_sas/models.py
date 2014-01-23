from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from django.conf import settings


GENDER_CHOICES = (
    ('M', _('Masculino')),
    ('F', _('Femenino')),
    ('N', _('No definido')),
)

class GenericManager(models.Manager):

    def get_all_active(self):
        return self.filter(is_active=True).order_by('-date_modified')

    def get_or_none(self, **kwargs):
        try:
            return self.get(**kwargs)
        except self.model.DoesNotExist:
            return None
        except self.model.MultipleObjectsReturned:
            return None

class Service(models.Model):
    """Extended profile to Django User model"""
    nombre = models.CharField(max_length=30, verbose_name=_("nombre"))
    precio = models.IntegerField(max_length=20,verbose_name=_("Precio"))   
    description = models.CharField(max_length=900,null=True,blank=True,verbose_name=_("descripcion"))
  	# Requerimientos
    type_service =	models.CharField(max_length=250,verbose_name=_("Valor"))
    time_license  = models.IntegerField(max_length=20,verbose_name=_("tiempo licencia")) 
    developed_by = models.CharField(max_length=250,null=True,blank=True,verbose_name=_("descripcion"))
    # ------ datos para todas las tablas
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    
    objects = GenericManager()

    def __unicode__(self):
        return self.short_name


class Company(models.Model):
    """Extended profile to Django User model"""
    
    Nit = models.CharField(max_length=30, null=False, verbose_name=_("NIT"))
    legal_forma = models.CharField(max_length=30, verbose_name=_("Rorma Legal"), null=True, blank=True)
    razon = models.CharField(max_length=30, verbose_name=_("Razon"), null=True, blank=True)
    ambito = models.CharField(max_length=30, verbose_name=_("Ambito"), null=True, blank=True)
    phone1 = models.CharField(max_length=30, verbose_name=_("Telefono 1"), null=True, blank=True)
    phone2 = models.CharField(max_length=30, verbose_name=_("Telefono 2"), null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name=_("Direccion"), null=True, blank=True)    
    city = models.CharField(max_length=60, verbose_name=_("Ciudad"), null=True, blank=True)
    state = models.CharField(max_length=60, verbose_name=_("Estado"), null=True, blank=True)        
    country = models.CharField(max_length=60, verbose_name=_("Pais"), null=True, blank=True)
    commercial_activity = models.CharField(max_length=60, verbose_name=_("Pais"), null=True, blank=True)     
    logo = models.FileField(upload_to=settings.MEDIA_ROOT + "/logos", max_length=400, null=True, blank=True)

    service =  models.OneToOneField(Service, verbose_name=_("Service"))
    # ------ datos para todas las tablas
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = GenericManager()

    def __unicode__(self):
        return self.short_name

class DniType(models.Model):
    """List of DNI types"""
    short_name = models.CharField(max_length=40, verbose_name=_("Nombre corto"))
    long_name = models.CharField(max_length=300, verbose_name=_("Nombre Largo"))
    # ------ datos para todas las tablas

    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = GenericManager()

    def __unicode__(self):
        return self.short_name




class UserProfile(models.Model):
    """Extended profile to Django User model"""
    user = models.OneToOneField(User, verbose_name=_("Usuario"))
    admin_user = models.BooleanField(default=False)
    dni_type = models.ForeignKey(DniType)
    dni = models.CharField(max_length=30, null=False, verbose_name=_("DNI"))
    phone1 = models.CharField(max_length=30, verbose_name=_("Telefono 1"), null=True, blank=True)
    phone2 = models.CharField(max_length=30, verbose_name=_("Telefono 2"), null=True, blank=True)
    address = models.CharField(max_length=150, verbose_name=_("Direccion"), null=True, blank=True)
    city = models.CharField(max_length=60, verbose_name=_("ciudad"), null=True, blank=True)
    state = models.CharField(max_length=60, verbose_name=_("estado"), null=True, blank=True)        
    country = models.CharField(max_length=60, verbose_name=_("pais"), null=True, blank=True)    
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name=_("Genero"), null=True, blank=True)
    date_born = models.DateField(null=True, verbose_name=_("Fecha de nacimiento"), blank=True)
    # ------ datos para todas las tablas
    is_active = models.BooleanField(default=True)
    date_added = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
    objects = GenericManager()

    def __unicode__(self):
        return self.short_name



