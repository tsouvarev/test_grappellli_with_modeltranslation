from modeltranslation.translator import translator, TranslationOptions

from .models import Tag


class TagTranslationOptions(TranslationOptions):
    fields = ('name',)

translator.register(Tag, TagTranslationOptions)
