from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from .models import Tag


class TagAdmin(TranslationAdmin):
    pass


admin.site.register(Tag, TagAdmin)
