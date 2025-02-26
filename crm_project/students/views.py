from django.shortcuts import render,redirect,get_object_or_404

from django.views.generic import View

from . models import DistrictChoices,TrainerChoices,BatchChoices,CourseChoices

from .utility import get_admission_number,get_password

from .models import Students

from .forms import StudentRegisterForm

from django.db.models import Q

from authentication.models import Profile

from django.db import transaction

from django.contrib.auth.decorators import login_required

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles






# Create your views here.

class GetStudentObject:

     def get_student(self,request,uuid):

          try:

               student = Students.objects.get(uuid=uuid)

               return student

          except:

               return render(request,"errorpages/error-404.html")
          
          



# @method_decorator(login_required(login_url="login"),name="dispatch")
@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")
class DashboardView(View):

     def get(self,request,*args,**kwargs):
         
      
          return render(request,"students/dashboard.html")
     
@method_decorator(permission_roles(roles=["Admin","Sales","Trainer","Academic Counsellor"]),name="dispatch")
class StudentsListView(View):
     
     def get(self,request,*args,**kwargs):

          query = request.GET.get("query")

          role = request.user.role

          if role in ["Trainer"]:

               students = Students.objects.filter(active_status=True,trainer__profile = request.user)

               if query:

                    students = Students.objects.filter(Q(active_status = True)&
                                                       Q(trainer__profile=request.user)&
                                                       (Q(first_name__icontains=query)|
                                                        Q(last_name__icontains=query)|
                                                        Q(house_name__icontains=query)|
                                                        Q(district__icontains=query)|
                                                        Q(contact_num__icontains=query)|
                                                        Q(adm_number__icontains=query)|
                                                        Q(email__exact=query)|
                                                        Q(pincode__icontains=query)|
                                                        Q(course__name__icontains=query)|
                                                        Q(trainer__first_name__icontains=query)|
                                                        Q(trainer__last_name__icontains=query)|
                                                        Q(batch__name__icontains=query)
                                                        )
                                                        )
               
          else:

               students = Students.objects.filter(active_status = True)  

               if query:

                    students = Students.objects.filter(Q(active_status = True)&(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(house_name__icontains=query)|Q(district__icontains=query)|Q(contact_num__icontains=query)|Q(adm_number__icontains=query)|Q(email__exact=query)|Q(pincode__icontains=query)|Q(course__name__icontains=query)|Q(trainer__first_name__icontains=query)|Q(trainer__last_name__icontains=query)|Q(batch__name__icontains=query)))


          print(query)

          # students  = Students.objects.all()

          

          print(students)

          data = {"students":students,"query":query}

          # for student in students:

          #      print(student.first_name)
          
          return render(request,"students/students.html",context=data)

@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")    
class RegisterView(View):
     
     def get(self,request,*args,**kwargs):

          form = StudentRegisterForm()

          # data = {"districts":DistrictChoices,"batches":BatchChoices,"trainers":TrainerChoices,"courses":CourseChoices,"form":form}

          data = {"form":form}


          
          return render(request,"students/register.html",context=data)
     

     def post(self,request,*args,**kwargs):

          form = StudentRegisterForm(request.POST,request.FILES)

          if form.is_valid():

               with transaction.atomic():

                    student =  form.save(commit=False)

                    student.adm_number = get_admission_number()

                    # student.join_date = "2025-02-05"

                    username = student.email

                    password = get_password()

                    print(password)

                    profile = Profile.objects.create_user(username=username,password=password,role="Student")

                    student.profile = profile


                    student.save()

               return redirect("students-list")
          
          else:

               data = {"form":form}

               return render(request,"students/register.html",context=data)

               

     #      form_data = request.POST

     #      # print(form_data)

     #      first_name = form_data.get("firstname")

     #      last_name = form_data.get("lastname")

     #      photo = request.FILES.get("photo")

     #      email = form_data.get("email")

     #      contact = form_data.get("contact")

     #      house_name = form_data.get("housename")

     #      post_office = form_data.get("postoffice")

     #      district = form_data.get("district")

     #      pincode = form_data.get("pincode")

     #      course = form_data.get("course")

     #      batch = form_data.get("batch")

     #      batch_date = form_data.get("batchdate")

     #      print(batch_date)

     #      trainer = form_data.get("trainer")

     #      adm_number = get_admission_number()

     #      join_date = "04-05-2024"

     #      Students.objects.create(first_name=first_name,
     #                              last_name=last_name,
     #                              photo=photo,
     #                              email=email,
     #                              contact_num= contact,
     #                              house_name=house_name,
     #                              post_office=post_office,
     #                              district=district,
     #                              pincode=pincode,
     #                              adm_number=adm_number,
     #                              course = course,
     #                              batch = batch,
     #                              batch_date = batch_date,
     #                              trainer_name = trainer
                                  

                                  



     #                              )

     #      print(adm_number)

     #      print(first_name)

     #      print(last_name)

     #      print(photo)

     #      print(email)

     #      print(contact)

     #      print(house_name)

     #      print(post_office)

     #      print(district)

     #      print(pincode)

     #      print(course)

     #      print(batch)

     #      print(batch_date)

     #      print(trainer)

          
#Student Detail View  
@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")
class StudentDetailView(View):

     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          print(uuid)

          student = GetStudentObject().get_student(request,uuid)

          # student = get_object_or_404(Students,pk=pk)


          data = {"student":student}

          return render(request,"students/student-detail.html",context=data)
     
# class Error404View(View):

#      def get(self,request,*args,**kwargs):

#           return render(request,"students/error-404.html")
     
# student delete view

@method_decorator(permission_roles(roles=["Admin","Sales","Trainer","Academic Counsellor"]),name="dispatch")     
class StudentDeleteView(View):

     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          student = GetStudentObject().get_student(uuid,request)
          
          # student.delete()

          student.active_status = False

          student.save()

          return redirect("students-list")
@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")     
class StudentUpdateView(View):

     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          student = GetStudentObject().get_student(uuid,request)

          form = StudentRegisterForm(instance=student)

          data = {"form":form}



          return render(request,"students/student-update.html",context=data)
     
     def post(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          student = GetStudentObject().get_student(uuid,request)

          form =  StudentRegisterForm(request.POST,request.FILES,instance=student)

          if form.is_valid():

               form.save()

               return redirect("students-list")
          
          

          data = {"form":form}

          return render(request,"students/student-update.html",context=data)






