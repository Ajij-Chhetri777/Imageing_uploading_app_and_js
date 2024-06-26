from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from theapp.models import Thepost, Type, Comment, Like, Reply
from theapp.forms import PostForm, RegisterForm, LoginForm, CommentForm, ReplyForm
from django.db.models import Q
# Create your views here.
def home(request):
    posts = Thepost.objects.all()
    search = request.GET.get('search')
    if search != None:
        posts = Thepost.objects.filter(title__icontains = search)
    form = PostForm()
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            image_object = form.instance
            obj = form.save(commit=False)
            obj.user = request.user
            obj.save()
            return redirect('home')
    context = {'posts':posts,'form':form }
    return render(request,'home.html',context)


def get_view(request,id):
    objects = get_object_or_404(Thepost,id = id )
    com = get_object_or_404(Comment,id =id)
    form = CommentForm()
    replys = ReplyForm()
    if request.method == "POST":
        button = request.POST['submitButton']
        if button == "comment":
             form = CommentForm(request.POST)
             if form.is_valid():
                 new_comment = form.save(commit=False)
                 new_comment.user = request.user
                 new_comment.belong_to = objects
                 new_comment.save()
                 return redirect('get_view',id = objects.id)
        elif button == "reply":
            replys = ReplyForm(request.POST)
            if replys.is_valid():
                new_replys = form.save(commit= False)
                new_replys.user = request.user


                new_replys.save()
                return redirect('get_view',id = objects)
    comments =  Comment.objects.filter(belong_to = objects)
    reply = Reply.objects.all() 
    counts = Comment.objects.filter(belong_to = objects).count()
    context = { 'objects':objects, 'form':form, 'comments':comments, 'count':counts , 'reply':reply ,'replys':replys }
    return render(request,'view_object.html',context)

def register(request):
    form =  RegisterForm()

    if request.method == "POST":
       form = RegisterForm(request.POST)
       if form.is_valid():
           user = form.save()
           login(request,user)
           return redirect('home')
    context ={'form':form}
    return render(request,'register.html',context)

def logins(request):
    form = LoginForm()
    if request.method == "POST":
        form = LoginForm(request.POST)
        username = request.POST['name']
        password = request.POST['password']
        user = authenticate(request,username = username , password = password)
        if user is not None:
                login(request,user)
                return redirect('home')
    context = {'form': form}
    return render(request,'login.html',context)
def liked(request):
    pass #prashan ko try nagaram alli high  level ko cha

def replycomment(request,id ):
    init_comment = get_object_or_404(Comment,id = id)
    replys = ReplyForm()
    if request.method == 'POST':
        replys = ReplyForm(request.POST)
        if replys.is_valid():
            rep = replys.save(commit= False)
            rep.user = request.user
            rep.initial_comment = init_comment
            rep.save()

        return redirect('home')
