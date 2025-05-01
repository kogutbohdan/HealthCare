from django.core.management.base import BaseCommand
from ...models import Tasks
from registretion.models import MyUser

class Command(BaseCommand):
    help = 'Повертає таски користувачам кожного дня'

    def handle(self, *args, **kwargs):
        tasks = Tasks.objects.all()
        users=MyUser.objects.all()
        for user in users:
            for task in tasks:
                user.tasks.add(task)
        self.stdout.write(self.style.SUCCESS('Таски успішно оновлені!'))
