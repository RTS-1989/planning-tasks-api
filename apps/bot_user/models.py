from django.db import models


class BotUser(models.Model):
    surname = models.CharField(verbose_name="Фамилия", max_length=50)
    first_name = models.CharField(verbose_name="имя", max_length=50)
    patronymic = models.CharField(verbose_name="Отчество", max_length=50, null=True, blank=True)
    is_active = models.BooleanField(verbose_name="Активен", default=True)
    email = models.EmailField(verbose_name="Электронная почта", null=True, blank=True)
    birthday = models.DateField(verbose_name="День рождения", null=True, blank=True)

    class Meta:
        verbose_name = "Пользователь бота"
        verbose_name_plural = "Пользователи бота"

    @property
    def full_name(self) -> str:
        _full_name = f"{self.surname} {self.first_name}"
        if self.patronymic is not None:
            _full_name = f"{_full_name} {self.patronymic}"
        return _full_name

    def __str__(self):
        return self.full_name
