from rest_framework import serializers

from .models import Game, Rating

class GameSerializer(serializers.ModelSerializer):


    class Meta:
        model = Game
        fields = '__all__'


class RatingSerializer(serializers.ModelSerializer):

    def validate_rating(self, rating):
        if  0 > rating > 5:
            raise serializers.ValidationError('rating must be beetween 0 and 5')
        return rating

    def create(self, validated_data):
        requests = self.context.get('request')
        user = requests.user
        resume = Rating.objects.create(name=user, **validated_data)
        return resume

    class Meta:
        model = Rating
        fields = '__all__'