from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import FormMixin
from .forms import InvoiceForm, PAYMENT_TERMS
from .models import Invoice, InvoiceItem

class InvoiceListView(FormMixin, ListView):
  template_name = "invoices/invoices.html"
  model = Invoice
  form_class = InvoiceForm
  context_object_name = "invoices"
  success_url = reverse_lazy("invoices")
  paginate_by = 3

  def get_queryset(self):
        # user = self.request.user
        # queryset = Invoice.objects.filter(owner=user) Implement once auth working
        queryset = Invoice.objects.all().order_by('created_at')
        return queryset
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.get_form()
        context['payment_terms_options'] = PAYMENT_TERMS
        return context
  
  def post(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

  def form_valid(self, form):
      # Process the form data
      # For example, save the form and return a redirect response
      return super().form_valid(form)

  def form_invalid(self, form):
      # Handle invalid form submission
      # For example, render the template with the form and errors
      return self.render_to_response(self.get_context_data(form=form))
  

class InvoiceDetailView(DetailView):
  template_name = "invoices/invoice.html"
  model = InvoiceItem
  context_object_name = "invoice"

  def get_queryset(self):
      # user = self.request.user
      # queryset = Invoice.objects.filter(owner=user) Implement once auth working
      invoice_id = self.kwargs['pk']
      queryset = Invoice.objects.filter(id=invoice_id)
      return queryset
  
  def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['payment_terms_options'] = PAYMENT_TERMS
        return context

