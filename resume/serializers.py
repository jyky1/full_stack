from rest_framework import serializers

from .models import Resume

class ResumeSerializer(serializers.ModelSerializer):
    # name = serializers.ReadOnlyField()
    # email = serializers.ReadOnlyField()
    # phone = serializers.ReadOnlyField()
    # city = serializers.ReadOnlyField()

    class Meta:
        model = Resume
        fields = '__all__'

    # def create(self, validated_data):
    #     requests = self.context.get('request')
    #     user = requests.user
    #     resume = Resume.objects.create(name=user, **validated_data)
    #     return resume
