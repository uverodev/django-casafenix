from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Page

class PageResource(resources.ModelResource):
    class Meta:
        model = Page
    

class PagesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
	readonly_fields = ('fecha_modificacion', 'fecha_creacion')
	list_display = ('nombre', 'orden', 'estado', 'fecha_creacion','fecha_modificacion',)
	resourse_class = PageResource
	
	def get_readonly_fields(self, request, obj = None):
		if request.user.groups.filter(name="Personal").exists():
			return ('fecha_creacion','fecha_modificacion', 'slug')
		else:
			return ('fecha_creacion','fecha_modificacion')

admin.site.register(Page, PagesAdmin)
