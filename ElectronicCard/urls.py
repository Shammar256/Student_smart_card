"""ElectronicCard URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Cards.views import index_view, add_feesstructure_view, add_tuitionpayment_view, edit_tuitionpayment_view, edit_feesstructure_view, edit_student_view, add_student_view, add_course_view, edit_course_view, edit_card_view, add_card_view, add_clearance_view, edit_clearance_view, delete_tuitionpayment_view, delete_feesstructure_view, sign_up_view, delete_card_view, delete_clearance_view, delete_course_view, delete_student_view, student_pdf_view, clearance_pdf_view, profile


urlpatterns = [
    path('admin/', admin.site.urls),
    path('profile/', profile, name='profile_page'),
    path('sign_up/',sign_up_view, name = "sign_up_page"),
    path('accounts/', include("django.contrib.auth.urls")),
    path('', index_view, name = 'index_page'),
    path('add_course/', add_course_view, name= "add_course_page" ),
    path('add_student/', add_student_view, name = 'add_student_page'),
    path('add_feesstructure/', add_feesstructure_view, name = 'add_feesstructure_page'),
    path('add_tuitionpayment/', add_tuitionpayment_view, name = 'add_tuitionpayment_page'),
    path('add_card/',add_card_view,name='add_card_page'),  
    path('add_clearance/',add_clearance_view, name='add_clearance_page'),
    path('edit_course/<int:course_id>/', edit_course_view, name="edit_course_page"),
    path('edit_student/<int:student_id>/', edit_student_view, name = "edit_student_page"),
    path('edit_feesstructure/<int:feesstructure_id>/', edit_feesstructure_view, name = "edit_feesstructure_page"),
    path('edit_clearance/<int:clearance_id>/', edit_clearance_view, name="edit_clearance_page"),
    path('edit_tuitionpayment/<int:tuitionpayment_id>/', edit_tuitionpayment_view, name = "edit_tuitionpayment_page"),
    path('edit_card/<int:card_id>/', edit_card_view, name="edit_card_page"),
    path('delete_feestructure/<int:feestructure_id>/',delete_feesstructure_view, name="delete_feesstructure_page"),
    path('delete_tuitionpayment/<int:tuitionpayment_id>/', delete_tuitionpayment_view, name="delete_tuitionpayment_page"),
    path('delete_card/<int:card_id>/', delete_card_view, name="delete_card_page"),
    path('delete_clearance/<int:clearance_id>/', delete_clearance_view, name="delete_clearance_page"),
    path('delete_course/<int:course_id>/', delete_course_view, name="delete_course_page"),
    path('delete_student/<int:student_id>/', delete_student_view, name="delete_student_page"),
    path('student_pdf/', student_pdf_view, name='student_pdf_page'),
    path('clearance_pdf/', clearance_pdf_view, name='clearance_pdf_page')
]

