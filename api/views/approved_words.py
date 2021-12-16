from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.approved_word import ApprovedWordSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.approved_word import ApprovedWord
# from django.views import View
# import json

# Words, Plural
class ApprovedWordsView(APIView):
    # POST request to create a new word
    # POST /words
    def post(self, request):
        word = ApprovedWordSerializer(data=request.data)
        if word.is_valid():
             word.save()
             return Response(word.data, status=status.HTTP_201_CREATED)
        else:
            return Response(word.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all words
    # GET /words "INDEX"
    def get(self, request):
        words = ApprovedWord.objects.all()
        data = ApprovedWordSerializer(words, many=True).data
        return Response(data)

# Word, Singular
class ApprovedWordView(APIView):
    # GET request for a specific word by id
    # GET /words/:id "SHOW"
    def get(self, request, id):
        word = get_object_or_404(ApprovedWord, id=id)
        data = ApprovedWordSerializer(word).data
        return Response(data)

    # DELETE
    def delete(self, request, id):
        word = get_object_or_404(ApprovedWord, id=id)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE... PATCH
    def patch(self, request, id): 
        word = get_object_or_404(ApprovedWord, id=id)
        updated_word = ApprovedWordSerializer(word, data=request.data, partial=True)
        if updated_word.is_valid():
            updated_word.save()
            return Response(updated_word.data)
    
    # UPDATE... PUT
    def put(self, request, id): 
        word = get_object_or_404(ApprovedWord, id=id)
        updated_word = ApprovedWordSerializer(word, data=request.data)
        if updated_word.is_valid():
            updated_word.save()
            return Response(updated_word.data)
