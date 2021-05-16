from django.shortcuts import render
from django.views import View
from .models import Student, Course, Cart, OrderPlaced
from .forms import StudentRegistrationForm

class homeView(View):
    def get(self,request):
        webDevlopment = Course.objects.filter(category='WB')
        cloudLearn = Course.objects.filter(category ='CL')

        return render(request, 'app/home.html', {'WebDevlopment':webDevlopment,'cloudLearn':cloudLearn})


def login(request):
    return render(request, 'app/login.html')


class StudentRegistrationView(View):
    def get(self, request):
        form = StudentRegistrationForm()
        return render(request, 'app/studentregistration.html', {'form': form})

    def post(self, request):
        form = StudentRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
        return render(request, 'app/studentregistration.html', {'form': form})

# def webDevlopment(request):
 
#     webDevlopment=Course.objects.filter(category='WB')
    
#     return render(request, 'app/webDevlopment.html', {webDevlopment:webDevlopment})


# def cloudLearn(request):

#     cloudLearn = Course.objects.filter(category='CL')

#     return render(request, 'app/cloudLearn.html', {cloudLearn: cloudLearn})


# def add_to_cart(request):
#     return render(request, 'app/addtocart.html')


# def buy_now(request):
#     return render(request, 'app/buynow.html')


# def profile(request):
#     return render(request, 'app/profile.html')


# def address(request):
#     return render(request, 'app/address.html')


# def orders(request):
#     return render(request, 'app/orders.html')


# def change_password(request):
#     return render(request, 'app/changepassword.html')








