from django.db import models
from utils.utils import remove_html_tags


class Article(models.Model):
  id = models.AutoField(primary_key=True)
  position = models.IntegerField(null=True)
  create_at = models.DateTimeField(null=False)
  title = models.CharField(max_length=150, null=False, default="[Title not set]")
  category_list_json = models.CharField(max_length=1000, null=False, default="[]")
  content_html = models.CharField(max_length=10_000_000, null=False, default="<p>[Content not set]</p>")

  def __str__(self):
    return f"[{self.id}] {self.title} ({self.create_at})"
  
  def get_clear_text(self):
    return remove_html_tags(self.content_html)
  

class Comment(models.Model):
  article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
  send_at = models.DateTimeField(null=False)
  sender_name = models.CharField(max_length=150, null=False, default="[Anonim]")
  text = models.CharField(max_length=1000, null=False, default="[Text not set]")
  is_visible = models.BooleanField(null=False, default=True)

  def __str__(self):
    return f"{self.sender_name}: {self.text}"

