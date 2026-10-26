# Add these three models to the BOTTOM of onlinecourse/models.py
# (after Course, Lesson, Instructor, Learner and Enrollment).
# models is already imported at the top of that file: from django.db import models


class Question(models.Model):
    # Each question belongs to one course
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.CharField(max_length=500)
    # Points awarded for answering this question correctly
    grade = models.IntegerField(default=1)

    def __str__(self):
        return "Question: " + self.question_text

    # Returns True only if the selected choices are exactly the correct ones
    def is_get_score(self, selected_ids):
        correct_ids = set(
            self.choice_set.filter(is_correct=True).values_list("id", flat=True)
        )
        return correct_ids == set(int(i) for i in selected_ids)


class Choice(models.Model):
    # Each choice belongs to one question
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=500)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return self.choice_text


class Submission(models.Model):
    # A submission belongs to one enrollment and holds the selected choices
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)

    def __str__(self):
        return "Submission #" + str(self.id)
