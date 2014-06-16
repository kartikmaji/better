from django.shortcuts import render,render_to_response
from forms import SignupForm,LoginForm
from django.contrib.auth import login,authenticate
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
#from django.conf import settings
#from django.core.urlresolvers import reverse
#from django.http import HttpResponseRedirect
#from django.template.response import TemplateResponse
from django.utils.translation import ugettext as _
#from django.shortcuts import resolve_url
from django.views.decorators.csrf import csrf_protect
from django.template import RequestContext
from django.contrib.auth import REDIRECT_FIELD_NAME, login as auth_login, logout, get_user_model

#from django.contrib.auth.decorators import login_required
#from django.contrib.auth.forms import AuthenticationForm, PasswordResetForm, SetPasswordForm, PasswordChangeForm
#from django.contrib.auth.tokens import default_token_generator
#from django.contrib.sites.models import get_current_site
#from django.contrib.auth.models import User
# Create your views here.

def home(request):
	if request.user.is_authenticated():
		#return HttpResponse("Hello")
		current_user= request.user
		#return HttpResponse(current_user)
		return render(request,'users/welcome.html',{'current_user':current_user})
	else:
		return render(request,'index.html',{})
		#return HttpResponse("You are not logged in")

def user_logout(request):
	if request.user.is_authenticated():
		logout(request)
		return HttpResponseRedirect("/")
	else:
		return HttpResponse("You have to be logged in before getting to logout.")
	
def signup(request):
	if request.method=="POST":
		form= SignupForm(request.POST)
		if form.is_valid():
			new_user = User.objects.create_user(**form.cleaned_data)
			User.backend='django.contrib.auth.backends.ModelBackend'
			authenticate()
			login(request,new_user) 
			#redirect, or however you want to get to the main view
			return HttpResponseRedirect('/')
	else:
		form = SignupForm()
	return render(request,'users/adduser.html',{'form':form})
	#return HttpResponseRedirect('/')

"""def login(request, template_name='users/login.html',
          redirect_field_name=REDIRECT_FIELD_NAME,
          authentication_form=AuthenticationForm,
          current_app=None, extra_context=None):

    #Displays the login form and handles the login action.
    redirect_to = request.REQUEST.get(redirect_field_name, '/users/welcome.html')

    if request.method == "POST":
        form = authentication_form(request, data=request.POST)
        if form.is_valid():

            # Ensure the user-originating redirection url is safe.
            if not is_safe_url(url=redirect_to, host=request.get_host()):
                redirect_to = resolve_url(settings.LOGIN_REDIRECT_URL)

            # Okay, security check complete. Log the user in.
            auth_login(request, form.get_user())

            return HttpResponseRedirect(redirect_to)
    else:
        form = authentication_form(request)

    current_site = get_current_site(request)

    context = {
        'form': form,
        'redirect_field_name': redirect_to,
        'site': current_site,
        'site_name': current_site.name,
    }
    if extra_context is not None:
        context.update(extra_context)
    return TemplateResponse(request, template_name, context,
                            current_app=current_app)

"""
def user_login(request):
	context = RequestContext(request)
	if request.method == "POST":
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user:
			if user.is_active:
				authenticate()
				login(request,user)
				return HttpResponseRedirect('/')
			else:
				return HttpResponse("Your account is disabled")
		else:
			return HttpResponse("Invalid login")
	else:	
		return render_to_response("users/login.html",{},context)
	"""
	if request.method == "POST" :
		form= LoginForm(request.POST)
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				HttpResponse(request.user)
				# Redirect to a success page.
			else:
				HttpResponse("Disabled account")
				# Return a 'disabled account' error message
		else:
			HttpResponse("Invalid login")
			# Return an 'invalid login' error message.
	else:
		form=LoginForm()
	return render(request,'users/login.html',{'form':form})"""


