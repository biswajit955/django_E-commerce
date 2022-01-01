from django.shortcuts import render, redirect
from django.http.response import HttpResponse

from product.views import home
from .models import Customer
from django.contrib import messages
from django.contrib.auth.hashers import make_password, check_password


# Create your views here.

def signup(request):
    if request.method == 'POST':
        firstname = request.POST.get('first_name')
        lastname = request.POST.get('last_name')
        phone = request.POST.get('phone_no')
        email = request.POST.get('email_id')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        print(type(password1))

    # ------------ error chack --------------
        error_mgs = None
        if not firstname:
            error_mgs = "First Name Required !"
        elif len(firstname) < 4:
            error_mgs = 'First Name must be 4 char long or more'
        elif not lastname:
            error_mgs = "Last Name Required !"
        elif len(lastname) < 4:
            error_mgs = 'Last Name must be 4 char long or more'
        elif not phone:
            error_mgs = "Phone Required !"
        elif len(phone) < 13:
            error_mgs = 'Phone must be 13 char long or more and must add +91 at first'
        elif not email:
            error_mgs = "Email Required !"
        elif len(email) < 5:
            error_mgs = 'Email must be 5 char long'
        elif not password1:
            error_mgs = "enter password !"
        elif len(password1) < 8:
            error_mgs = 'password must be 8 char long'
        elif not password2:
            error_mgs = "enter Conform password !"
        elif len(password2) < 8:
            error_mgs = 'Conform password must be 8 char long'
        elif password1 != password2:
            error_mgs = 'Enter same password in to pasword fild'
        elif (password1 == firstname):
            error_mgs = 'change your password, your password similer to first name '
        elif (password1 == lastname):
            error_mgs = 'change your password, your password similer to last name '
        elif password1:
            if (('@' not in password1)
                and ('0' not in password1)
                and ('1' not in password1)
                and ('2' not in password1)
                and ('3' not in password1)
                and ('4' not in password1)
                and ('5' not in password1)
                and ('6' not in password1)
                and ('7' not in password1)
                and ('8' not in password1)
                and ('9' not in password1)
                and ('#' not in password1)
                and ('$' not in password1)
                and ('%' not in password1)
                and ('&' not in password1)
                and ('!' not in password1)
                and ('*' not in password1)
                ):
                error_mgs = 'change your password,You need to add minimum one special character and one number '
            pass

        # --------------This is for holding value in singpage if come error_mgs---------------
        value = {
            'first_name': firstname,
            'last_name': lastname,
            'email': email
        }
        data = {
            'error': error_mgs,
            'values': value
        }

        # -----------------saving------------------
        if error_mgs:
            return render(request, 'signup.html', data)
        password = make_password(password1)
        customer = Customer(first_name=firstname,
                            last_name=lastname,
                            phone_no=phone,
                            email_id=email,
                            password1=password,
                            password2=password2)
        customer.save()
        return redirect('login')
    return render(request, 'signup.html')


def login(request):
    error_mgs = None
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:

            customer = Customer.objects.get(email_id=email)
            print(customer.password1)
            print(customer.id)
            if customer:
                flag = check_password(password, customer.password1)
                print(flag)

                if flag:
                    request.session['customer'] = customer.id
                    return redirect('home')
                else:
                    error_mgs = 'Email or Password invalid !!'
                    return render(request, 'login.html', {'error_mgs': error_mgs})
            error_mgs = 'Email or Password invalid !!'
            return render(request, 'login.html', {'error_mgs': error_mgs})
        except:
            error_mgs = 'Email or Password invalid !!'
    return render(request, 'login.html', {'error_mgs': error_mgs})


def logout(request):
    try:
        request.session.clear()
    except KeyError:
        pass
    return redirect('login')
    
    
