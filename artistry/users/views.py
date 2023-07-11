from django.shortcuts import render,redirect,reverse
from users.models import User,Post,article
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
import uuid
from .helpers import send_forget_password_mail
from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.core.mail import EmailMessage
from django.shortcuts import render
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from django.core.mail import send_mail
import random as r

# Create your views here.




def signout(request):
    logout(request)
    messages.success(request, "logout successfully")
    return redirect(reverse('login/'))



def contest(request):
    if request.method == 'POST':
        email_subject = 'Email Subject'
        recipient_email = 'artistrinothing@gmail.com'
        sender_email = 'sandeepkotari60@gmail.com'
        uploaded_file = request.FILES.get('attachment')
        description = request.POST.get('description', '')
        g=request.user.email
        description=description+" "+"sent by "+g
        print(description)
        if uploaded_file:  
            email = EmailMessage(
                email_subject,
                description,
                sender_email,
                [recipient_email],
            )
            email.attach(uploaded_file.name, uploaded_file.read(), uploaded_file.content_type)
            email.send()
            return redirect("user_home")
    return render(request, 'contest.html')





def searchfun(request,srch_txt):
    user_list=User.objects.filter(username__icontains=srch_txt)
    ul=[]
    contents=''
    for i in user_list:
        print(i.username)
        
        contents+='''<div class="ram"><a href="view/'''+str(i.id)+'''"><img src="'''+i.profile_photo.url+'''" alt="Person" width="96" height="96"></a>'''+i.username+'''</div><br/>'''
    data = {'users':contents,}
    return JsonResponse(data)





def searched_profile(request,profile_id):
    prof=User.objects.get(id=profile_id)
    pst=Post.objects.filter(user=prof)
    articl=article.objects.filter(user=prof)
    return render(request,'search.html',{'prof':prof,'images':pst,'article':articl})
    





def toggle_like_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        is_liked=False
    else:
        post.likes.add(user)
        is_liked=True
    post.save()
    data = {'likes': post.likes.count(),'is_liked':is_liked}
    return JsonResponse(data)






