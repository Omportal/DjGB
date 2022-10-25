from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model



class News(models.Model):
    title = models.CharField(max_length=256, verbose_name="Заголовок")
    preambule = models.CharField(max_length=256)
    body = models.TextField(verbose_name="Описание")
    body_as_markdown = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    updated = models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"

    def __str__(self) -> str:
        return self.title


class Courses(models.Model):
    name=models.CharField(max_length=256, verbose_name="Заголовок")
    description=models.TextField(verbose_name="Описание")
    description_as_markdown=models.BooleanField(default=False)
    cost=models.DecimalField(max_digits=12, decimal_places=2, verbose_name="Цена")
    cover=models.URLField()
    created=models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    updated=models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Курс"
        verbose_name_plural = "Курсы"

    def __str__(self) -> str:
        return self.name



class Lesson(models.Model):
    course = models.ForeignKey(Courses, related_name="lesson",on_delete=models.CASCADE, verbose_name='Курс')
    num = models.PositiveIntegerField()
    title=models.CharField(max_length=256, verbose_name="Заголовок")
    description=models.TextField(verbose_name="Описание")
    description_as_markdown=models.BooleanField(default=False)
    created=models.DateTimeField(auto_now_add=True, verbose_name="Дата Создания")
    updated=models.DateTimeField(auto_now=True, verbose_name="Дата изменения")

    class Meta:
        verbose_name = "Урок"
        verbose_name_plural = "Уроки"

    def __str__(self) -> str:
        return self.title


class CourseTeachers(models.Model):
    name_first = models.CharField(max_length=256, verbose_name="Имя")
    name_second = models.CharField(max_length=256, verbose_name="Фамилия")
    day_birth = models.DateField(verbose_name="Дата рождения")
    course = models.ManyToManyField(to=Courses, related_name='teacher')

    class Meta:
        verbose_name = "Учитель"
        verbose_name_plural = "Учителя"

    def __str__(self) -> str:
        return f"{self.name_first} {self.name_second}"

class CourseFeedback(models.Model):
    RATING = ((5, "⭐⭐⭐⭐⭐"), (4, "⭐⭐⭐⭐"), (3, "⭐⭐⭐"), (2, "⭐⭐"),
    (1, "⭐"))
    course = models.ForeignKey(
    Courses, on_delete=models.CASCADE, verbose_name="Course"
    )
    user = models.ForeignKey(
    get_user_model(), on_delete=models.CASCADE, verbose_name="User"
    )
    feedback = models.TextField(default="No feedback", verbose_name="Feedback")
    rating = models.SmallIntegerField(choices=RATING, default=5, verbose_name="Rating")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created")
    deleted = models.BooleanField(default=False)
    def __str__(self):
        return f"{self.course} ({self.user})"

