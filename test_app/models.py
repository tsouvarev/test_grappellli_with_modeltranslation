from django.db import models


class Tag(models.Model):
    name = models.CharField(max_length=255)

    @staticmethod
    def autocomplete_search_fields():
        # return ['name_en__icontains']
        return ['name__icontains']
