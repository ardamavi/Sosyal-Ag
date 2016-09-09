from django.contrib import admin
from .models import Post
from .models import guncelYazi

class PostAdmin(admin.ModelAdmin):
    list_display = [
        'name',
        'first_name',
        'last_name',
        'text'
    ]
    search_fields = [
        'name',
        'first_name',
        'last_name',
        'text'
    ]


admin.site.register(Post, PostAdmin)
admin.site.register(guncelYazi)
