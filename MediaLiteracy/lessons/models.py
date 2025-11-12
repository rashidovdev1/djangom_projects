from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True, null=True)
    video_url = models.URLField(help_text="YouTube video linkini kiriting")
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='lessons')
    created_at = models.DateTimeField(auto_now_add=True)

    def embed_url(self):
        """YouTube linkni iframe uchun tayyor formatga o‘giradi"""
        return self.video_url.replace("watch?v=", "embed/")

    def __str__(self):
        return self.title
