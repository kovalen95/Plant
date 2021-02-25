from django.db import models
from django.conf import settings


class NameDescriptionMixin(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150, blank=True, default="")

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class UserMixin(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    class Meta:
        abstract = True


class ImageMixin(models.Model):
    image_url = models.URLField(blank=True, default="")

    class Meta:
        abstract = True


class Category(UserMixin, NameDescriptionMixin, ImageMixin, models.Model):
    # SlugField - Łamiąca Wiadomość -> lamiaca-wiadomosc
    slug = models.SlugField(unique=True)


class Plant(UserMixin, NameDescriptionMixin, models.Model):
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    watering_interval = models.PositiveIntegerField(help_text="in seconds")
    fertilizing_interval = models.PositiveIntegerField(help_text="in seconds")
    EXPOSURE_CHOICES = [
        ("dark", "Dark"),
        ("shade", "Shade"),
        ("partsun", "Part Sun"),
        ("fullsun", "Full Sun"),
    ]
    required_exposure = models.CharField(
        max_length=10,
        verbose_name="Amount of sun",
        choices=EXPOSURE_CHOICES
    )
    HUMIDITY_CHOICES = [
        ("low", "Low"),
        ("medium", "Medium"),
        ("high", "High"),
    ]
    required_humidity = models.CharField(
        max_length=10,
        choices=HUMIDITY_CHOICES
    )
    TEMPERATURE_CHOICES = [
        ("cold", "Cold"),
        ("medium", "Medium"),
        ("warm", "Warm"),
    ]
    required_temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURE_CHOICES
    )
    blooming = models.BooleanField(
        default=False,
        blank=True,
        null=False,
        verbose_name="blooming?"
    )
    DIFFICULTY_CHOICES = [
        (1, "low"),
        (2, "medium low"),
        (3, "medium"),
        (4, "medium high"),
        (5, "high"),
    ]
    difficulty = models.PositiveIntegerField(
        default=1,
        verbose_name="Cultivation difficulty level",
        choices=DIFFICULTY_CHOICES
    )


class Room(UserMixin, NameDescriptionMixin, models.Model):
    EXPOSURE_CHOICES = Plant.EXPOSURE_CHOICES
    exposure = models.CharField(
        max_length=10,
        verbose_name="Amount of sun",
        choices=EXPOSURE_CHOICES
    )
    HUMIDITY_CHOICES = Plant.HUMIDITY_CHOICES
    humidity = models.CharField(
        max_length=10,
        choices=HUMIDITY_CHOICES
    )
    TEMPERATURE_CHOICES = Plant.TEMPERATURE_CHOICES
    temperature = models.CharField(
        max_length=10,
        choices=TEMPERATURE_CHOICES
    )
    drafty = models.BooleanField(
        default=False,
        blank=True,
        null=False,
        verbose_name="drafty?"
    )


class UserPlant(UserMixin, NameDescriptionMixin, ImageMixin, models.Model):
    room = models.ForeignKey(Room, on_delete=models.PROTECT)
    plant = models.ForeignKey(Plant, on_delete=models.PROTECT, verbose_name="Type of plant")
    last_watered = models.DateTimeField(null=True, blank=True, verbose_name="Timestamp of last watering")
    last_fertilized = models.DateTimeField(null=True, blank=True, verbose_name="Timestamp of last fertizing")
