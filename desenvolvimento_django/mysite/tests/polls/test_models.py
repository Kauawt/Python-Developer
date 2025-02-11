import pytest
from polls.models import Question
from django.utils import timezone

@pytest.mark.django_db

def test_question_create():
    # Given
    question_text = "Qual é sua linguagem"
    pub_date = timezone.now()
    active = True

    # When
    question = Question.objects.create(question_text=question_text, pub_date = pub_date, active=active)

    #Then
    assert 1 == 1
