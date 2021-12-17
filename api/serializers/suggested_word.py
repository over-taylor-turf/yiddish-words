from rest_framework import serializers
from ..models.suggested_word import SuggestedWord

class SuggestedWordSerializer(serializers.ModelSerializer):
    class Meta:
         # Specify the model from which to define the fields
        model = SuggestedWord
        # Define fields to be returned
        fields = '__all__'