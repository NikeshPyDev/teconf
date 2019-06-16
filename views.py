# from django.contrib.sites.shortcuts import get_current_site
from django.shortcuts import render, redirect
# from django.utils.encoding import force_bytes
# from django.template.loader import render_to_string
# from django.utils.http import urlsafe_base64_encode
from .forms import SignUpForm
from django.contrib.auth import authenticate
from django.contrib.auth.views import auth_login
# from django.contrib.auth.tokens import default_token_generator


def home(request):
    return render(request, 'home.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            # current_site = get_current_site(request)
            # subject = 'Activate Your MySite Account'
            # message = render_to_string('account_activation_email.html', {
            #     'user': user,
            #     'domain': current_site.domain,
            #     'uid': urlsafe_base64_encode(force_bytes(user.pk)),
            #     'token': default_token_generator.make_token(user),
            # })
            # user.email_user(subject, message)
            # return redirect('account_activation_sent')
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=raw_password)
            auth_login(request, user, backend='django.contrib.auth.backends.ModelBackend')
        return render(request, 'home.html')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})

# def login(request):
#     if request.method == 'POST':


