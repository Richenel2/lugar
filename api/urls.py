from django.urls import include, path
from rest_framework.routers import DefaultRouter

from api.views import (DomaineViewSet, EcoleViewSet,
                       MetierViewSet, QuestionViewSet, ReponseViewSet)

router = DefaultRouter()
router.register(r'ecole', EcoleViewSet, basename='ecole')
# router.register(r'enseigne', EnseigneViewSet, basename='enseigne')
router.register(r'reponse', ReponseViewSet, basename='reponse')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'domaine', DomaineViewSet, basename='domaine')
router.register(r'metier', MetierViewSet, basename='metier')

urlpatterns = [
    path(r'', include(router.urls)),
]
