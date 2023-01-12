from django.db import models

class Category(models.Model):
    category_name = models.CharField(verbose_name="カテゴリ名", max_length=100)

    def __str__(self):
        return self.category_name

    class Meta:
        verbose_name = "カテゴリテーブル"
        verbose_name_plural = "カテゴリテーブル"

class Blog(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="タイトル", max_length=200)
    image = models.ImageField(verbose_name="画像", upload_to='', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "ブログテーブル"
        verbose_name_plural = "ブログテーブル"