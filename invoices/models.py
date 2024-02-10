import uuid
from django.db import models
from django.core.validators import MinValueValidator
from users.models import CustomUser
from .forms import PAYMENT_TERMS

PAYMENT_STATUS = [
    ("DR", "Draft"),
    ("PA", "Paid"),
    ("PE", "Pending"),
]

"""
Note string based model fields such as CharField and TextField can be blank=True but do not require null=True
This is because Django will save these empty fields as empty strings (i.e. ""), so a NULL isn't required in the DB column

"""


class Invoice(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    invoice_ref = models.CharField(max_length=20)
    owner = models.ForeignKey(
        CustomUser, related_name="invoices", on_delete=models.CASCADE, null=True
    )
    created_at = models.DateField()
    payment_due = models.DateField()
    description = models.TextField()
    payment_terms = models.CharField(
        choices=PAYMENT_TERMS,
        max_length=255,
    )
    client_name = models.CharField(max_length=255)
    client_email = models.EmailField(blank=True, null=True)
    status = models.CharField(
        choices=PAYMENT_STATUS,
        max_length=255,
    )
    # Sender address
    sender_street = models.CharField(max_length=255, blank=True)
    sender_city = models.CharField(max_length=255, blank=True)
    sender_postcode = models.CharField(max_length=10, blank=True)
    sender_country = models.CharField(max_length=255, blank=True)
    # Client address
    client_street = models.CharField(max_length=255, blank=True)
    client_city = models.CharField(max_length=255, blank=True)
    client_postcode = models.CharField(max_length=10, blank=True)
    client_country = models.CharField(max_length=255, blank=True)

    def _get_total(self):
        items = InvoiceItem.objects.filter(invoice=self.id)
        total_cost = 0
        for obj in items:
            total_cost = total_cost + obj.total
        return total_cost

    total = property(_get_total)

    def __str__(self):
        return self.invoice_ref


class InvoiceItem(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    quantity = models.IntegerField(validators=[MinValueValidator(1)])
    price = models.DecimalField(max_digits=7, decimal_places=2)
    invoice = models.ForeignKey(
        Invoice, on_delete=models.CASCADE, related_name="invoice_items"
    )

    @property
    def total(self):
        return self.quantity * self.price

    def __str__(self):
        # Note using FK property - not using here due to FK constraint in admin search
        # return f"{self.name} - Invoice {self.invoice.invoice_ref}"
        return self.name