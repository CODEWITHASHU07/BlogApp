from django.contrib import admin
from .models import User, Blog,Like,comment
# Register your models here.
admin.site.register(User)
admin.site.register(Blog)
admin.site.register(Like)
admin.site.register(comment)