Test project to show issues for https://github.com/sehmaschine/django-grappelli/pull/738

This project has translated `Tag` model, with one `Tag` object with `name_en='en name'` and `name_de='de name'`. 
It also has `autocomplete_search_fields` returning `['name__icontains']`

So `grappelli` should be able to autocomplete tags by name (as `modeltranslation` rewrites queries, and `name` becomes `name_en`):

`http://localhost:8000/grappelli/lookup/autocomplete/?term=name&app_label=test_app&model_name=tag`

But it answers with zero results, however.

There are two ways to solve the problem:
- install patched `grappelli`, which doesn't instantiate and then merge new QuerySet:
```
pip install --upgrade git+https://github.com/tsouvarev/django-grappelli@use-models-queryset-in-autocomplete-lookup
```
- change `autocomplete_search_fields` to `['name_en__icontains']`
