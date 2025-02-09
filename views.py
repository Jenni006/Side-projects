from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
from django.views.decorators.csrf import ensure_csrf_cookie

# Create your views here.
'''posts = [ 
    {"id":1, "Title": "Post 1", "Content":"Content of Post 1"},
    {"id":2, "Title": "Post 2", "Content":"Content of Post 2"},
    {"id":3, "Title": "Post 3", "Content":"Content of Post 3"},
    {"id":4, "Title": "Post 4", "Content":"Content of Post 4"}
]'''
def index(request):
    blog_title = "Latest Posts"
    
    #getting all posts
    all_posts = Post.objects.all()

    #paginate
    paginator = Paginator(all_posts, 5)
    page_no = request.GET.get('page')
    page_obj = paginator.get_page(page_no)
    return render(request,'blogs/index.html', {"id":id,'blog_title':blog_title, "page_obj": page_obj}) 

def details(request,slug): 
    try:
        post = Post.objects.get(slug = slug)
        related_posts = Post.objects.filter(category = post.category).exclude(pk = post.id)
    except Post.DoesNotExist:
        raise Http404("Post Does Not Exist!")
    
    return render(request,'blogs/details.html',{'post':post, 'related_posts': related_posts})

def old_url_redirect(request):
    return redirect(reverse('blog:new_page_url'))

def new_url_view(request):
    return HttpResponse("This is the new URL") 

from django.shortcuts import render
from django.http import HttpResponse

@ensure_csrf_cookie
def contact_view(request):
    success_message = None
    if request.method =='POST':
        form = ContactForm(request.POST)
        logger = logging.getLogger("TESTING")
        
        if form.is_valid():
            logger.debug(f"POST Data is {form.cleaned_data['name']} {form.cleaned_data['email']} {form.cleaned_data['message']}")
            success_message = "Your email hass been sent!"
        else:
            logger.debug("Form validation failure")
    else:
        form = ContactForm() 
    return render(request, 'blogs/contact.html',{"form":form, "success_message": success_message}) 

def about_view(request):
    return render(request, 'blogs/about.html') 
