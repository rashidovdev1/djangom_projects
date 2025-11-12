from django.shortcuts import render, get_object_or_404
from lessons.models import Lesson
from .models import Question

def quiz_view(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    questions = lesson.questions.all()
    return render(request, 'quizzes/quiz.html', {'lesson': lesson, 'questions': questions})
