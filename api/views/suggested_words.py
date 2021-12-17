from rest_framework.views import APIView
from rest_framework.response import Response
from ..serializers.suggested_word import SuggestedWordSerializer
from rest_framework import status
from django.shortcuts import get_object_or_404
from ..models.suggested_word import SuggestedWord
# from django.views import View
# import json

# Words, Plural
class SuggestedWordsView(APIView):
    # POST request to suggest a new word
    # POST /suggestedwords
    def post(self, request):
        word = SuggestedWordSerializer(data=request.data)
        if word.is_valid():
             word.save()
             return Response(word.data, status=status.HTTP_201_CREATED)
        else:
            return Response(word.errors, status=status.HTTP_400_BAD_REQUEST)

    # GET request for all words
    # GET /words "INDEX"
    def get(self, request):
        words = SuggestedWord.objects.all()
        data = SuggestedWordSerializer(words, many=True).data
        return Response(data)

# Word, Singular
class SuggestedWordView(APIView):
    # GET request for a specific word by id
    # GET /words/:id "SHOW"
    def get(self, request, id):
        word = get_object_or_404(SuggestedWord, id=id)
        data = SuggestedWordSerializer(word).data
        return Response(data)

    # DELETE
    def delete(self, request, id):
        word = get_object_or_404(SuggestedWord, id=id)
        word.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    # UPDATE... PATCH
    def patch(self, request, id): 
        word = get_object_or_404(SuggestedWord, id=id)
        updated_word = SuggestedWordSerializer(word, data=request.data, partial=True)
        if updated_word.is_valid():
            updated_word.save()
            return Response(updated_word.data)
    
    # UPDATE... PUT
    def put(self, request, id): 
        word = get_object_or_404(SuggestedWord, id=id)
        updated_word = SuggestedWordSerializer(word, data=request.data)
        if updated_word.is_valid():
            updated_word.save()
            return Response(updated_word.data)
