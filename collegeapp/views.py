from django.shortcuts import render,redirect
from collegeapp.models import Course,Student,Teacher
from django.contrib.auth.models import User
from django.contrib.auth.models import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request,"base.html")

def add_course(request):
    return render(request,"add_course.html")

def course_db(request):
    if request.method=='POST':
        course_name=request.POST['course']
        course_fee=request.POST['fee']
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('admin')

def log_in(request):
    return render(request,"login.html")


def signup(request):
    return render(request,'signup.html')
    

def user(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        age=request.POST['age']
        num=request.POST['phn']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exist')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
               
                
                return redirect('log_in')
            
                print("successed")
            
        else:
            messages.info(request,'Password doesnt match')
            print("Password is not matching")
            return redirect('signup')
    else:
        return render(request,'signup.html')
                
def login_in(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            if user.is_staff:
                login(request,user)
                return redirect('admin')
            else:
                login(request,user)
                auth.login(request,user)
                messages.info(request,f'welcome  {username}')
                return redirect('welcome')
            
        else:
            messages.info(request,'Invalid username or Password')
            return redirect('/')
    else:
        return render(request,'login.html')
                


def admin(request):
    return render(request,'admin.html')

def add_stud(request):
    courses=Course.objects.all()
    return render(request,'add_stud.html',{'course':courses})

def stud_db(request):
    if request.method=='POST':
        student_name=request.POST['name']
        print(student_name)
        student_address=request.POST['address']
        print(student_address)
        age=request.POST['age']
        print(age)
        jdate=request.POST['jdate']
        print(jdate)
        sel=request.POST['sel']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        student=Student(stud_name=student_name,stud_address=student_address,stud_age=age,join_date=jdate,course=course1)
        student.save()
        return redirect('/')


def show_details(request):
    student=Student.objects.all()
    return render(request,'show_stud.html',{'students':student})

def edit(request,pk):
    course=Course.objects.all()
    students=Student.objects.get(id=pk) 
    return render(request,"stud_edit.html",{'student':students,'cs':course})

def edit_db(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.stud_name=request.POST['name']
        student.stud_address=request.POST['address']
        student.stud_age=request.POST['age']
        student.join_date=request.POST['jdate']
        dept=request.POST['cos']
        courses=Course.objects.get(id=dept)
        student.course=courses
        
        student.save()
        
        return redirect('show_details')
    return render (request,"stud_edit.html")

def delt(request,pk):
    students=Student.objects.get(id=pk)
    students.delete()
    return redirect('teach_log')

def logout(request):
    auth.logout(request)
    return render(request,"admin.html")


#Teacher.........
                
def tsignup(request):
    course=Course.objects.all()
    return render(request,'t_signup.html',{'course':course})


def tuser(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
        cpassword=request.POST['cpassword']
        email=request.POST['email']
        sel=request.POST['sel']
        address=request.POST['Address']
        Number=request.POST['number']
        print(sel)
        course1=Course.objects.get(id=sel)
        print(course1)
        
        if request.FILES.get('file') is not None:
            image=request.FILES['file']
        else:
            image="/static/image/teacher_img.jpg"
       

        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'This username already exist')
                return redirect('signup')
            else:
                user=User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()
                Userid=User.objects.get(id=user.id)
                teacher=Teacher(course=course1,user=Userid,address=address,number=Number,image=image)
                teacher.save()

               
                
                return redirect('login_in')    
            
        else:
            messages.info(request,'Password doesnt match')
            print("Password is not matching")
            return redirect('tsignup')
    else:
        return render(request,'t_signup.html')





def profile(request):
    if request.user.is_authenticated:
        userid=request.user.id
        teacher=Teacher.objects.get(user=userid)
        
    return render(request,'t_showprofile.html',{'teacher':teacher}) 

def profile_edit(request):
    if request.user.is_authenticated:
        userid=request.user.id
        teacher=Teacher.objects.get(user=userid)
        user=User.objects.get(id=userid)
        if request.method=='POST':
            teacher.address=request.POST['Address']
            teacher.number=request.POST['number']
            teacher.image=request.POST['file']
            user.first_name=request.POST['first_name']
            user.last_name=request.POST['last_name']
            user.username=request.POST['username']
            user.password=request.POST['password']
            user.email=request.POST['email']
            teacher.save()
            user.save()

           
            return redirect('profile')
        return render(request,'t_edit.html')
        

def edit_profile(request):
    userid=request.user.id
    data=Teacher.objects.get(user=userid)
    return render(request,'t_edit.html',{'data':data})


def welcome(request):
    return render(request,'t_welcome.html')

 
def showt_details(request):
    if request.user.is_authenticated:
        
        teachers=Teacher.objects.all()
        
        return render(request,'t_details.html',{'teacher':teachers})


def Del(request,pk):
    teacher=Teacher.objects.get(id=pk)
    teacher.delete()
    return redirect('/')
  



    

    