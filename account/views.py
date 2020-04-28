from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users

from .tokens import account_activation_token
from django.core.mail import EmailMessage
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text
# Create your views here.


@login_required(login_url='login')
def home(request):
    students = Student.objects.all()
    teachers = Teacher.objects.all()

    context = {
        'students': students,
        'teachers': teachers
    }
    return render(request, 'account/dashboard.html', context)


@unauthenticated_user
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, email=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('sites:home')
        else:
            messages.info(request, "username or password is incorrect")
            return render(request, 'account/loginPage.html')
    context = {}
    return render(request, 'account/loginPage.html', context)


@unauthenticated_user
def registerPage(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = 'Activate your account.'
            message = render_to_string('account/acc_active_email.html', {
                'user': user,
                'domain': current_site.domain,
                'uid': urlsafe_base64_encode(force_bytes(user.id)),
                'token': account_activation_token.make_token(user),
            })
            to_email = form.cleaned_data.get('email')
            email = EmailMessage(
                mail_subject, message, to=[to_email]
            )
            #email.send()
            username = form.cleaned_data.get('username')
            # messages.success(request, f"Account was created for {username}")
            messages.success(
                request, 'Please confirm your email address to complete the registration')
            return redirect('account:login')

        else:
            for error in form.errors:
                messages.add_message(
                    request, messages.INFO, form.errors[error])

    context = {'form': form}
    return render(request, 'account/registerPage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('account:login')


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = Account.objects.get(id=uid)
        print(user.username)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.email_verified = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')
