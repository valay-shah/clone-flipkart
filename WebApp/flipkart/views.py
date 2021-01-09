from django.shortcuts import render, HttpResponse, redirect
from .forms import FeedbackForm
from .models import ProductInformation, Cart
from .forms import SignUpForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django import forms


def welcome(request):
    return redirect('login')

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            userObj = form.cleaned_data
            username = userObj['username']
            email = userObj['email']
            password = userObj['password1']
            if not (User.objects.filter(username=username).exists()):# or User.objects.filter(email=email).exists()):

                user = form.save()
                user.refresh_from_db()  # load the profile instance created by the signal
                user.save()
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect('home')

            else:
                raise forms.ValidationError('Looks like a username with that email or password already exists')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})



# Create your views here.
def feedback(request):
    if request.method == 'GET':
        form = FeedbackForm
        return render(request,'feedback.html',{
            'form': form,
        })

    elif request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponse("Saved!")


def home(request):
    content = ProductInformation.objects.all()
    print("Content : ",content)
    return render(request, 'home.html',{
        'content' : content,
    })

def moreinfo(request):

    user_category = request.GET.get('category')
    content = ProductInformation.objects.filter(category=user_category).values_list('id','name','price')
    print("content : ",content)
    return render(request,'moreinfo.html',{
        'content' : content,
    })

def explore(request):
    id = request.GET.get('product_id')
    content = ProductInformation.objects.filter(id=id).values()
    content = content[0]
    return render(request,'explore.html',{
        'content':content
    })

def add_to_cart(request):
    id = request.GET.get('prod_id')
    content = ProductInformation.objects.filter(id=id).values()

    content = content[0]
    product_name = content['name']
    price = content['price']
    seller = content['seller']
    username = request.user.username
    email = request.user.email

    obj = Cart(name=username, price=price, product=product_name, email=email, seller=seller)
    obj.save()
    return render(request, "Added_successfully.html",{
        'product_name' : product_name,
    })

def view_my_profile(request):
    username = request.user.username
    content = Cart.objects.filter(name=username).values_list('product', 'price', 'seller')
    return render(request, 'mycart.html',{
        'content' : content
    })

