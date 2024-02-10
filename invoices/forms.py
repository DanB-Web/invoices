from django import forms

PAYMENT_TERMS = [
    ("1", "Net 1 Day"),
    ("7", "Net 7 Days"),
    ("14", "Net 14 Days"),
    ("30", "Net 30 Days")
]

class InvoiceForm(forms.Form):
  
  # Invoice Ref
  invoice_ref = forms.CharField(
    max_length = 20,
    label = "Invoice Reference",
    # required = True,
    widget = forms.TextInput()
  )

  # Billed From
  sender_street = forms.CharField(
    max_length = 255,
    label = "Street Address",
    # required = True
    widget = forms.TextInput()
  )

  sender_city = forms.CharField(
    max_length = 255,
    label = "City",
    # required = True
    widget = forms.TextInput()
  )

  sender_postcode = forms.CharField( # REGEX
    max_length = 10,
    label = "Post Code",
    # required = True
    widget = forms.TextInput()
  )

  sender_country = forms.CharField(
    max_length = 255,
    label = "Country",
    # required = True
    widget = forms.TextInput()
  )

  # Client Details
  client_name = forms.CharField(
    max_length = 255,
    label = "Client's Name",
    widget = forms.TextInput()
  )

  client_email = forms.EmailField(
    label = "Client's Email",
    widget = forms.EmailInput()
  )

  client_street = forms.CharField(
    max_length = 255,
    label = "Street Address",
    # required = True
    widget = forms.TextInput()
  )

  client_city = forms.CharField(
    max_length = 255,
    label = "City",
    # required = True
    widget = forms.TextInput()
  )

  client_postcode = forms.CharField( # REGEX
    max_length = 10,
    label = "Post Code",
    # required = True
    widget = forms.TextInput()
  )

  client_country = forms.CharField(
    max_length = 255,
    label = "Country",
    # required = True
    widget = forms.TextInput()
  )

  # Payment Details
  created_at = forms.DateField(
    label = "Issue Date",
    # required = True,
    widget = forms.DateInput()
  )


  payment_terms = forms.ChoiceField(
    label = "Payment Terms",
    choices = PAYMENT_TERMS
  )

  # Description
  description = forms.CharField(
    max_length = 200,
    label = "Project Description",
    # required = True,
    widget = forms.TextInput()
  )

  def clean_invoice_ref(self):
    invoice_ref = self.cleaned_data['invoice_ref']
    if len(invoice_ref) < 2:
      raise forms.ValidationError('Length too short')
    else:
      return invoice_ref