def ref_toggle_like_post(request, profile_id,article_id):
    post = get_object_or_404(article, id=article_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        is_liked=False
    else:
        post.likes.add(user)
        is_liked=True
    post.save()
    data = {'likes': post.likes.count(),'is_liked':is_liked}
    return JsonResponse(data)






def pref_toggle_like_post(request, profile_id,post_id):
    post = get_object_or_404(Post, id=post_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        is_liked=False
    else:
        post.likes.add(user)
        is_liked=True
    post.save()
    data = {'likes': post.likes.count(),'is_liked':is_liked}
    return JsonResponse(data)





def index(request):
    return render(request,"home.html")





def register(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        pass1 = request.POST.get("pass1")
        pass2 = request.POST.get("pass2")
        
        if pass1 == pass2:
            user = User.objects.create_user(name, email, pass1)
            user.is_User = True
            user.save() 
            messages.success(request, "Registered successfully")
            return redirect("login")
            
        else:
            messages.error(request, "Passwords do not match")
        return redirect("register")
    return render(request, "register.html")





def e_verify(request):
    return render(request,"email_verify.html")






from django.db.models import Count
def user_home(request):
    post=Post.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')
    return render(request, "homeu.html",{'post':post}) 






def user_login(request):
    if request.method == "POST":
        name = request.POST.get("name")
        password = request.POST.get("pass")
        user = authenticate(request, username=name, password=password)
        
        if user is not None:
            login(request,user)
            messages.success(request, 'Login successful.')
            if user.is_User:
               return redirect('user_home')
                
            elif user.is_admin and user.is_staff:
                return render(request, "homea.html")
            elif user.is_staff and not(user.is_admin):
                return render(request,"homes.html")
        else:
            messages.error(request, "Invalid username or password")
    return render(request, "login.html")




def passwordreset(request):
    if request.method=='POST':
        emailid=request.POST.get('email')
        print(emailid)
        if not User.objects.filter(email=emailid):
             return render(request,'email.html')
        else:
            token=str(uuid.uuid4())
            User.objects.all().filter()
            send_forget_password_mail(emailid,token)
            return render(request,'emailsent.html')
    return render(request,'email.html')





def newpassword(request,token):
    if request.method=="POST":
        uname=request.POST.get('uname')
        pass1=request.POST.get('password')
        pass2=request.POST.get('password1')
      
        user=User.objects.get(username=uname)
        user.set_password(pass2)
        user.save()
        return render(request,'newpassword.html')
    return render(request,'newpassword.html')








@login_required
def create_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        image = request.FILES.get('image')
        post = Post.objects.create(title=title, content=content, image=image, user=request.user)
        messages.success(request, 'Post created successfully!')
        return redirect("user_home")
    else:
        return render(request, 'create_post.html')




def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'post_detail.html', {'post': post})






def view_post(request):
    if request.user.is_User:
        if request.method=="POST":
            us=request.user
            us.profile_photo=request.FILES.get('profile_pic')
            print(us.profile_photo)
            us.bio=request.POST['bio']
            us.save()
        post=Post.objects.filter(user=request.user)
        articl=article.objects.filter(user=request.user)
        return render(request,'view_post.html',{'images':post,'article':articl})
 



def contact(request):
    return render(request,"contact.html")





def help1(request):
    return render(request,"index.html")






def article1(request):
    if request.method == "POST":
        text = request.POST.get("text")
        user = request.user  
        new_article = article.objects.create(content=text, user=user)
        new_article.save()
        messages.success(request, 'Post created successfully!')
        return redirect("/view_article")
    else:
        
        return render(request, 'create_article.html')
    





    



def user_is(request):
    if request.user.is_User:
        post=Post.objects.all()
        return render(request,'view_post.html',{'post':post})







def toggle_like_article(request, article_id):
    post = get_object_or_404(article, id=article_id)
    user = request.user
    if user in post.likes.all():
        post.likes.remove(user)
        is_liked=False
    else:
        post.likes.add(user)
        is_liked=True
    post.save()
    data = {'likes': post.likes.count(),'is_liked':is_liked}
    return JsonResponse(data)







def search(request):
    if request.method=="POST":
        nam=request.POST['searchInput']
        user_list=User.objects.filter(first_name__icontains=nam)
        if user_list:
            return render(request,"search.html",{"result":user_list})
    return render(request,"search.html")






def view_article(request):
    post=article.objects.annotate(likes_count=Count('likes')).order_by('-likes_count')
    return render(request, "view_article.html",{'article':post}) 






def e_verify(request):
    if request.method=="POST":
        btn=request.POST.get('btn')
        print(btn)
        sub="Email verification"
        from1=settings.EMAIL_HOST_USER
        if btn=='1':
            mail=request.POST.get('email')
            print(mail)
            request.session['otp']=str(r.randrange(1000,9999))
            cmail=User.objects.filter(email=mail)
            request.session['mail']=mail
            if not cmail :
                to=[mail,]
                msg="Use otp"+" "+request.session['otp']+" "+"for email confirmation!"
                print(msg)
                send_mail(sub,msg,from1,to)
                return render(request,'email_verify.html',{'type': 2 })
            else:
                messages.error(request,"Entered email is already registered")
                return render(request,'email_verify.html',{'type': 1 })
          
        elif btn=='2':
            otp2=request.POST.get('otp')
            otp1=request.session['otp']
            if otp1==otp2:
                        return render(request,"register.html",{'email':request.session['mail']})
            else:
                messages.error(request,"Enter correct  OTP")
                return render(request,'email_verify.html',{'type':1}) 

    return render(request,'email_verify.html',{'type':1})







def send_msg(request):
    if request.method=="POST":
        email=request.POST.get('email')
        name=request.POST.get('name')
        msg1=request.POST.get('msg')
        from1=settings.EMAIL_HOST_USER
        to=[from1,]
        sub=" Artistry Help"
        msg="Name: "+name+"\n"+"Email: "+email+"\n"+"Query: "+msg1
        send_mail(sub,msg,from1,to)
        messages.success(request,"Query sent.!")
        return redirect('contact/')
    print("HI")
    return redirect('contact/')  



