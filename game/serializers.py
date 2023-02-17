from rest_framework import serializers
from django.db.models import Avg

from .models import Game, Rating

class GameSerializer(serializers.ModelSerializer):
    company = serializers.ReadOnlyField()


    class Meta:
        model = Game
        fields = '__all__'
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        print(representation)
        representation['ratings'] = instance.ratings.aggregate(Avg('rating'))['rating__avg']
        return representation



class RatingSerializer(serializers.ModelSerializer):

    def validate_rating(self, rating):
        if rating > 5:
            raise serializers.ValidationError('rating must be beetween 0 and 5')
        return rating

    def create(self, validated_data):
        rating = Rating.objects.create( **validated_data)
        return rating

    class Meta:
        model = Rating
        fields = '__all__'