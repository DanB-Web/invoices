from django.urls import path
from invoices.views import (
    InvoiceDetailView,
    InvoiceListView
)

urlpatterns = [
  path("", InvoiceListView.as_view(), name="invoices"),
  path("<uuid:pk>", InvoiceDetailView.as_view(), name="invoice")
]