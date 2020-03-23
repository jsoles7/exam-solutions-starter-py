
from solutions.social import question_a, tweets

def test_question_a():
    result = question_a(tweets)
    assert result == "sandwhoa"