from django.forms import ModelForm, DateInput
from Cards.models import Course, Student, FeesStructure, TuitionPayment, Card, Clearance
from django.db import models
from  django import forms

class CourseForm(ModelForm):
    class Meta:
        model = Course
        fields = '__all__'

class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = '__all__'

class FeesStructureForm(ModelForm):
    class Meta:
        model = FeesStructure
        fields = '__all__'

class TuitionPaymentForm(ModelForm):
    class Meta:
        model = TuitionPayment
        fields = ("fees_structure", "amount_paid", "payment_date", "student")
        
        widget = {"payment_date": DateInput(attrs={"type":"date"})
        
        }

class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = '__all__'

class ClearanceForm(ModelForm):
    class Meta:
        model = Clearance
        fields = ('card','year_of_study','semester','academic_year','is_test_cleared','is_exam_cleared','is_library_cleared')

        widget = {
            'is_test_cleared': forms.CheckboxInput(),
            'is_exam_cleared' : forms.CheckboxInput(),
            'is_library_cleared' : forms.CheckboxInput(),

        }




from .models import Profile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['bio', 'location', 'birth_date']
        widgets = {
            'bio': forms.Textarea(attrs={'rows': 5}),
            'birth_date': forms.DateInput(attrs={'type': 'date'}),
        }
