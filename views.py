# Q5: add these imports (if missing) at the TOP of onlinecourse/views.py
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Course, Enrollment, Question, Choice, Submission


# Then add these functions at the BOTTOM of onlinecourse/views.py

def extract_answers(request):
    """Collect the ids of every checked choice from the exam form."""
    submitted_answers = []
    for key in request.POST:
        if key.startswith('choice'):
            choice_id = int(request.POST[key])
            submitted_answers.append(choice_id)
    return submitted_answers


def submit(request, course_id):
    """Create a Submission for the user's enrollment and store the selected choices."""
    course = get_object_or_404(Course, pk=course_id)
    user = request.user
    enrollment = get_object_or_404(Enrollment, user=user, course=course)

    submission = Submission.objects.create(enrollment=enrollment)
    selected_choice_ids = extract_answers(request)
    submission.choices.set(selected_choice_ids)

    return HttpResponseRedirect(
        reverse(
            viewname='onlinecourse:show_exam_result',
            args=(course.id, submission.id),
        )
    )


def show_exam_result(request, course_id, submission_id):
    """Calculate the total score for a submission and show the result page."""
    course = get_object_or_404(Course, pk=course_id)
    submission = get_object_or_404(Submission, pk=submission_id)
    selected_choices = submission.choices.all()

    total_score = 0
    max_score = 0
    for question in course.question_set.all():
        max_score += question.grade
        selected_ids_for_question = submission.choices.filter(
            question=question
        ).values_list('id', flat=True)
        if question.is_get_score(selected_ids_for_question):
            total_score += question.grade

    percent = round((total_score / max_score) * 100) if max_score else 0

    context = {
        'course': course,
        'submission': submission,
        'choices': selected_choices,
        'grade': total_score,
        'max_score': max_score,
        'percent': percent,
        'passed': percent >= 80,
    }
    return render(request, 'onlinecourse/exam_result_bootstrap.html', context)
