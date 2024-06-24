from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наиминование категории")
    description = models.TextField(verbose_name="Описание категории")

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Наиминование продукта")
    description = models.TextField(verbose_name="Описание продукта")
    photo = models.ImageField(
        upload_to="Product/photo", blank=True, null=True, verbose_name="Фото"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        null=True,
        blank=True,
        related_name="Product",
    )
    price = models.IntegerField(verbose_name="Цена")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ["name", "description"]

    def __str__(self):
        return self.name