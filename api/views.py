from django.contrib.auth.models import User, auth
from rest_framework import filters
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Domaine, Ecole, Metier, Question
from .pagination import CustomPagination
from .serializers import (DomaineSerializer, EcoleSerializer, MetierSerializer,
                          QuestionSerializer)

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
    search_fields = ['name', 'qualite', 'salaire']
    filter_backends = (filters.SearchFilter,)
    serializer_class = MetierSerializer
    queryset = Metier.objects.all()


class QuestionViewSet(ModelViewSet):

    serializer_class = QuestionSerializer
    queryset = Question.objects.all()



@api_view(["POST"])
def login(request):
    username = request.data['username']
    password = request.data['password']
    user = auth.authenticate(username=username, password=password)
    if user:
        return Response({"status": "OK"})
    else:

        return Response({"status": "Tsuiiiiipppp"})


@api_view(["POST"])
def register(request):
    user = User(email=request.data["email"],
                password=request.data["password"], username=request.data["username"])
    user.save()
    return Response({"status": "OK"})
