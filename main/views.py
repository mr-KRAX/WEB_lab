from django.shortcuts import render, redirect
from .models import Article, User, Like
from passlib.hash import pbkdf2_sha256
from django.http import HttpResponse
import json

# Create your views here.

from .forms import RegForm

def mainBoard(request):
  articles = Article.objects.all()
  res = []
  for art in articles:
    a={}
    a['id'] = art.id
    a['title'] = art.title
    a['text'] = art.text
    a['author'] = art.author
    a['likes'] = art.countLikes()
    res.append(a)
    # res += []
    # print(art.countLikes())
  print(res)
  return render(request, 'main/index.html', {'articles': res})

def login(request):
  if request.method == 'POST':
    nickname = request.POST['nickname']
    password = request.POST['password']
    user = User.objects.filter(pk=nickname)
    print(user)
    if user:
      if user[0].verify_password(password):
        User.last_authorized_user = user[0].nickname
        return redirect('home')

      return redirect('login')

  return render(request, 'main/login.html')

def registration(request):
  if request.method == 'POST':
    form = RegForm(request.POST)
    if form.is_valid():
      print("valid")
      new_user = form.save(commit=False)
      new_user.password = pbkdf2_sha256.encrypt(request.POST['password'], rounds=12000, salt_size=32)
      new_user.save()
      return redirect('login')
    return redirect('registration')
  
  return render(request, 'main/registration.html')
  # return render(request, 'main/login.html')

def likes(request, id):
  article = Article.objects.get(id=id)
  data = {"likes" : article.countLikes()}
  return HttpResponse(json.dumps(data), content_type="application/json")

authedUser = "User1"

def markLiked(request, id):
  user = User.objects.get(nickname=authedUser)


  if user:
    article = Article.objects.get(id=int(id))
    try:
      like = Like.objects.get(article=article, user=user)
      like.delete()
    except:
      like = Like(article=article, user=user)
      like.save()
  return likes(request, id)
  

def debug_info(request):
  data = {"user": User.objects.get(nickname=authedUser).nickname, 
          "count" : "-"}
  return HttpResponse(json.dumps(data), content_type="application/json")

  

