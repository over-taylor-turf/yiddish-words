from django.contrib import admin
from .models.approved_word import ApprovedWord
from .models.suggested_word import SuggestedWord
  
# Register your models here.
admin.site.register(ApprovedWord)
admin.site.register(SuggestedWord)