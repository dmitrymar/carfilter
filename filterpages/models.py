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
    display = models.BooleanField(default=True)
    year = models.PositiveSmallIntegerField(default=2016)

    MITS = 'Mitsubishi'
    SMRT = 'smart'
    CHEV = 'Chevrolet'
    VW = 'Volkswagen'
    NISS = 'Nissan'
    FORD = 'Ford'
    FIAT = 'FIAT'
    KIA = 'Kia'
    MB = 'Mercedes-Benz'
    BMW = 'BMW'
    TSLA = 'Tesla'
    MAKES = (
        (MITS, 'Mitsubishi'),
        (SMRT, 'smart'),
        (CHEV, 'Chevrolet'),
        (VW, 'Volkswagen'),
        (NISS, 'Nissan'),
        (FORD, 'Ford'),
        (FIAT, 'FIAT'),
        (KIA, 'Kia'),
        (MB, 'Mercedes-Benz'),
        (BMW, 'BMW'),
        (TSLA, 'Tesla'),
    )
    make = models.CharField(max_length=60,
                                      choices=MAKES,
                                      blank=True)

    model = models.CharField(max_length=60)

    SEDAN = 'Sedan'
    WAGON = 'Wagon'
    HATCHBACK = 'Hatchback'
    SUV = 'SUV'
    BODY_STYLES = (
        (SEDAN, 'Sedan'),
        (WAGON, 'Wagon'),
        (HATCHBACK, 'Hatchback'),
        (SUV, 'SUV'),
    )
    body = models.CharField(max_length=60,
                                      choices=BODY_STYLES,
                                      blank=True)
    FWD = 'front-wheel drive'
    RWD = 'rear-wheel drive'
    AWD = 'all-wheel drive'
    DRIVE_TYPES = (
        (FWD, 'front-wheel drive'),
        (RWD, 'rear-wheel drive'),
        (AWD, 'all-wheel drive'),
    )
    drive = models.CharField(max_length=60,
                                      choices=DRIVE_TYPES,
                                      blank=True)


    city_mpg = models.PositiveSmallIntegerField(blank=True, null=True)
    hwy_mpg = models.PositiveSmallIntegerField(blank=True, null=True)
    range = models.PositiveSmallIntegerField(blank=True, null=True)
    battery = models.PositiveSmallIntegerField(blank=True, null=True, default=0)
    motor = models.PositiveSmallIntegerField(blank=True, null=True)
    # battery = models.CommaSeparatedIntegerField(
    #     blank=True, max_length=255,
    # )
    power = models.CharField(max_length=255, default=0)
    torque = models.PositiveSmallIntegerField(blank=True, null=True)
    seats = models.PositiveSmallIntegerField(blank=True, null=True)
    version = models.CharField(max_length=60, blank=True)
    styles = models.PositiveSmallIntegerField(blank=True, null=True)
    lowest_price = models.PositiveIntegerField()
    zero_two_sixty = models.DecimalField(blank=True, null=True, max_digits=5, decimal_places=1)
    image_url = models.CharField(max_length=255)

    def get_page_path(self):
        pagepath = "/".join(["/overview", str(self.year), self.make, self.model, self.body, self.version])
        return pagepath

    # def __str__(self):
    #     field_values = []
    #     for field in self._meta.get_all_field_names():
    #         field_values.append(getattr(self, field, ''))
    #     return ' '.join(field_values)

    # def __str__(self):
    #     return '%s %s %s %s %s %s %s %s %s %s %s %s %s %s %s' % (self.year,
    #                                 self.city_mpg,
    #                                 self.hwy_mpg,
    #                                 self.range,
    #                                 self.battery,
    #                                 self.motor,
    #                                 self.power,
    #                                 self.torque,
    #                                 self.make.lower(),
    #                                 self.model.replace(" ", "-"),
    #                                 self.body,
    #                                 self.styles,
    #                                 self.lowest_price,
    #                                 self.image_url,
    #                                 self.get_page_path())
