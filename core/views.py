from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User,auth 
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile,Post

@login_required(login_url='signin')
def index(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    posts = Post.objects.all()
    return render(request,'index.html',{'user_profile':user_profile,'posts':posts})

def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
 
        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,"Email Already Exists")
                return redirect('signup')
            elif User.objects.filter(username=username).exists():
                messages.info(request,"Username Already Exists")
                return redirect('signup')

            else:
                user = User.objects.create_user(username=username,email=email,password=password)
                user.save()

                #login the user and redirect to settings page 
                user_login  = auth.authenticate(username = username,email = email,password = password) 
                auth.login(request,user_login)
                print(dir(request.user))
                #create a profile object for the new user 

                user_model = User.objects.get(username=username) 
                new_profile = Profile.objects.create(user = user_model,id_user = user_model.id)
                new_profile.save()
                return redirect('settings')
            


        else:
            messages.info(request,"Password not matching !!")
            return redirect('signup')

    else:
        return render(request,'signup.html')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate (username = username , password = password)

        if user is None:
            messages.info(request,'Credentials Invalid')
            return redirect("signin")
        
        else:
            # for test case 
            # print(f"user is printed {dir(request.user)}")
            auth.login(request,user)
            return redirect('/')


    else:
        return render(request,"signin.html")


@login_required(login_url='signin')
def settings(request):

    user_profile = Profile.objects.get(user = request.user)
    if request.method == "POST":

        if request.FILES.get('image') == None:
            firstName = request.POST['firstname']
            lastName = request.POST['lastname']
            image = user_profile.profileImg
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.profileImg = image 
            user_profile.bio = bio
            user_profile.location = location
            user_profile.lastName = lastName
            user_profile.firstName = firstName
            user_profile.save()
        
        if request.FILES.get('image') != None:
            firstName = request.POST['firstname']
            lastName = request.POST['lastname']
            image = request.FILES.get('image')
            bio = request.POST['bio']
            location = request.POST['location']

            user_profile.lastName = lastName
            user_profile.firstName = firstName
            user_profile.profileImg = image 
            user_profile.bio = bio
            user_profile.location = location
            user_profile.save()
        

        return redirect('settings')

    return render(request,'setting.html',{'user_profile':user_profile})

@login_required(login_url='signin')
def upload(request):

    if request.method == "POST":
        user = request.user.username 
        image = request.FILES.get('image_upload')
        caption = request.POST['caption']
        new_post = Post.objects.create (user = user,caption = caption,image = image)
        new_post.save()
        return redirect("/")

    return redirect("/")

def custom_404(request, exception):  # 'exception' argument is optional
    return render(request, '404.html', status=404)
    # for later implementation

