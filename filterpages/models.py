from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title

class Carmodel(models.Model):
    year = models.PositiveSmallIntegerField(default=2016)
    make = models.CharField(max_length=60)
    model = models.CharField(max_length=60)
    body_type = models.CharField(max_length=60, default='sedan')
    styles = models.PositiveSmallIntegerField(default=1)
    lowest_price = models.PositiveIntegerField()
    image_url = models.CharField(max_length=100)

    def get_page_path(self):
        pagepath = "/".join(["/overview", str(self.year), self.make, self.model, self.body_type])
        return pagepath

    def get_thumb_url(self):
        thumb_path = "".join(["http://media.ed.edmunds-media.com/", self.image_url, "276.jpg"])
        return thumb_path

    def __str__(self):
        return '%s %s %s %s %s %s %s' % (self.year,
                                    self.make,
                                    self.model,
                                    self.styles,
                                    self.lowest_price,
                                    self.get_page_path(),
                                    self.get_thumb_url())
