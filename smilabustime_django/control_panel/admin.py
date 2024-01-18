from django.contrib import admin

# Register your models here.
from .models import all_models

for model in all_models:
    admin.site.register(model)
