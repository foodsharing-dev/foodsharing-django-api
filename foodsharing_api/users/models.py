import hashlib

from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager
from django.db import models
from django.utils.deprecation import CallableFalse, CallableTrue


class User(models.Model):
    bezirk_id = models.IntegerField(default=0)
    position = models.CharField(max_length=255)
    verified = models.IntegerField(default=0)
    last_pass = models.DateTimeField(null=True)
    new_bezirk = models.CharField(max_length=120)
    want_new = models.IntegerField(default=0)
    mailbox_id = models.IntegerField(null=True)
    rolle = models.IntegerField(default=0)
    type = models.IntegerField(blank=True, null=True)
    zip = models.CharField(max_length=10, blank=True, null=True, db_column='plz')
    city = models.CharField(max_length=100, blank=True, null=True, db_column='stadt')
    lat = models.CharField(max_length=20, blank=True, null=True)
    lon = models.CharField(max_length=20, blank=True, null=True)
    photo = models.CharField(max_length=50, blank=True, null=True)
    photo_public = models.IntegerField(default=0)
    email = models.CharField(unique=True, max_length=120, blank=True, null=True)
    passwd = models.CharField(max_length=32, blank=True, null=True)
    first_name = models.CharField(max_length=120, blank=True, null=True, db_column='name')
    admin = models.IntegerField(blank=True, null=True)
    last_name = models.CharField(max_length=120, blank=True, null=True, db_column='nachname')
    address = models.CharField(max_length=120, blank=True, null=True, db_column='anschrift')
    phone = models.CharField(max_length=30, blank=True, null=True, db_column='telefon')
    tox = models.CharField(max_length=255, blank=True, null=True)
    homepage = models.CharField(max_length=255, blank=True, null=True)
    github = models.CharField(max_length=255, blank=True, null=True)
    twitter = models.CharField(max_length=255, blank=True, null=True)
    mobile = models.CharField(max_length=50, blank=True, null=True, db_column='handy')
    geschlecht = models.IntegerField(blank=True, null=True)
    geb_datum = models.DateField(blank=True, null=True)
    anmeldedatum = models.DateTimeField(blank=True, null=True)
    orgateam = models.IntegerField(blank=True, null=True)
    active = models.IntegerField(default=0)
    data = models.TextField()
    about_me_public = models.TextField()
    newsletter = models.IntegerField(blank=True, null=True)
    token = models.CharField(max_length=25)
    infomail_message = models.IntegerField(default=0)
    last_login = models.DateTimeField(blank=True, null=True)
    stat_fetchweight = models.DecimalField(max_digits=7, decimal_places=2, default=0)
    stat_fetchcount = models.IntegerField(default=0)
    stat_ratecount = models.IntegerField(default=0)
    stat_rating = models.DecimalField(max_digits=4, decimal_places=2, default=0)
    stat_postcount = models.IntegerField(default=0)
    stat_buddycount = models.IntegerField(default=0)
    stat_bananacount = models.IntegerField(default=0)
    stat_fetchrate = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    sleep_status = models.IntegerField(default=0)
    sleep_from = models.DateField(null=True)
    sleep_until = models.DateField(null=True)
    sleep_msg = models.TextField(null=True)
    option = models.TextField(default='')
    beta = models.IntegerField(default=0)
    fs_password = models.CharField(max_length=50, blank=True, null=True)
    quiz_rolle = models.IntegerField(default=0)
    contact_public = models.IntegerField(default=0)
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
    def is_staff(self):
        return self.admin

    @property
    def is_active(self):
        return self.active > 0

    REQUIRED_FIELDS=[]
    USERNAME_FIELD='email'

    class Meta:
        managed = False
        db_table = 'fs_foodsaver'

    def hash_password(self, raw_password):
        salted_password = self.email.lower() + '-lz%&lk4-' + raw_password
        hashed = hashlib.md5(salted_password.encode()).hexdigest()
        return hashed

    def check_password(self, raw_password):
        return self.passwd == self.hash_password(raw_password)

    def set_password(self, raw_password):
        self.passwd = self.hash_password(raw_password)
        self.save()

    def __str__(self):
        return self.first_name