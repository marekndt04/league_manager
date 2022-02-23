from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from .models import Team


class TeamModelAdmin(ModelAdmin):
    model = Team
    menu_label = 'Teams'
    menu_icon = 'group'
    menu_order = 200
    list_display = ('name',)
    search_fields = 'name'


modeladmin_register(TeamModelAdmin)
