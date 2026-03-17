from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse
import logging
from .models import Post, AboutUs
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm

# Create your views here.

# Demo datas
# posts = [
#     {'id': 1, 'title': 'Post 1', 'content': 'Content of Post 1'},
#     {'id': 2, 'title': 'Post 2', 'content': 'Content of Post 2'},
#     {'id': 3, 'title': 'Post 3', 'content': 'Content of Post 3'},
#     {'id': 4, 'title': 'Post 4', 'content': 'Content of Post 4'},
# ]


def index(request):
    blog_title = 'Latest Posts'

   # get data from post model
    all_posts = Post.objects.all()

    # pagination
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'index.html', {'blog_title': blog_title, 'page_obj': page_obj})


def detail(request, slug):
    # return HttpResponse(f'detail page: {post_id}')
    # post = next((item for item in posts if item['id'] == int(post_id)), None)

    try:
        post = Post.objects.get(slug=slug)
        related_posts = Post.objects.filter(
            category=post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404('Post does not exist')

    # logger = logging.getLogger('TEST')
    # logger.debug(f'post variable {post}')
    return render(request, 'detail.html', {'post': post, 'related_posts': related_posts})


def oldUrlRedirect(request):
    return redirect(reverse('blog:newUrl'))


def newUrlView(request):
    return HttpResponse(f'this is the new URL')


def contactView(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger('TEST')

        # form.cleaned_data['name']

        if form.is_valid():
            logger.debug(f'post data {form.cleaned_data['name']}, {form.cleaned_data['email']}, {form.cleaned_data['message']}')
            successMessage = 'Your mail has been sent!'
            return render(request, 'contact.html', {'form': form, 'successMessage': successMessage})
                
        else:
            logger.debug(f'Form validation failure')
        return render(request, 'contact.html', {'form': form, 'name': name, 'email': email, 'message': message})

    return render(request, 'contact.html')


# def contactView(request):
#     logger = logging.getLogger('TEST')

#     successMessage = None
#     form = ContactForm()

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             logger.debug(form.cleaned_data)

#             successMessage = 'Your mail has been sent!'
#             form = ContactForm()  # reset form

#         else:
#             logger.debug('Form validation failure')

#     return render(request, 'contact.html', {
#         'form': form,
#         'successMessage': successMessage
#     })




# def contactView(request):
#     logger = logging.getLogger('TEST')

#     if request.method == 'POST':
#         form = ContactForm(request.POST)

#         if form.is_valid():
#             logger.debug(form.cleaned_data)

#             request.session['successMessage'] = 'Your mail has been sent!'
#             return redirect('blog:contact')  # redirect to same page

#         else:
#             logger.debug('Form validation failure')

#     else:
#         form = ContactForm()

#     successMessage = request.session.pop('successMessage', None)

#     return render(request, 'contact.html', {
#         'form': form,
#         'successMessage': successMessage
#     })

def aboutView(request):
    aboutContent = AboutUs.objects.first().content
    return render(request, 'about.html', {'aboutContent': aboutContent})
    