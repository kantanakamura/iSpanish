from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404 
from django.http import JsonResponse

from .forms import BookTutorsForm
from .models import BookTutors
from accounts.models import Users


@login_required
def book_tutors(request, tutor_username):
    book_tutors_form = BookTutorsForm(request.POST or None, files=request.FILES)
    tutor = get_object_or_404(Users, username=tutor_username)
    if book_tutors_form.is_valid():
        book_tutors_form.instance.user = request.user
        book_tutors_form.instance.tutor = tutor
        book_tutors_form.save()
        return redirect('book_tutors:lecture-list')
    return render(request, 'bookTutors/book_tutors.html', context={
        'book_tutors_form': book_tutors_form,
        'tutor': tutor
    })
    

@login_required
def lecture_list(request):
    study_lecture_list = BookTutors.objects.filter(user=request.user).order_by('date')
    teach_lecture_list = BookTutors.objects.filter(tutor=request.user, is_accepted=True).order_by('date')
    lesson_request_list = BookTutors.objects.filter(tutor=request.user, is_accepted=False).order_by('date')
    return render(request, 'bookTutors/lecture_list.html', context={
        'study_lecture_list': study_lecture_list,
        'teach_lecture_list': teach_lecture_list,
        'lesson_request_list': lesson_request_list
    })
    

def accept_lecture_request(request, pk):
    lecture = get_object_or_404(BookTutors, id=pk)
    lecture.is_accepted = True
    lecture.save()
    return redirect('book_tutors:lecture-list')


def reject_lecture_request(request, pk):
    lecture = get_object_or_404(BookTutors, id=pk)
    lecture.delete()
    return redirect('book_tutors:lecture-list')


def make_lecture_completed(request, pk):
    lecture = get_object_or_404(BookTutors, id=pk)
    if request.user != lecture.user:
        return JsonResponse(
            {'message': 'You do not have permission.'}
        )
    lecture.is_done = True
    lecture.save()
    return redirect('book_tutors:lecture-list')