from django.shortcuts import render, redirect
from .models import School

# Create your views here.

def home(request):
    return render(request, 'index.html')

def insert(request):
    return render(request, 'insert.html')

def insert_data(request):
    if request.method == 'POST':
        class_name = request.POST['class_name']
        number_of_students = request.POST['number_of_students']
        teacher = request.POST['teacher']
        mentor = request.POST['mentor']
        img = request.FILES['img']

        school = School(class_name=class_name, 
                        number_of_students=number_of_students,
                        teacher=teacher,
                        mentor=mentor,
                        image=img
                        )
        school.save()
        return redirect('view')
    else:
        return render(request, 'insert.html')
    


def view_data(request):
    school = School.objects.all()
    
    return render(request, 'view.html', {'schooler': school})


def update(request, id):
    school = School.objects.get(id=id)
    if request.method == 'POST':
        class_name = request.POST['class_name']
        number_of_students = request.POST['number_of_students']
        teacher = request.POST['teacher']
        mentor = request.POST['mentor']
        img = request.FILES['img']

        school.class_name = class_name
        school.number_of_students = number_of_students
        school.teacher = teacher
        school.mentor = mentor
        school.image = img

        school.save()

        return redirect('view')
    return render(request, 'update.html', {'school': school})

def delete_dt(request, id):
    school = School.objects.get(id=id)
    school.delete()
    return redirect('view')

    
    



