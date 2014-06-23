from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponseRedirect

from django import forms
#from blog.models import Base, Blogs
#import blog.models as bm

class LoginForm(forms.Form):
    email = forms.CharField('email', validators=[Email()])
    password = forms.CharField('password', validators=[DataRequired()])


class SignUpForm(forms.Form):
    email = forms.TextField('email', validators=[Email()])
    password = forms.PasswordField('password', validators=[DataRequired()])
    fullname = forms.TextField('fullname', validators=[DataRequired()])




# Create your views here.
def login(request):
    print "add_new"
    if request.method == 'POST': # If the form has been submitted...
        print request.POST
        #bm.add_new_blog( request.POST['desciption']
        #        , request.POST['message']
        #        ) 
        #form = ContactForm(request.POST) # A form bound to the POST data
        return HttpResponseRedirect('/tw_study/index') # Redirect after POST

    return render(request, 'tw_study/login.html', {
        #'form': form,
        'action':"/blog/add_new/",
        'user_name':'',
        'password':'',
    })



def register(request):
    print "register"
    pass
    if request.method == 'POST': # If the form has been submitted...
        print request.POST
        #bm.add_new_blog( request.POST['desciption']
        #        , request.POST['message']
        #        ) 
        #form = ContactForm(request.POST) # A form bound to the POST data
        return HttpResponseRedirect('/tw_study/login') # Redirect after POST

    return render(request, 'tw_study/register.html', {
        #'form': form,
        'action':"/blog/add_new/",
        'user_name':'',
        'password':'',
    })

