from rest_framework.viewsets import ModelViewSet

from .models import Domaine, Ecole, Enseigne, Metier, Question, Reponse
from .serializers import (DomaineSerializer, EcoleSerializer,
                          EnseigneSerializer, MetierSerializer,
                          QuestionSerializer, ReponseSerializer)


class EnseigneViewSet(ModelViewSet):

    serializer_class = EnseigneSerializer
    queryset = Enseigne.objects.all()


class EcoleViewSet(ModelViewSet):

    serializer_class = EcoleSerializer
    queryset = Ecole.objects.all()


class DomaineViewSet(ModelViewSet):

    serializer_class = DomaineSerializer
    queryset = Domaine.objects.all()


class MetierViewSet(ModelViewSet):

    serializer_class = MetierSerializer
    queryset = Metier.objects.all()


class QuestionViewSet(ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ReponseViewSet(ModelViewSet):

    serializer_class = ReponseSerializer
    queryset = Reponse.objects.all()
