from datetime import date, timedelta

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from bugdemo.models import Report


class Command(BaseCommand):
    help = "Create a superuser and demo rows for the django-unfold filter bug."

    def handle(self, *args, **options):
        user_model = get_user_model()

        if not user_model.objects.filter(username="admin").exists():
            user_model.objects.create_superuser(
                username="admin",
                email="admin@example.com",
                password="admin",
            )
            self.stdout.write(self.style.SUCCESS("Created superuser admin/admin"))
        else:
            self.stdout.write("Superuser admin already exists")

        Report.objects.all().delete()

        today = date.today()
        Report.objects.bulk_create(
            [
                Report(
                    title="Current month row",
                    filter_date=today,
                    editable_date=today + timedelta(days=2),
                ),
                Report(
                    title="Previous month row",
                    filter_date=today - timedelta(days=40),
                    editable_date=today - timedelta(days=10),
                ),
                Report(
                    title="Another current month row",
                    filter_date=today + timedelta(days=5),
                    editable_date=today + timedelta(days=7),
                ),
            ]
        )

        self.stdout.write(self.style.SUCCESS("Seeded demo data"))
