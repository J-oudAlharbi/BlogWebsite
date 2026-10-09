from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.models import User
from .models import Post, Comment, Category


def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())


def users(request):
    myusers = User.objects.all()
    template = loader.get_template('users.html')
    context = {'myusers': myusers}
    return HttpResponse(template.render(context, request))


def blogs(request):
    myblogs = Post.objects.all()
    template = loader.get_template('blogs.html')
    context = {'myblogs': myblogs}
    return HttpResponse(template.render(context, request))


def blogdetails(request, id):
    myblog = Post.objects.get(id=id)
    template = loader.get_template('blogdetails.html')
    context = {'myblog': myblog}
    return HttpResponse(template.render(context, request))


def comments(request):
    mycomments = Comment.objects.all()
    template = loader.get_template('comments.html')
    context = {'mycomments': mycomments}
    return HttpResponse(template.render(context, request))


def categories(request):
    mycategories = Category.objects.all()
    template = loader.get_template('categories.html')
    context = {'mycategories': mycategories}
    return HttpResponse(template.render(context, request))