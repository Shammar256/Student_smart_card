from django.contrib.auth.decorators import login_required
from .models import Profile
from .forms import ProfileForm


from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from Cards.forms import CourseForm, FeesStructureForm, TuitionPaymentForm, StudentForm, CardForm, ClearanceForm
from Cards.models import FeesStructure, TuitionPayment, Student, Course, Card, Clearance
from django.contrib import messages

from django.http import HttpResponse
from Cards.utils import render_to_pdf 


@login_required
def index_view(request):
    return render(request, 'base2.html')

@login_required
def add_course_view(request): 
    message =''
    if request.method == "POST":
        course_form = CourseForm(request.POST)

        if course_form.is_valid():
            course_form.save()

        message = "Course Added Successfully"
    else:
        course_form = CourseForm()
    messages.success(request,message)

    courses = Course.objects.all()
    
    context = {
        'form':course_form,
        'msg' :message,
        'courses' :courses
    }
    return render(request, "add_course.html", context)

def edit_course_view(request, course_id):
    message = ''
    course = Course.objects.get(id=course_id)

    if request.method == "POST":
        course_form = CourseForm(request.POST, instance=course)

        if course_form.is_valid():
            course_form.save()
            message = "Changes saved successfully"
        else:
            message = "Input not in right format"
        messages.success(request,message)
    else:
        course_form = CourseForm(instance=course )
    context = {
        'form': course_form,
        'course': course,
        'message':message,
    }
    return render(request, 'edit_course.html', context)
    

@login_required
def add_student_view(request):
    message = ""
    if request.method == "POST":
        student_form = StudentForm(request.POST)

        if student_form.is_valid():
            student_form.save()

        messages.success(request, message = 'Student has been Added Successfully !')

    else:
        student_form = StudentForm()
    students = Student.objects.all()

    context = {
        'form' : student_form,
        'msg' : message,
        'students' : students,
    }

    return render(request, "add_student.html", context)

def edit_student_view(request, student_id):
    message = ''
    student  = Student.objects.get(id = student_id)

    if request.method == "POST":
        student_form =  StudentForm(request.POST, instance = student)

        if student_form.is_valid():
            student_form.save()
            message = "Changed Successfully !"

        else:
            message = "Form has invalid input"
        messages.success(request, message)
             
    else:
        student_form = StudentForm(instance = student)
        

    context = {
        'form' : student_form,
        'student' : student,
        'msg' : message,
    }

    return render(request, 'edit_student.html', context)


@login_required
def add_feesstructure_view(request):
    message = ''
    if request.method == "POST":
        feesstructure_form = FeesStructureForm(request.POST)

        if feesstructure_form.is_valid():
            feesstructure_form.save()

        messages.success(request,message = 'feesstructure added successfuly !')

    else:
        feesstructure_form = FeesStructureForm()

    feesstructures = FeesStructure.objects.all()

    context = {
        'form' : feesstructure_form,
        'msg' : message,
        'feesstructures' : feesstructures,
    }

    return render(request, "add_feesstructure.html", context)


def edit_feesstructure_view(request, feesstructure_id):
    message = ''
    feesstructure = FeesStructure.objects.get(id = feesstructure_id)

    if request.method == "POST":
        feesstructure_form = FeesStructureForm(request.POST, instance = feesstructure)

        if feesstructure_form.is_valid():
            feesstructure_form.save()
            message = "Changed Successfully !"

        else:
            message = "Form has invalid input"
        
        
    else:
        feesstructure_form = FeesStructureForm(instance = feesstructure)
        messages.success(request, message)

    context = {
        'form' : feesstructure_form,
        'feesstructure' : feesstructure,
        'msg' : message,
    }

    return render(request, 'edit_feesstructure.html', context)



@login_required
def add_tuitionpayment_view(request):
    message =''
    if request.method == "POST":
        tuitionpayment_form = TuitionPaymentForm(request.POST)

        if tuitionpayment_form.is_valid():
            tuitionpayment_form.save()

        messages.success(request, message = 'tuitionpayment added succesfully !')

    else:
        tuitionpayment_form = TuitionPaymentForm()

    tuitionpayments = TuitionPayment.objects.all()

    context = {
        'form' : tuitionpayment_form,
        'msg' : message,
        'tuitionpayments' : tuitionpayments,
    }
    return render(request, "add_tuitionpayment.html", context)


def edit_tuitionpayment_view(request, tuitionpayment_id):
    message = ""
    tuitionpayment = TuitionPayment.objects.get(id = tuitionpayment_id)

    if request.method == "POST":
        tuitionpayment_form = TuitionPaymentForm(request.POST, instance = tuitionpayment)

        if tuitionpayment_form.is_valid():
            tuitionpayment_form.save()
            message = "Changed Successfully !"

        else:
            message = "Form has invalid input"
        messages.success(request, message)
        
    else:
        tuitionpayment_form = TuitionPaymentForm (instance = tuitionpayment)

    context = {
        'form' : tuitionpayment_form,
        'tuitionpayment' : tuitionpayment,
        'msg' : message,
    }

    return render(request, 'edit_tuitionpayment.html', context)


