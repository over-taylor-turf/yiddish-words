from django.db import models

class SuggestedWord(models.Model):
    email = models.CharField(max_length=255)
    word = models.CharField(max_length=255)
    phonetic_spelling = models.CharField(max_length=255)
    definition = models.CharField(max_length=255)
    example_sentence = models.CharField(max_length=255)
    bubbe = models.CharField(max_length=255)

    def __str__(self):
            return f"Proposed by {self.email}: {self.word} is pronounced as '{self.phonetic_spelling}' and means '{self.definition}'. An example sentence would be, '{self.example_sentence}' This word has been added in honor of Bubbe {self.bubbe}."