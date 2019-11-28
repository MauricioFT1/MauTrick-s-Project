from django.db import transaction
from rest_framework import serializers
from app.models import (Championship, Edition, EditionChampionship, Team, People, Noticia, Brazilian)

class EditionChampionshipSerializer(serializers.HyperlinkedModelSerializer):
    edition = serializers.ReadOnlyField(source="edition.id")
    championship = serializers.ReadOnlyField(source="championship.id")

    class Meta:
        model = EditionChampionship
        fields = ('id', 'championship', 'edition')


class ChampionshipSerializer(serializers.ModelSerializer):
    # authors = BookAuthorSerializer(source='bookauthor_set', many=True)
    
    class Meta:
        model = Championship
        fields = (
            'id', 'name', 'description', 'created', 'role'
        )
    
    # @transaction.atomic
    # def create(self, validated_data):
    #     championship = Championship.objects.create(**validated_data)
    #     if "editions" in self.initial_data:
    #         editions = self.initial_data.get("editions")
    #         for edition in editions:
    #             edition_id = edition.get("edition")
    #             role = author.get("role")
    #             author_instance = Author.objects.get(pk=author_id)
    #             EditionChampionship( ).save()
    #     book.save()
    #     return book

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ('id', 'name', 'stadium', 'coach', 'foundation')


class EditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Edition
        fields = ('id', 'date', 'participants', 'number')


class PeopleSerializer(serializers.ModelSerializer):
    class Meta:
        model = People
        fields = ('id', 'name', 'birth')

class NoticiaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Noticia
        fields = ('id','title', 'link', 'summary', 'image')

class BrazilianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brazilian
        fields = ('name', 'score', 'games', 'wins', 'draws', 'loses')
