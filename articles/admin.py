from django.contrib import admin

from articles.models import Items, Subsections, Questions


class SubsectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'section']
    list_display_links = ['id', 'name', 'section']
    search_fields = ['name', 'subject']


class ItemsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'subsection']
    list_display_links = ['id', 'name', 'subsection']
    search_fields = ['name', 'subsection']


class QuestionsAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'item', 'answer']
    list_display_links = ['id', 'name', 'item', 'answer']
    search_fields = ['name', 'item', 'answer']


admin.site.register(Subsections, SubsectionAdmin)
admin.site.register(Items, ItemsAdmin)
admin.site.register(Questions, QuestionsAdmin)
