from django.db import transaction
from rest_framework import serializers
from app.models import (Championship, Edition, EditionChampionship, Team, People)


# class BookAuthorSerializer(serializers.HyperlinkedModelSerializer):
#     id = serializers.ReadOnlyField(source="author.id")
#     name = serializers.ReadOnlyField(source="author.name")

#     class Meta:
#         model = BookAuthor

#         fields = ('id', 'name', 'role')


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
