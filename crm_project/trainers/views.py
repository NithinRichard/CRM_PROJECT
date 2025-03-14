from django.shortcuts import render,redirect

from trainers.models import Trainers

from .forms import TrainerRegisterForm

from django.views.generic import View

from django.db.models import Q

from django.utils.decorators import method_decorator

from authentication.permissions import permission_roles

from django.db import transaction

from .utility import get_employee_id,get_password

from authentication.models import Profile

# Create your views here.

class GetTrainerObject:

     def get_student(self,request,uuid):

          try:

               trainer = Trainers.objects.get(uuid=uuid)

               return trainer

          except:

               return render(request,"errorpages/error-404.html")

# @method_decorator(login_required(login_url="login"),name="dispatch")
@method_decorator(permission_roles(roles=["Admin","Sales"]),name="dispatch")
class TrainersListView(View):
     
     def get(self,request,*args,**kwargs):

          query = request.GET.get("query")

          role = request.user.role


          if role in ["Trainer"]:

               trainers = Trainers.objects.filter(active_status=True,trainer__profile = request.user)

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&
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
                    
          elif role in ["Academic Counsellor"]:

               trainers = Trainers.objects.filter(active_status = True,batch__academic_counsellor__profile = request.user)

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&
                                                       Q(batch__academic_counsellor__profile =request.user)&
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

               trainers = Trainers.objects.filter(active_status = True)  

               if query:

                    trainers = Trainers.objects.filter(Q(active_status = True)&(Q(first_name__icontains=query)|Q(last_name__icontains=query)|Q(house_name__icontains=query)|Q(district__icontains=query)|Q(contact_num__icontains=query)|Q(adm_number__icontains=query)|Q(email__exact=query)|Q(pincode__icontains=query)|Q(course__name__icontains=query)|Q(trainer__first_name__icontains=query)|Q(trainer__last_name__icontains=query)|Q(batch__name__icontains=query)))


          print(query)

          # students  = Students.objects.all()

          

          print(trainers)

          data = {"trainers":trainers,"query":query}

          # for student in students:

          #      print(student.first_name)
          
          return render(request,"trainers/trainer-list.html",context=data)
     
class RegisterView(View):
     
     
    def get(self,request,*args,**kwargs):


        form = TrainerRegisterForm()

          
        # data = {"districts":DistrictChoices,"batches":BatchChoices,"trainers":TrainerChoices,"courses":CourseChoices,"form":form}

        data = {"form":form}


          
        return render(request,"trainers/register.html",context=data)
     

    def post(self,request,*args,**kwargs):

        form = TrainerRegisterForm(request.POST,request.FILES)

        

        if form.is_valid():

            with transaction.atomic():

                trainer =  form.save(commit=False)

                trainer.employee_id = get_employee_id()

                    # student.join_date = "2025-02-05"

                username = trainer.email

                password = get_password()

                print(password)

                profile = Profile.objects.create_user(username=username,password=password,role="Trainer")

                trainer.profile = profile


                trainer.save()

                return redirect("trainers-list")
          
        else:

            data = {"form":form}

            return render(request,"trainers/register.html",context=data)

     

   

class TrainerDetailView(View):
     
     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          print(uuid)

          trainer = GetTrainerObject().get_student(request,uuid)

          # student = get_object_or_404(Students,pk=pk)


          data = {"trainer":trainer}

          return render(request,"trainers/trainer-detail.html",context=data)

class TrainerUpdateView(View):
     
     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          trainer = GetTrainerObject().get_student(request,uuid)

          form = TrainerRegisterForm(instance=trainer)

          data = {"form":form}



          return render(request,"students/student-update.html",context=data)
     
     def post(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          trainer = GetTrainerObject().get_student(request,uuid)

          form =  TrainerRegisterForm(request.POST,request.FILES,instance=trainer)

          if form.is_valid():

               form.save()

               return redirect("trainers-list")
          
          

          data = {"form":form}

          return render(request,"trainers/trainer-update.html",context=data)







  

class TrainerDeleteView(View):
     
     
     def get(self,request,*args,**kwargs):

          uuid = kwargs.get("uuid")

          trainer = GetTrainerObject().get_student(request,uuid)
          
          # student.delete()

          trainer.active_status = False

          trainer.save()

          return redirect("trainers-list")
  