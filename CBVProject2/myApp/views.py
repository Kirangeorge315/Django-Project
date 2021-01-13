from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
from myApp.models import HOD
from django.urls import reverse_lazy
class HODListView(ListView):
    model=HOD
    #default template=hod_list.html
    #default context=hod_list
class HODDetailView(DetailView):
    model=HOD
    #default template=hod_detail.html
    #default context=hod
class HODCreateView(CreateView):
    model=HOD
    fields='__all__'
    #default template=hod_form.html
class HODUpdateView(UpdateView):
    model=HOD
    fields=('name','sal')
    #default template=hod_form.html
class HODDeleteView(DeleteView):
    model=HOD
    success_url=reverse_lazy('hods')
    #default template=hod_confirm_delete.html
'''class StaffListView(ListView):
    model=Staff
    #default template=staff_list.html
    #default context=staff_list
class StaffDetailView(DetailView):
    model=Staff
    #default template=staff_detail.html
    #default context=staff
class StaffCreateView(CreateView):
    model=Staff
    fields='__all__'
    #default template=staff_form.html
class StaffUpdateView(UpdateView):
    model=Staff
    fields=('sal')
    #default template=staff_form.html
class StaffDeleteView(DeleteView):
    model=Staff
    success_url=reverse_lazy('staffs')
    #default template=staff_confirm_delete.html
    '''






