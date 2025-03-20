from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Article, Category
from .forms import CommentForm
import datetime
import json


def index(request):
  category = request.GET.get('category', None)
  categories = Category.objects.order_by('name')

  query = Article.objects.filter(is_visible=True).order_by('position', '-create_at')
  query = query if category is None else query.filter(category_list_json__icontains=f'"{category}"')
  page = request.GET.get('page', 1)
  paginator = Paginator(query, 4)
  pages_nums = [i for i in range(1, paginator.num_pages + 1)]
  articles = paginator.get_page(page)

  context = {'articles': articles, 'pages_nums': pages_nums, 'categories': categories, 'category': category}

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

  categories = json.loads(found_article.category_list_json) if found_article else None

  context = {'article': found_article, 'comments': comments, 'form': form, 'categories': categories}

  return render(request, 'blog/article-view.html', context)

