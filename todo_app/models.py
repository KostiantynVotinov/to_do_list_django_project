from django.utils import timezone
from django.db import models
from django.urls import reverse

def one_week_hence():
    """
    Функція, що повертає поточну дату і час, збільшені на один тиждень
    для встановлення дат виконання ToDoItem за замовчуванням..
    """
    return timezone.now() + timezone.timedelta(days=7)


class ToDoList(models.Model):
    """
    Модель для представлення списку ToDoList.
    """
    title = models.CharField(max_length=100, unique=True)

    def get_absolute_url(self):
        """
        Повертає URL для перегляду списку ToDoList.
        """
        return reverse("list", args=[self.id])

    def __str__(self):
        """
        Повертає рядок, що представляє заголовок списку ToDoList.
        """
        return self.title


class ToDoItem(models.Model):
    """
    Модель для представлення елементу ToDoItem.
    """
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    due_date = models.DateTimeField(default=one_week_hence)
    todo_list = models.ForeignKey(ToDoList, on_delete=models.CASCADE)

    def get_absolute_url(self):
        """
        Повертає URL для перегляду або редагування елементу ToDoItem.
        """
        return reverse(
            "item-update", args=[str(self.todo_list.id), str(self.id)]
        )

    def __str__(self):
        """
        Повертає рядок, що представляє заголовок і дату до якої треба виконати елемент ToDoItem.
        """
        return f"{self.title}: due {self.due_date}"

    class Meta:
        ordering = ["due_date"]

