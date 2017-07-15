import hashlib

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.contrib.auth.models import UserManager
from django.db import models
from django.utils.deprecation import CallableFalse, CallableTrue


class FsFoodsaver(models.Model):
    bezirk_id = models.IntegerField()
    position = models.CharField(max_length=255)
    verified = models.IntegerField()
    last_pass = models.DateTimeField()
    new_bezirk = models.CharField(max_length=120)
    want_new = models.IntegerField()
    mailbox_id = models.IntegerField()
    rolle = models.IntegerField()
    type = models.IntegerField(blank=True, null=True)
    plz = models.CharField(max_length=10, blank=True, null=True)
    stadt = models.CharField(max_length=100, blank=True, null=True)
    lat = models.CharField(max_length=20, blank=True, null=True)
    lon = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    photo_public = models.IntegerField()
    email = models.CharField(unique=True, max_length=120, blank=True, null=True)
    passwd = models.CharField(max_length=32, blank=True, null=True)
    name = models.CharField(max_length=120, blank=True, null=True)
    admin = models.IntegerField(blank=True, null=True)
    nachname = models.CharField(max_length=120, blank=True, null=True)
    anschrift = models.CharField(max_length=120, blank=True, null=True)
    telefon = models.CharField(max_length=30, blank=True, null=True)
    tox = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    handy = models.CharField(max_length=50, blank=True, null=True)
    geschlecht = models.IntegerField(blank=True, null=True)
    geb_datum = models.DateField(blank=True, null=True)
    anmeldedatum = models.DateTimeField(blank=True, null=True)
    orgateam = models.IntegerField(blank=True, null=True)
    active = models.IntegerField()
    data = models.TextField()
    about_me_public = models.TextField()
    newsletter = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=25)
    infomail_message = models.IntegerField()
    last_login = models.DateTimeField(blank=True, null=True)
    stat_fetchweight = models.DecimalField(max_digits=7, decimal_places=2)
    stat_fetchcount = models.IntegerField()
    stat_ratecount = models.IntegerField()
    stat_rating = models.DecimalField(max_digits=4, decimal_places=2)
    stat_postcount = models.IntegerField()
    stat_buddycount = models.IntegerField()
    stat_bananacount = models.IntegerField()
    stat_fetchrate = models.DecimalField(max_digits=6, decimal_places=2)
    sleep_status = models.IntegerField()
    sleep_from = models.DateField()
    sleep_until = models.DateField()
    sleep_msg = models.TextField()
    last_mid = models.DateField()
    option = models.TextField()
    beta = models.IntegerField()
    fs_password = models.CharField(max_length=50, blank=True, null=True)
    quiz_rolle = models.IntegerField()
    contact_public = models.IntegerField()
    deleted_at = models.DateTimeField(blank=True, null=True)

    objects = BaseUserManager()

    @property
    def is_anonymous(self):
        """
        Always return False. This is a way of comparing User objects to
        anonymous users.
        """
        return CallableFalse

    @property
    def is_authenticated(self):
        """
        Always return True. This is a way to tell if the user has been
        authenticated in templates.
        """
        return CallableTrue

    @property
    def is_active(self):
        return self.active > 0

    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'

    class Meta:
        managed = False
        db_table = 'fs_foodsaver'

    def check_password(self, raw_password):
        salted_password = self.email.lower() + '-lz%&lk4-' + raw_password
        hashed = hashlib.md5(salted_password.encode()).hexdigest()
        return self.passwd == hashed

    def __str__(self):
        return self.name