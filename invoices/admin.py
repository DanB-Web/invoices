from django.contrib import admin
from .models import Invoice, InvoiceItem

# Overide Admin model to show 'total' field from model
class InvoiceAdmin(admin.ModelAdmin):
    list_display = (
        "invoice_ref",
        "description",
        "client_name",
        "payment_due",
        "total",
        "owner",
    )
    readonly_fields = ["total"]
    search_fields = ("invoice_ref", "client_name", "owner")


class InvoiceItemAdmin(admin.ModelAdmin):
    list_display = ("name", "quantity", "price", "total", "invoice")
    # Note format to search by FK
    search_fields = ("name", "invoice__invoice_ref")


admin.site.register(Invoice, InvoiceAdmin)
admin.site.register(InvoiceItem, InvoiceItemAdmin)
