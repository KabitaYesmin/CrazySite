from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, HttpResponse, redirect
from django.views.generic import ListView, DetailView, CreateView

from .models import *
from .models import Post
from .models import Video
from .models import images


def context(request):
    video = Video.objects.all()
    return render(request, "Blog_App/context.html", {"video": video})


def HomePage(request):
    return render(request, 'Blog_App/home.html')


def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('Blog_App/login.html')

    return render(request, 'Blog_App/signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('context')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'Blog_App/login.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')


def imagesView(request):
    if request.method == 'POST':
        form = images(request.POST)

        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = imagesView(request)
    return render(request, 'Blog_App/images.html', {'form': form})


def success():
    return HttpResponse('successfully uploaded')


def display_images(request):
    if request.method == 'GET':
        # getting all the objects of hotel.
        display = display_images.objects.all()
        return render((request, 'display_images.html',
                       {'display_images': display}))


class ArticleDetailView(DetailView):
    model = Post
    template_name = 'Blog_App/article_details.html'
    context_object_name = 'Article'


class AddPostCreateView(CreateView):
    model = Post
    template_name = 'Blog_App/add_post.html'
    fields = '__all__'


class Dashboard(ListView):
    model = Post
    template_name = 'Blog_App/Dashboard.html'


class trendingListView(ListView):
    model = Video
    template_name = 'Blog_App/trending.html'
