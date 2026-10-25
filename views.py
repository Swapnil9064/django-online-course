from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404,redirect,render
from .models import Course,Submission
def course_list(request):
 return render(request,'onlinecourse/course_list.html',{'courses':Course.objects.all()})
def course_details(request,course_id):
 return render(request,'onlinecourse/course_details_bootstrap.html',{'course':get_object_or_404(Course,pk=course_id)})
@login_required
def submit(request,course_id):
 course=get_object_or_404(Course,pk=course_id)
 if request.method!='POST': return redirect('onlinecourse:course_details',course_id=course.id)
 questions=list(course.questions.prefetch_related('choices')); score=0
 for q in questions:
  selected=request.POST.get(f'question_{q.id}')
  if selected and q.choices.filter(id=selected,is_correct=True).exists(): score+=1
 sub=Submission.objects.create(user=request.user,course=course,score=score,total_questions=len(questions))
 return redirect('onlinecourse:show_exam_result',submission_id=sub.id)
@login_required
def show_exam_result(request,submission_id):
 sub=get_object_or_404(Submission,pk=submission_id,user=request.user)
 return render(request,'onlinecourse/exam_result_bootstrap.html',{'submission':sub})
