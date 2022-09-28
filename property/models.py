from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    created_at = models.DateTimeField(
        verbose_name='Когда создано объявление',
        default=timezone.now,
        db_index=True,
    )
    description = models.TextField(
        verbose_name='Текст объявления',
        blank=True,
    )
    price = models.IntegerField(
        verbose_name='Цена квартиры',
        db_index=True,
    )
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True,
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
    )
    address = models.TextField(
        verbose_name='Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4',
    )
    new_building = models.BooleanField(
        verbose_name='Новостройка',
        db_index=True,
        null=True,
    )
    floor = models.CharField(
        verbose_name='Этаж',
        help_text='Первый этаж, последний этаж, пятый этаж',
        max_length=3,

    )
    rooms_number = models.IntegerField(
        verbose_name='Количество комнат в квартире',
        db_index=True,
    )
    living_area = models.IntegerField(
        verbose_name='Количество жилых кв.метров',
        blank=True,
        db_index=True,
        null=True,
    )
    has_balcony = models.BooleanField(
        verbose_name='Наличие балкона',
        db_index=True,
        default=None,
        null=True,
    )
    active = models.BooleanField(
        verbose_name='Активно-ли объявление',
        db_index=True,
    )
    construction_year = models.IntegerField(
        verbose_name='Год постройки здания',
        blank=True,
        db_index=True,
        null=True,

    )
    liked_by = models.ManyToManyField(
        User,
        verbose_name='Кому понравилось',
        related_name='liked_flats',
        blank=True,
    )

    class Meta:
        verbose_name = 'квартиру'
        verbose_name_plural = 'Квартиры'

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Complaint(models.Model):
    user = models.ForeignKey(
        User,
        verbose_name='Кто жаловался',
        on_delete=models.SET_NULL,
        null=True,
        related_name='complaints',
    )
    flat = models.ForeignKey(
        Flat,
        verbose_name='Квартира',
        on_delete=models.CASCADE,
        related_name='complaints',
    )
    text = models.TextField(
        verbose_name='Жалоба',
    )

    class Meta:
        verbose_name = 'жалобу'
        verbose_name_plural = 'Жалобы'

    def __str__(self):
        return f'{self.user} жалуется на квартиру: {self.flat}.'


class Owner(models.Model):
    name = models.CharField(
        verbose_name='ФИО',
        max_length=200,
        db_index=True,
    )
    phonenumber = PhoneNumberField(
        verbose_name='Телефон',
        blank=True,
        db_index=True,
        region='RU',
    )
    flats = models.ManyToManyField(
        Flat,
        verbose_name='Квартиры в собственности',
        blank=True,
        db_index=True,
        related_name='owners',
    )

    class Meta:
        verbose_name = 'собственника'
        verbose_name_plural = 'Собственники'

    def __str__(self):
        return f'Собственник {self.name} тел. {self.phonenumber}'
