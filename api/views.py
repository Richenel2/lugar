from django.contrib.auth.models import User, auth
from django.shortcuts import get_object_or_404
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
def corrige(request):
    data = request.data
    school = {}
    met = {}
    for rep in data:
        question = get_object_or_404(Question, pk=rep['id'])
        schoolSet = set()
        metierSet = set()
        for domaine in question.domaines.all():
            ecoles = Ecole.objects.filter(departments=domaine)
            metiers = Metier.objects.filter(departments=domaine)
            for ecole in ecoles:
                schoolSet.add(ecole.id)
            for metier in metiers:
                metierSet.add(metier.id)
        point = (rep["reponse"] - 3)*10
        for sch in schoolSet:
            try:
                school[sch] += point
            except KeyError:
                school[sch] = point
        for sch in metierSet:
            try:
                met[sch] += point
            except KeyError:
                met[sch] = point
        school = dict(sorted(school.items(), key=lambda item: item[1]))
        met = dict(sorted(met.items(), key=lambda item: item[1]))
        school = school.keys()[:3]
        met = met.keys()[:3]
    return Response(list(map(lambda x: EcoleSerializer(get_object_or_404(Ecole, pk=x)).data, school))


@api_view(["POST"])
def register(request):
    user = User(email=request.data["email"],
                password=request.data["password"], username=request.data["username"])
    user.save()
    return Response({"status": "OK"})
