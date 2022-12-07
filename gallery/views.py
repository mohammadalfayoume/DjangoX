from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .models import Gallery


class GalleryListView(ListView):
    template_name = "gallery/gallery_list.html"
    model = Gallery


class GalleryDetailView(DetailView):
    template_name = "gallery/gallery_detail.html"
    model = Gallery


class GalleryCreateView(CreateView):
    template_name = "gallery/gallery_create.html"
    model = Gallery
    fields = ['title','img_url','purchaser','description']


class GalleryUpdateView(UpdateView):
    template_name = "gallery/gallery_update.html"
    model = Gallery
    fields = ['title','img_url','purchaser','description']


class GalleryDeleteView(DeleteView):
    template_name = "gallery/gallery_delete.html"
    model = Gallery
    success_url = reverse_lazy("gallery_list")