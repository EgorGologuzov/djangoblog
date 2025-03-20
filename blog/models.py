from django.db import models
from utils.utils import remove_html_tags


class Article(models.Model):
  id = models.AutoField(primary_key=True)
  position = models.IntegerField(blank=True, default=0)
  create_at = models.DateTimeField(auto_now_add=True, blank=True, null=False)
  title = models.CharField(max_length=150, null=False, default="[Title not set]")
  category_list_json = models.CharField(max_length=1000, null=False, default="[]")
  avatar = models.CharField(max_length=200, blank=True, null=True, default=None)
  content_html = models.FileField(upload_to='articles', null=True, blank=False)
  content_preview = models.CharField(max_length=200, blank=True)
  is_visible = models.BooleanField(null=False, default=True)

  __content_html_text__ = None

  def __str__(self):
    return f"[{self.id}] {self.title} ({self.create_at})"
  
  @property
  def content_html_text(self):
    if self.__content_html_text__:
      return self.__content_html_text__

    if self.content_html:
      with open(self.content_html.path, 'r', encoding='utf-8') as f:
        self.__content_html_text__ = f.read()
        return self.__content_html_text__
      
    return None
  
  def save(self, *args, **kwargs):
    super(Article, self).save(*args, **kwargs)

    if not self.content_preview and self.content_html_text:
      self.content_preview = remove_html_tags(self.content_html_text)[:100]
      
    super(Article, self).save(*args, **kwargs)
  

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  send_at = models.DateTimeField(auto_now_add=True, blank=True, null=False)
  sender_name = models.CharField(max_length=150, null=False, default="[Anonim]")
  text = models.CharField(max_length=1000, null=False, default="[Text not set]")
  is_visible = models.BooleanField(null=False, default=True)

  def __str__(self):
    return f"{self.sender_name}: {self.text}"
  

class Image(models.Model):
  name = models.CharField(max_length=200, blank=True, null=True)
  file = models.ImageField(upload_to='images', null=False)

  def __str__(self):
    return f"{self.name} ({self.file.url})"

