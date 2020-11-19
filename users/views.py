from django.shortcuts import render , redirect
from users.form import UserRegisterForm
from django.contrib import messages 

# Create your views here.





def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            print("your user name is " , username)
            messages.success(request , f'Account Created for {username} !')
            return redirect('app_blog:home')
    else:
        
        form = UserRegisterForm()
    
    
    
    context = {
        'form' : form 
    }
    return render(request , 'users/register.html', context )