@login_required
def add_card_view(request): 
    message =''
    if request.method == "POST":
        card_form = CardForm(request.POST)

        if card_form.is_valid():
            card_form.save()

        message = "Card Added Successfully"
    else:
        card_form = CardForm()
    messages.success(request,message)

    cards = Card.objects.all()
    
    context = {
        'form':card_form,
        'msg' :message,
        'cards' :cards
    }
    return render(request, "add_card.html", context)

def edit_card_view(request, card_id):
    message = ''
    card = Card.objects.get(id=card_id)

    if request.method == "POST":
        card_form = CardForm(request.POST, instance=card)

        if card_form.is_valid():
            card_form.save()
            message = "Changes saved successfully"
        else:
            message = "Input not in right format"
        messages.success(request,message)
    else:
        card_form = CardForm(instance=card)
    context = {
        'form': card_form,
        'card': card,
        'message':message
    }
    return render(request, 'edit_card.html', context)
    
@login_required
def add_clearance_view(request): 
    message =''
    if request.method =="POST":
        clearance_form = ClearanceForm(request.POST)

        if clearance_form.is_valid():
            clearance_form.save()

            messages.success(request,message = "Clearance Added Successfully !")

    else:
        clearance_form = ClearanceForm()

    clearances = Clearance.objects.all()

    context = {
        'form' : clearance_form,
        'msg' : message,
        'clearances' : clearances,
    }

    return render(request, "add_clearance.html", context)



def edit_clearance_view(request, clearance_id):
    message = ''
    clearance = Clearance.objects.get(id=clearance_id)

    if request.method == "POST":
        clearance_form = ClearanceForm(request.POST, instance=clearance)

        if clearance_form.is_valid():
            clearance_form.save()
            message = "Changes saved successfully"
        else:
            message = "Input not in right format"
        messages.success(request,message)
    else:
        clearance_form = ClearanceForm(instance=clearance)
    context = {
        'form': clearance_form,
        'clearance': clearance,
        'message':message,
    }
    return render(request, 'edit_clearance.html', context)
    
def delete_course_view(request, course_id):
    course = Course.objects.get(id=course_id)

    course.delete()
    
    return redirect(add_course_view)

def delete_card_view(request, card_id):
    card = Card.objects.get(id=card_id)

    card.delete()
    
    return redirect(add_card_view)



def delete_feesstructure_view(request, feesstructure_id):
    feesstructure = FeesStructure.objects.get(id = feesstructure_id)

    feesstructure.delete()
    
    return redirect(add_feesstructure_view)

def delete_tuitionpayment_view(request, tuitionpayment_id):
    tuitionpayment = TuitionPayment.objects.get(id=tuitionpayment_id)

    tuitionpayment.delete()
    
    return redirect(add_tuitionpayment_view)


def delete_clearance_view(request, clearance_id):
    clearance = Clearance.objects.get(id=clearance_id)

    clearance.delete()
    
    return redirect(add_clearance_view)

def delete_student_view(request, student_id):
    student = Student.objects.get(id=student_id)

    student.delete()
    
    return redirect(add_student_view)


def sign_up_view(request):
    if request.method == "POST":
        sign_up_form = UserCreationForm(request.POST)

        if sign_up_form.is_valid():
            sign_up_form.save()
            message = 'User Created Successfully !'

        else:
            message = 'something went wrong'
    else:
        sign_up_form =  UserCreationForm()

    context = {
        'form' : sign_up_form,
    }
    return render(request, "registration/sign_up.html", context)

def login_view(request):
    if request.method == "POST":
        login_form = UserCreationForm(request.POST)

        if login_form.is_valid():
            login_form.save()
            message = 'User Created Successfully !'

        else:
            message = 'something went wrong'
    else:
        login_form =  UserCreationForm()

    context = {
        'form' : login_form,
    }
    return render(request, "registration/login.html", context)


def student_pdf_view(request):
    students = Student.objects.all()
    context = {
        "students":students,
    }
    pdf = render_to_pdf("student_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")

def clearance_pdf_view(request):
    clearances = Clearance.objects.all()
    context = {
        "clearances" : clearances,
    }
    pdf = render_to_pdf("clearance_pdf.html", context)

    return HttpResponse(pdf, content_type = "application/pdf")




@login_required
def profile(request):
    user_profile = Profile.objects.get(user=request.user)

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=user_profile)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = ProfileForm(instance=user_profile)

    context = {
        'form': form
    }

    return render(request, 'profile.html', context)
