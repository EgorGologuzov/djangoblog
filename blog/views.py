from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from .models import Article, Comment
from .forms import CommentForm
import datetime


def index(request):
  query = Article.objects.order_by('position', '-create_at')

  page = request.GET.get('page', 1)
  paginator = Paginator(query, 4)
  pages_nums = [i for i in range(1, paginator.num_pages + 1)]
  articles = paginator.get_page(page)

  context = {'articles': articles, 'pages_nums': pages_nums}

  return render(request, 'blog/articles-list-view.html', context)


def article(request, id):
  try:
    found_article = Article.objects.get(id=id)
    comments = found_article.comments.filter(is_visible=True).order_by('-send_at')
  except:
    found_article = None
    comments = None

  if request.method == 'POST':
    form = CommentForm(request.POST)
    if form.is_valid():
      new_comment = form.save(commit=False)
      new_comment.article = found_article
      new_comment.send_at = datetime.datetime.now()
      new_comment.save()
  else:
    form = CommentForm()

  context = {'article': found_article, 'comments': comments, 'form': form}
  return render(request, 'blog/article-view.html', context)

