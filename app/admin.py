from django.contrib import admin
from app.models import post , likepost , commnetpost
# Register your models here.


@admin.register(post)
class postadmin(admin.ModelAdmin):
    list_display = ['id','postname','shortdesc','description','date']


@admin.register(likepost)
class postadmin(admin.ModelAdmin):
    list_display = ['id','user','postname']

@admin.register(commnetpost)
class postadmin(admin.ModelAdmin):
    list_display = ['id','user','commnent']