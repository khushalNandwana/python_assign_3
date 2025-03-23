from django.shortcuts import render, redirect
from .models import Student
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


def index(request):
    try:
        if request.method == 'POST':
            name = request.POST.get('name')
            age = request.POST.get('age')
            email = request.POST.get('email')
            marks = request.POST.get('marks')
            user = Student(name=name, age=age, email=email, marks=marks)
            user.save()
            messages.success(request, 'Student data saved successfully')
            return redirect('index')
    except Exception as e:
        messages.error(request, 'Failed to save student data, Error: {}'.format(e))
        return redirect('index')
    return render(request, 'index.html')

def students(request):
    students = Student.objects.all()
    messages.success(request, 'Student data fetched successfully')
    return render(request, 'students.html', {'students': students})

def update(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        user = Student.objects.get(id=id)
        user.name = request.POST.get('name')
        user.age = request.POST.get('age')
        user.email = request.POST.get('email')
        user.marks = request.POST.get('marks')
        user.save()
        return redirect('update')
    return render(request, 'update.html')

def delete(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        user = Student.objects.get(id=id)
        user.delete()
        return redirect('delete')
    return render(request, 'delete.html')

@csrf_exempt
def api_create_student(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            student = Student(
                name=data['name'],
                age=data['age'],
                email=data['email'],
                marks=data['marks']
            )
            student.save()
            return JsonResponse({'message': 'Student created successfully'}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def api_get_students(request):
    if request.method == 'GET':
        students = Student.objects.all()
        students_list = list(students.values())
        return JsonResponse(students_list, safe=False, status=200)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def api_update_student(request, id):
    if request.method == 'PUT':
        try:
            data = json.loads(request.body)
            student = Student.objects.get(id=id)
            student.name = data['name']
            student.age = data['age']
            student.email = data['email']
            student.marks = data['marks']
            student.save()
            return JsonResponse({'message': 'Student updated successfully'}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def api_delete_student(request, id):
    if request.method == 'DELETE':
        try:
            student = Student.objects.get(id=id)
            student.delete()
            return JsonResponse({'message': 'Student deleted successfully'}, status=200)
        except Student.DoesNotExist:
            return JsonResponse({'error': 'Student not found'}, status=404)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Invalid request method'}, status=405)    

# Create your views here.
