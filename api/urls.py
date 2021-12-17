from django.urls import path
from .views import approved_words
from .views import suggested_words

urlpatterns = [
    path('approvedwords/', approved_words.ApprovedWordsView.as_view(), name='index'),
    path('approvedwords/<int:id>/', approved_words.ApprovedWordView.as_view(), name='show'),
    path('suggestedwords/', suggested_words.SuggestedWordsView.as_view(), name='index'),
    path('suggestedwords/<int:id>/', suggested_words.SuggestedWordView.as_view(), name='show')
]