from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='categories_pics', default='default_cat_img.png')
    description = models.CharField(blank=True, max_length=1000)
    slug = models.SlugField(unique=True, blank=True)

    objects = models.Manager()

    def __str__(self):
        return self.name

    @property
    def meals_by_cat(self):
        return Meal.objects.filter(category=self.pk)

    def save(self, *args, **kwargs):
        if not self.id:     # This line verifies id value is not None or 0,
                            # then it will generate the slug if only it's new object and not in update cases
            self.slug = slugify(self.name)      # It will slugify the name of Category
        super().save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "categories"


class Meal(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='meals_pics', default='default_meal_img.png')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    description = models.CharField(blank=True, max_length=1000)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(Category, related_name="products", on_delete=models.CASCADE)

    objects = models.Manager()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('meal_details', args=[self.pk, self.slug])

    def save(self, *args, **kwargs):
        if not self.id:     # This line verifies id value is not None or 0,
                            # then it will generate the slug if only it's new object and not in update cases
            self.slug = slugify(self.name)      # It will slugify the name of Category
        super().save(*args, **kwargs)

    class Meta:
        ordering = ('name',)    # This defines how we can order Meals
