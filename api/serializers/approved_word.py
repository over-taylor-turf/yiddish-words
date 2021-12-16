from rest_framework import serializers
from ..models.approved_word import ApprovedWord

class ApprovedWordSerializer(serializers.ModelSerializer):
    class Meta:
         # Specify the model from which to define the fields
        model = ApprovedWord
        # Define fields to be returned
        fields = '__all__'