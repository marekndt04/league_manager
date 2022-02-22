from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Team


class TeamModelAdmin(ModelAdmin):
    model = Team
    menu_label = 'Teams'
    menu_icon = 'Group'
    menu_order = 200
    list_display = ('name', 'image')
    list_filter = ('name',)
    search_fields = 'name'


modeladmin_register(TeamModelAdmin)
