from django.shortcuts import render, redirect, HttpResponse
from .models import AllCourse, Contact, Blog, Motivational_Quote
from datetime import datetime
from django.utils import timezone
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth import logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import authenticate as auth_authenticate
from django.contrib.auth.models import User, auth
from django.core.paginator import Paginator
import random
# from Your_Educator.settings import EMAIL_HOST_USER
# Create your views here.

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def courses(request):
    post = AllCourse.objects.all()
    paginator = Paginator(post, 6) # Show 6 objects per page.
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    num = 0
    for num2 in page_obj.paginator.page_range:
        if num < num2:
            num = num2
    return render(request, 'course.html', {'cour': page_obj, 'lastpage': num})

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        countrycode = request.POST.get('countrycode')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        contact = Contact(name=name, email=email, phone=phone, subject=subject,countrycode=countrycode, message=message, date=datetime.today(), time=timezone.now())
        contact.save()
        messages.success(request, 'Your query has been recorded')
        return redirect(request.META.get('HTTP_REFERER', '/'))
    return render(request, 'contact.html')

def search(request):
    if request.method == "GET":        
        query = request.GET['search']
        if len(query) >= 60:
            messages.error(request, "Sorry😥, your query was too long:\n i)Try different key word.\nii)Try more general keywords.\niii)Make sure that all words are spelled correctly.")
            return redirect('/course')
        elif len(query) == 0:
            return redirect('/course')
        else:
            postname = AllCourse.objects.filter(Name__icontains=query)
            postadd = AllCourse.objects.filter(Desc__icontains=query)
            postad = AllCourse.objects.filter(Category__icontains=query)
            post = postname.union(postadd,postad)
            if len(post) == 0:
                messages.error(request, 'No search results found.')
                return redirect('/course')
            else:
                return render(request, 'search.html', {'cour': post})

def teacher(request):
    return render(request, 'teacher.html')

def blog(request):
    allblogs = Blog.objects.all()
    return render(request, 'blog.html', {'allblogs': allblogs})

def blog_single(request):
    return render(request, 'blog-single.html')

def event(request):
    return render(request, 'event.html')

li = list()
lo = list()
def subscription(request):
    if request.method == "POST":
        email = str(request.POST.get('email'))
        email = email[-1].replace(' ','')
        mail = Motivational_Quote(email=email)
        mail.save()
        messages.success(request, 'Thanks for subscribing')
        return redirect(request.META.get('HTTP_REFERER', '/'))      
        
def subscribe(request):
    if request.method == "POST":
        email = request.POST.get('email')
        no = random.randint(26723, 94734)
        li.append(no)
        li.append(email)
        message = f'Your otp is {no}'
        subject = 'Verification Code'
        lo.append(email)
        recepient = lo
        send_mail(subject, message, EMAIL_HOST_USER, recepient)
        return redirect(request.META.get('HTTP_REFERER','/'))      

def teacher_single(request):
    return render(request, 'teacher-single.html')

def otp(request):
    no = li[0]
    email = li[1]
    if request.method == "POST":
        verifi = request.POST.get('codever')
        verificationcode = int(verifi)
        if verificationcode == no:
            mail = Motivational_Quote(email=email)
            mail.save()
            messages.success(request, 'Thanks for subscribing')
            return redirect('/')
            li.clear()
            lo.clear()
        else:
            messages.error(request, 'Code Does not match. Please try again.')
    return render(request, 'otp.html')

def signup(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('Password')
        email = request.POST.get('email')
        try:
            myuser = User.objects.create_user(username, email, password)
            myuser.save()
            messages.success(request, "Your account has been created")
            user = auth_authenticate(username=username, password=password)
            auth.login(request, user)
        except:
            messages.error(request, "Username already exists.")
        return redirect(request.META.get('HTTP_REFERER', '/'))      
    return render(request, 'not found.html')

def login(request):
    if  request.method == "POST":
        pword = request.POST['Password']
        uname = request.POST['username']
        user = auth_authenticate(username=uname, password=pword)
        if user is not None:
            auth.login(request, user)
            messages.success(request, "Successfully logged In")
            return redirect(request.META.get('HTTP_REFERER', 'redirect_if_referer_not_found'))
        else:
            messages.warning(request, "Invalid Credentials, Please try again.")
            return redirect(request.META.get('HTTP_REFERER', '/'))

def logout(request):
    auth.logout(request)
    messages.success(request, "Succesfully Logged Out")
    return redirect(request.META.get('HTTP_REFERER', '/'))