from rest_framework.viewsets import ModelViewSet
from rest_framework import filters
from django.http import Http404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from .models import Domaine, Ecole, Metier, Question, Reponse
from .pagination import CustomPagination
from .serializers import (DomaineSerializer, EcoleSerializer,
                           MetierSerializer,
                          QuestionSerializer, ReponseSerializer)


# class EnseigneViewSet(ModelViewSet):

#     serializer_class = EnseigneSerializer
#     queryset = Enseigne.objects.all()


class EcoleViewSet(ModelViewSet):

    pagination_class = CustomPagination
    search_fields = ['nom',]
    filter_backends = (filters.SearchFilter,)
    serializer_class = EcoleSerializer
    queryset = Ecole.objects.all()

    # def retrieve(self, request, pk=None):
    #     queryset = Ecole.objects.all()
    #     user = get_object_or_404(queryset, pk=pk)
    #     serializer = EcoleSerializer(user)
    #     enseigne = get_list_or_404(Enseigne.objects.all(), ecole=pk)
    #     serializer.data["domaine"] = list(map(lambda x:EnseigneSerializer(x).data,enseigne))
    #     return Response(serializer.data)
    


class DomaineViewSet(ModelViewSet):

    serializer_class = DomaineSerializer
    queryset = Domaine.objects.all()


class MetierViewSet(ModelViewSet):
    pagination_class = CustomPagination
    search_fields = ['name','qualite','salaire']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MetierSerializer
    queryset = Metier.objects.all()


class QuestionViewSet(ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()


class ReponseViewSet(ModelViewSet):

    serializer_class = ReponseSerializer
    queryset = Reponse.objects.all()

@api_view(["POST"])
def login(request):
    user = get_object_or_404(User.objects.all(),username=request.data["username"])
    if user.check_password(request.data["password"]):
        return Response({"status":"OK"})
    else:
        raise Http404

@api_view(["POST"])
def register(request):
    user = User(email=request.data["email"],password=request.data["password"],username=request.data["username"])
    return Response({"status":"OK"})