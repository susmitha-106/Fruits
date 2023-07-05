from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from.models import Fruits,Course,User
from django.contrib.auth.decorators import login_required
import webbrowser
from django.contrib.auth import get_user_model

user = get_user_model()


# Create your views here.
def home(request):
    return render(request,'base.html')

def fruits(request):
   if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
   if request.method=='POST':
            PhoneNumber=request.POST.get('PhoneNumber')
            FullName=request.POST.get('FullName')
            FruitName=request.POST['FruitName']
            Image=request.FILES.get('Image')
            Price=request.POST['Price']
            Description=request.POST['Description']

            F = Fruits(FruitName=FruitName,Image=Image,Price=Price,Description=Description,FullName=FullName,PhoneNumber=PhoneNumber)
            F.save()
            messages.success(request,"Thanks For Enrollment")
            return redirect('/fruits_list')
   return render(request,"fruits.html")
      
   


def fruits_list(request):
     fruits_list = Fruits.objects.all()
     return render(request,'fruits_list.html',{'fruits_list':fruits_list})



def signup(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')
        email=request.POST.get('email')
        pass1=request.POST.get('pass1')
        pass2=request.POST.get('pass2')
      
        if len(username)>10 or len(username)<10:
            messages.info(request,"Phone Number Must be 10 Digits")
            return redirect('/signup')

        if pass1!=pass2:
            messages.info(request,"Password is not Matching")
            return redirect('/signup')
       
        try:
            if User.objects.get(username=username):
                messages.warning(request,"Phone Number is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        try:
            if User.objects.get(email=email):
                messages.warning(request,"Email is Taken")
                return redirect('/signup')
           
        except Exception as identifier:
            pass
        
        
        
        myuser=User.objects.create_user(username,email,pass1)
        myuser.save()
        messages.success(request,"User is Created Please Login")
        return redirect('/login')
    return render(request,'signup.html')

def login_user(request):
    if request.method=="POST":
        username=request.POST.get('usernumber')        
        pass1=request.POST.get('pass1')
        myuser=authenticate(username=username,password=pass1)
        if myuser is not None:
            login(request,myuser)
            messages.success(request,"Login Successful")
            return redirect('fruits')
        else:
            messages.error(request,"Invalid Credentials")
            return redirect('/login')
    return render(request,"login.html")  

def handlelogout(request):
    logout(request)
    messages.success(request,"Logout Success")    
    return redirect('/login')


def profile(request):
    if not request.user.is_authenticated:
        messages.warning(request,"Please Login and Try Again")
        return redirect('/login')
    user_phone=request.user
    posts=Fruits.objects.filter(PhoneNumber=user_phone)
    print(posts)
    context={"posts":posts}
    return render(request,"profile.html",context)



@login_required
def change_password(request):
    if request.method == 'POST':
        password = request.POST['new_password']
        user = request.user
        user.set_password(password)
        user.save()
        messages.success(request, 'Your password was successfully updated!')
        return redirect('/login')  
    return render(request, 'change_password.html')


def Course_list(request):
     Course_list = Course.objects.all()
     return render(request,'Course_list.html',{'Course_list':Course_list})

def open_youtube_link(request, course_id):
    course = Course.objects.get(pk=course_id)
    youtube_link = course.youtube_link

    webbrowser.open_new_tab(youtube_link)
    return redirect('/Course_list')

    #return HttpResponse('YouTube link opened successfully.')









        

         

