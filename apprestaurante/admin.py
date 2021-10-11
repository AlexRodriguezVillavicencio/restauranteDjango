from django.contrib import admin
from django.http.response import HttpResponseRedirect
from .models import Local, Direccion, Cliente, Pedido, Producto, Categoria, Promociones, Snippet
from django.contrib.auth.models import Group
from django.urls import path
from django.utils.html import format_html



admin.site.site_header = 'Admin Restaurante'


class SnippetAdmin(admin.ModelAdmin):
    list_display = ('title', 'font_size_html_display')
    list_filter = ('created',)
    change_list_template= 'admin/snippets/snippets_change_list.html'

    def get_urls(self):
        urls = super().get_urls()
        custom_urls = [
            path('fontsize/<int:size>/',self.change_font_size)
        ]
        return custom_urls + urls

    def change_font_size(self, request, size):
        self.model.objects.all().update(font_size=size)
        self.message_user(request, 'font size set successfully!')
        return HttpResponseRedirect("../")

    def font_size_html_display(self,obj):
        display_size = obj.font_size if obj.font_size <= 30 else 30
        return format_html(
            f'<span style="font-size: {obj.font_size}px">{obj.font_size}</span>'
        )

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "precio"]
    
admin.site.unregister(Group)

admin.site.register(Local)
admin.site.register(Direccion)
admin.site.register(Cliente)
admin.site.register(Pedido)
admin.site.register(Categoria)
admin.site.register(Promociones)
admin.site.register(Producto, ProductoAdmin)
admin.site.register(Snippet, SnippetAdmin)
