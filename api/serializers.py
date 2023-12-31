
from .models import Ecole,Domaine,Metier,Question
from rest_framework import serializers

class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = '__all__'

class EcoleSerializer(serializers.ModelSerializer):

    departments = DomaineSerializer(read_only=True, many=True)
    class Meta:
        model = Ecole
        fields = '__all__'


# class EnseigneSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Enseigne
#         fields = '__all__'



class MetierSerializer(serializers.ModelSerializer):

    departments = DomaineSerializer(read_only=True, many=True)
    class Meta:
        model = Metier
        fields = '__all__'


# class ReponseSerializer(serializers.ModelSerializer):

#     domaines = DomaineSerializer(read_only=True, many=True)
#     class Meta:
#         model = Reponse
#         fields = '__all__'

class QuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Question
        fields = ("question","id")



