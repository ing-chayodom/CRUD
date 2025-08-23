from django.shortcuts import render
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import InspectionRecord
from .forms import InspectionForm

class InspectionListView(ListView):
    model = InspectionRecord
    template_name = 'inspections/list.html'
    context_object_name = 'items'
    paginate_by = 10

    def get_queryset(self):
        qs = super().get_queryset()
        q = self.request.GET.get('q', '').strip()
        if q:
            qs = qs.filter(
                Q(inspection_no__icontains=q) |
                Q(product_code__icontains=q) |
                Q(smell__icontains=q) |
                Q(status__icontains=q)
            )
        return qs

class InspectionCreateView(CreateView):
    model = InspectionRecord
    form_class = InspectionForm
    template_name = 'inspections/form.html'
    success_url = reverse_lazy('inspection_list')

class InspectionUpdateView(UpdateView):
    model = InspectionRecord
    form_class = InspectionForm
    template_name = 'inspections/form.html'
    success_url = reverse_lazy('inspection_list')

class InspectionDeleteView(DeleteView):
    model = InspectionRecord
    template_name = 'inspections/confirm_delete.html'
    success_url = reverse_lazy('inspection_list')
