from django.shortcuts import redirect,render
from django.contrib import messages
from app.models import User
from django.contrib import auth
from app.models import account_profile,Post  
from django.contrib.auth.decorators import login_required

@login_required(login_url="signin")
def home (request):
    # user_object=User.objects.get(username=request.user.username)
    # user_profile=account_profile.objects.get(user=user_object)
    # return render (request,"index.html",{'user_profile':user_profile})
        return render (request,"index.html")

@login_required(login_url="signin")
# def user_bio(request):
#     user_profile = account_profile.objects.get(user=request.user)
#     if request.method == "POST":     
#         if request.FILES.get('image')== None:
#             image=user_profile.profile_image
#             bio=request.POST['bio']
#             location=request.POST['location']
            
#             user_profile.profile_image=image
#             user_profile.bio=bio
#             user_profile.location=location
#             user_profile.save()

#         if request.FILES.get('image') != None:
#             image=request.FILES.get('image')
#             bio=request.POST['bio']
#             location=request.POST['location']

#             user_profile.bio=bio
#             user_profile.profile_image=image
#             user_profile.location=location
#             user_profile.save() 
#             return redirect ("user_bio")
        
#         return render(request,"setting.html",{'user_profile':user_profile})

def user_bio(request):
    if request.method == 'GET':
        return render(request, 'setting.html')
    else:
        return HttpResponse("Invalid request", status=400)

def sign_up(request):     
        if request.method=="POST":
            username=request.POST["username"]
            email =request.POST["email"]
            password=request.POST["password"]
            password1=request.POST["password1"]
            if password==password1:
                if User.objects.filter(email=email).exists():
                    messages.info(request,"email already exist")
                    return redirect("signup")
                
                elif User.objects.filter(username=username).exists():
                    messages.info(request,"user is already taken")
                    return redirect("signup")
                else:
                    user=User.objects.create_user(username=username,email=email,password=password)
                    user.save()
                    
                    
                    
                    #extra
                    user_login=auth.authenticate(username=username,password=password)
                    auth.login(request,user_login)
                    
                    
                    #create profile for newusers
                    user_model=User.objects.get(username=username)
                    profile=account_profile.objects.create(user=user_model,id_user=user_model.id)
                    profile.save()
                    return redirect('signin')   
            else:
                messages.info(request,"password  is  not mismatch") 
                return redirect('signup')
        else:  
            return render (request,"signup.html") 
        
def signin (request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, "User and password don't match")
            return redirect('signin')
    else:
        return render (request,"signin.html")
    
    
@login_required(login_url="signin")
def logout(request):
    auth.logout(request)
    return redirect('signin')

@login_required(login_url="signin")
def upload(request):
    if request.method == "POST":
        user=request.user.username
        image=request.Fiels.get('')
    




