from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout as Logout_session
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import User,Blog,Like,comment,Dislike

# Create your views here.
def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request)
            return redirect('home')  # Redirect to home or another appropriate view
        else:
            messages.error(request, "Invalid credentials, please try again")
    return render(request, 'login.html')



def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        firstname = request.POST.get('firstname')
        lastname = request.POST.get('lastname')
        email = request.POST.get('email')
        password1 = request.POST.get('password')
        password2 = request.POST.get('confirm_password')
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "This username already exists, try another")
            elif User.objects.filter(email=email).exists():
                messages.error(request, "This email already exists, try another")
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=firstname,
                    last_name=lastname,
                    password=password1
                )
                user.save()
                messages.success(request, "Your account has been created successfully")
                return redirect('login')
        else:
            messages.error(request, "Passwords did not match")
    return render(request, 'register.html')


# handle the logic of blogs and creating the datastructure associate with other models
def handle(blog_list)->list[dict]:
    Accurate_data = []
    for blog in blog_list:
        temp = {"blog_content":blog}
        #handle likes data
        list_likes=Like.objects.filter(blog = blog.id).count()
        temp['count_of_likes'] = list_likes

        # handle comments data
        list_comments = comment.objects.filter(blog = blog.id)
        count_of_comments = comment.objects.filter(blog = blog.id).count()
        temp['count_of_comment'] = count_of_comments
        temp['list_comment'] = list_comments

        # handle Dislikes
        count_of_dislikes = Dislike.objects.filter(blog = blog.id).count()
        temp['count_dislikes'] = count_of_dislikes

        # appending the temperary dict
        Accurate_data.append(temp)
    
    return Accurate_data

@login_required(login_url='login/')
def add_comment(request,blog_id):
    # when user already login....
    user_id = request.POST.get('user_id')
    text_by_user = request.POST.get('comment')

    # geting the instance of user and blog by their id's
    user = User.objects.get(id=user_id)
    blog = Blog.objects.get(id=blog_id)

    # creating the comment object and saving it
    comment_instance = comment.objects.create(blog = blog , user = user ,comment_content = text_by_user)
    comment_instance.save()
    messages.success(request,"Your comment is added successfully!")
    return redirect('home')


@login_required(login_url='login/')
def home(request):
    All_blogs = Blog.objects.all()
    Main_data=handle(All_blogs)
    return render(request ,'home.html',{"data":Main_data})

@login_required(login_url='login/')
def add_like(request,blog_id,user_id =None):
    # if user_id is None:
    #     return redirect('login')
    
    user = User.objects.get(id=user_id)
    blog = Blog.objects.get(id=blog_id)
    obj_of_like = Like.objects.filter(user = user,blog = blog)
    if obj_of_like.exists():
        # deleted the like obj
        obj_of_like.delete()
        return redirect('home')
    
    instance_like = Like.objects.create(blog = blog , user = user)
    instance_like.save()
    # print(instance_like)
    messages.success(request,"Your like is added successfully!")
    return redirect('home')

@login_required(login_url='login/')
def add_dislike(request, blog_id, user_id=None):
    # if user_id is None:
    #     return redirect('login')
    
    # fetching the respective instance
    fetch_user = User.objects.get(id=user_id)
    fetch_blog = Blog.objects.get(id=blog_id)
    obj_of_dislike = Dislike.objects.filter(user = fetch_user , blog = fetch_blog)
    
    # checking if already liked the post
    if obj_of_dislike.exists():
        # deleting the dislike obj
        obj_of_dislike.delete()
        return redirect('home')
    
    # creating the dislike object
    instance_dislike = Dislike.objects.create(blog = fetch_blog , user = fetch_user)
    instance_dislike.save()
    messages.success(request,"Your dislike is added successfully!")
    return redirect('home')
        
# logout from session
def logout(request):
    Logout_session(request)
    return redirect('login')


