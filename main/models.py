from django.db import models
from passlib.hash import pbkdf2_sha256

# Create your models here.

class User(models.Model):
  name = models.CharField('name', max_length=50)
  nickname = models.CharField('nickname', max_length=50, primary_key=True)
  email = models.EmailField('email', max_length=255)
  gender = models.CharField('gender', max_length=50)
  password = models.CharField('password', max_length=255, null=True)

  last_authorized_user = "none"
  def verify_password(self, raw_pass):
    return pbkdf2_sha256.verify(raw_pass, self.password)

  def __str__(self):
    return f'{self.nickname} (name: {self.name}, email: {self.email})'

  class Meta:
    verbose_name = "User"
    verbose_name_plural = "Users"

class Article(models.Model):
  id = models.PositiveIntegerField('id', primary_key=True)
  title = models.CharField('title', max_length=100)
  text = models.TextField('text')
  author = models.CharField('author', max_length=50)

  def __str__(self):
    return f'Article: {self.title}'
  
  def countLikes(self):
    return Like.objects.filter(article__title=self.title).count()

  class Meta:
    verbose_name = "Article"
    verbose_name_plural = "Articles"

class Like(models.Model):
  article = models.ForeignKey(Article, on_delete=models.DO_NOTHING)
  user = models.ForeignKey(User, on_delete=models.DO_NOTHING)

  def __str__(self):
    return f'like: {self.article.id} - {self.user.nickname}'