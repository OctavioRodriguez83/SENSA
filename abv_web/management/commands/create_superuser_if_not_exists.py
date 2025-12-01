# abv_web/management/commands/create_superuser_if_not_exists.py
import os
from dotenv import load_dotenv
from django.core.management.base import BaseCommand
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = "Crea un superusuario a partir de variables de entorno si no existe"

    def handle(self, *args, **kwargs):
        load_dotenv()  # Carga variables del archivo .env

        username = os.getenv("SUPERUSER_NAME")
        email = os.getenv("SUPERUSER_EMAIL")
        password = os.getenv("SUPERUSER_PASSWORD")
        first_name = os.getenv("SUPERUSER_FIRST_NAME")
        last_name = os.getenv("SUPERUSER_LAST_NAME")

        if not User.objects.exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )
            self.stdout.write(self.style.SUCCESS("✅ Superusuario creado exitosamente"))
        else:
            # Verifica si existe algún superusuario
            if not User.objects.filter(is_superuser=True).exists():
                User.objects.create_superuser(
                    username=username,
                    email=email,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                self.stdout.write(self.style.SUCCESS("✅ Superusuario creado exitosamente"))
            else:
                self.stdout.write(self.style.WARNING("⚠️ El superusuario ya existe"))