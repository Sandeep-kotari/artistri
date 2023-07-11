from django.contrib import admin
from users.models import User,Post,like,article

admin.site.register(User)
# Register your models here.
admin.site.register(Post)
# admin.site.register(like)
admin.site.register(article)