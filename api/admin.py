from django.contrib import admin
from .models import Ecole,Domaine,Metier,Question,Reponse

# Register your models here.

admin.site.register(Ecole)
admin.site.register(Domaine)
admin.site.register(Metier)
admin.site.register(Question)
admin.site.register(Reponse)


