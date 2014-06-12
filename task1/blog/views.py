from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader
from django.http import HttpResponseRedirect

from django import forms
from blog.models import Base, Blogs
import blog.models as bm

class BlogItem(forms.Form):
    desciption = forms.CharField(max_length=20)
    message = forms.CharField(max_length=100)


# Create your views here.
def index(request):
    #list = bm.Blogs.objects.all()
    list = bm.get_all_items()
    t = loader.get_template('blog/index.html')
    c = Context({
        'msg': "Hello from here",
        'blog_list': list
    })
    return HttpResponse(t.render(c))


def add_new(request):
    print "add_new"
    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        print request.POST
        bm.add_new_blog( request.POST['desciption']
                , request.POST['message']
                ) 
        #form = ContactForm(request.POST) # A form bound to the POST data
        return HttpResponseRedirect('/blog/') # Redirect after POST
    else:
        form = BlogItem() # An unbound form

    return render(request, 'blog/add_new.html', {
        'form': form,
        'action':"/blog/add_new/",
    })
    #return HttpResponse("Add new" )

def edit(request, blog_id):
    response = "Edit %s."
    print "edit"
    (d, t) = bm.get_blog_items(blog_id)

    if request.method == 'POST': # If the form has been submitted...
        # ContactForm was defined in the previous section
        print request.POST
        bm.update_blog_item( blog_id
                , request.POST['desciption']
                , request.POST['message']
                ) 
        #form = ContactForm(request.POST) # A form bound to the POST data
        return HttpResponseRedirect('/blog/') # Redirect after POST
    else:
        print "form item:", d ,":", t
        dic = {
          "desciption": d,
          "message": t,
	}
        form = BlogItem(dic) # An unbound form
        #form.description = d
        #form.message = t
        print "done"

    return render(request, 'blog/add_new.html', {
        'form': form,
        'action':"/blog/" + blog_id + "/edit/",
    })

    #return HttpResponse(response % question_id)

