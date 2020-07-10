from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

title_choices = [
    ('MG', 'Менеджер'),
    ('AD', 'Администратор'),
    ('ST', 'Персонал')
]

class UserManager(BaseUserManager):
    def create_user(self, username, email, job_title, first_name, last_name, works_for, property_id, password=None):
        if not username:
            raise ValueError('Вы должны выбрать #username')
        if not email:
            raise ValueError('Укажите адрес электронной почты')
        if not job_title:
            raise ValueError('Выберите вашу должность')
        if not first_name:
            raise ValueError('Укажите имя')
        if not last_name:
            raise ValueError('Укажите фамилию')
        if not works_for:
            raise ValueError('Укажите название вашего объекта размещения')
        
        user = self.model(
            email = self.normalize_email(email),
            username = username,
            job_title = job_title,
            first_name = first_name,
            last_name = last_name,
            works_for = works_for,
            property_id = property_id,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, job_title, first_name, last_name, works_for, property_id, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            job_title = job_title,
            first_name = first_name,
            last_name = last_name,
            works_for = works_for,
            property_id = property_id
        )

        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    job_title = models.CharField(max_length=2, choices=title_choices)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    works_for = models.CharField(max_length=100, help_text='Введите название вашего объекта размещения.')
    property_id = models.CharField(max_length=48, help_text='Введите 32-ти значную последовательность цифр и букв. Храните её в секрете, она служит для защиты')

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'job_title', 'first_name', 'last_name', 'works_for', 'property_id']

    objects = UserManager()

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def has_perm(self, perm, obj=None):
        return self.is_admin
    
    def has_module_perms(self, app_label):
        return True

class PropertyIdentifier(models.Model):
    identifier = models.CharField(max_length=88)