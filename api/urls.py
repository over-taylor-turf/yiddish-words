from django.urls import path
from .views import approved_words

urlpatterns = [
    path('words/', approved_words.ApprovedWordsView.as_view(), name='index'),
    path('words/<int:id>/', approved_words.ApprovedWordView.as_view(), name='show')
]