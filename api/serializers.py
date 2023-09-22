
from .models import Enseigne,Ecole,Domaine,Metier,Question,Reponse
from rest_framework import serializers

class EcoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ecole
        fields = '__all__'


class EnseigneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enseigne
        fields = '__all__'


class DomaineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Domaine
        fields = '__all__'


class MetierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Metier
        fields = '__all__'


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = '__all__'


class ReponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reponse
        fields = '__all__'

