from django.db import models
from django.urls import reverse

"""
#=============================Наполнение странички контентом=========================================
#===========================================Content==================================================
"""
class Content(models.Model):
    """
    title = Первый заголловок (тот что обычно отображается сверху)
    titlex = Второй заголловок (тот что обычно отображается ниже и содержит смысловое слово)
    content = Описание работ которые подразумеваются
    photo = Набор изображений которые подтягиваются на страничку (оформление сайта)
    time_create = дата создания
    is_published = опубликован или нет (можно загрузить но не публиковать или публиковать с отсрочкой)
    cat = к какой категории привязан контент (тут внимательно почитай информацию по наполнению
            есть валидация и есть ограничения по изображениям)

    """
    title = models.CharField(max_length=50, verbose_name="Заголовок")
    titlex = models.CharField(max_length=50, verbose_name="Заголовок 2")
    content = models.TextField(blank=True, verbose_name="Сатья")
    photo_b = models.ImageField(blank=True ,upload_to="content/photos_big/%Y/%m/%d/")
    photo_l = models.ImageField(blank=True ,upload_to="content/photos_large/%Y/%m/%d/")
    photo_s = models.ImageField(blank=True ,upload_to="content/photos_small/%Y/%m/%d/")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('CategoryContent', on_delete=models.PROTECT, null=True)
    url = models.URLField(blank=True, verbose_name="ссылка")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Контент'
        verbose_name_plural = 'Контент'
        ordering = ['time_create', 'title']

    def get_absolute_url(self):
        return reverse('single', kwargs={'single_id': self.pk})


class CategoryContent(models.Model):
    name = models.CharField(max_length=255, db_index=True, verbose_name="Категория")


    def __str__(self):
        return self.name


    class Meta:
        verbose_name = 'Категории контента'
        verbose_name_plural = 'Категории контента'



"""    
#=======================================End Content==================================================
"""
"""
#================================Услуги и стоимость работ=============================================
"""
#
# class Jobs(models.Model):
#     title = models.CharField(max_length=50, verbose_name="Заголовок")
#     titlex = models.CharField(max_length=50, verbose_name="Заголовок 2")
#     content = models.TextField(blank=True, verbose_name="Сатья")
#     photo_b = models.ImageField(upload_to="content/photos_big/%Y/%m/%d/")
#     photo_l = models.ImageField(upload_to="content/photos_large/%Y/%m/%d/")
#     photo_s = models.ImageField(upload_to="content/photos_small/%Y/%m/%d/")
#     time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
#     is_published = models.BooleanField(default=True, verbose_name="Публикация")
#     cat = models.ForeignKey('CategoryJobs', on_delete=models.PROTECT, null=True)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         verbose_name = 'Описание работ'
#         verbose_name_plural = 'Описание работ'
#         ordering = ['time_create', 'title']
#
#     def get_absolute_url(self):
#         return reverse('single', kwargs={'single_id': self.pk})
#
#
# class CategoryJobs(models.Model):
#     name = models.CharField(max_length=255, verbose_name="Категория")
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Категории работ'
#         verbose_name_plural = 'Категории работ'
#================================================================================================================


class UserForm(models.Model):
    name = models.CharField(max_length=255, verbose_name='Имя')
    phone_number = models.CharField(max_length=12, verbose_name='Номер телефона')
    car_number = models.CharField(max_length=8, verbose_name='Номер машины')
    message = models.TextField(max_length=500, verbose_name='Задайте вопрос или уточните время в какое вам перезвонить')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата заявки")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Клиенты'
        verbose_name_plural = 'клиенты'
        ordering = ['phone_number', 'car_number']
    #
    # def get_absolute_url(self):
    #     return reverse('UserForm', kwargs={'UserForm': self.pk})


