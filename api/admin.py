from django.contrib import admin
from .models import Enseigne,Ecole,Domaine,Metier,Question,Reponse

# Register your models here.

admin.site.register(Ecole)
admin.site.register(Domaine)
admin.site.register(Enseigne)
admin.site.register(Metier)
admin.site.register(Question)
admin.site.register(Reponse)


