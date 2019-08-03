from django.shortcuts import render
from fun7app.models import Father,Student,User
from fun7app.forms import StudentProfileInfoForm, UserForm

# Create your views here.
def index(request):
    return render (request,'fun7app/index.html')
def home(request):
    return render(request,'fun7app/home.html')
def mtv(request):
    student_list=Student.objects.order_by('NameStudent')
    listy={'stu_key':student_list}
    return render(request,'fun7app/mtv.html',context=listy)

def register(request):

    registered=False
    if request.method=='POST':
        user_form=UserForm(request.POST)
        student_form=StudentProfileInfoForm(request.POST)

        if user_form.is_valid() and student_form.is_valid():
            allfields=user_form.save()
            allfields.set_password(allfields.password)
            allfields.save()

            profile=student_form.save(commit=False)
            profile.allfields=allfields

            if 'profile_pic_blnk' in request.FILES:
                print('found the image')
                profile.profile_pic_blnk=request.FILES['profile_pic_blnk']

            profile.save()

            registered=True
        else:
            print(user_form.errors,student_form.errors)
    else:
        print("form is not POSTED AS OF NOW/OR METHOD != POST")
        user_form=UserForm()
        student_form=StudentProfileInfoForm()

    dict={'user_form':user_form, 'student_form':student_form , 'registered':registered}
    return render(request,'fun7app/registration.html',context=dict)
