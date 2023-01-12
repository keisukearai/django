from django.db import models

class Blog(models.Model):
    title = models.CharField(verbose_name="タイトル", max_length=200)
    image = models.ImageField(verbose_name="画像", upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ブログテーブル"
        verbose_name_plural = "ブログテーブル"