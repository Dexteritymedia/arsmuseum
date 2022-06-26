from wagtail.core import hooks
from wagtail.contrib.modeladmin.options import ( ModelAdmin, ModelAdminGroup, modeladmin_register)
from .models import ExhibitionPage


class ExhibitionPage(ModelAdmin):
    model = ExhibitionPage
    menu_label = 'Exhibition'
    menu_order = 150
    add_to_settings_menu = False
    exclude_from_explorer = False

modeladmin_register(ExhibitionPage)

