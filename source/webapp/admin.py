from django.contrib import admin
from webapp.models import Task, Status, Type

# class ArticleAdmin(admin.ModelAdmin):
#     list_display = ['id','title','created_at']
    # list_filter = ['id']
    # search_fields = ['title']
    # fields = ['title','created_at']
    # readonly_fields = ['created_at']



admin.site.register(Task)
admin.site.register(Status)
admin.site.register(Type)

