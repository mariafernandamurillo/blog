from typing import Any, Dict, Optional
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView)
from django.urls import reverse_lazy
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    UserPassesTestMixin
)
from .models import Post, Status

class PostListView(ListView):
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        published_status = Status.objects.get(name="published")
        context["post_list"] = Post.objects.filter(
            status = published_status
        ).order_by("created_on").reverse()
        return context

class DraftPostListView(LoginRequiredMixin, ListView):
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="draft")
        context["post_list"] = Post.objects.filter(
            status = draft_status
        ).filter(
            author = self.request.user
        ).order_by("created_on").reverse()
        return context
    
class ArchievePostListView(LoginRequiredMixin, ListView):
    template_name = "posts/lists.html"
    model = Post

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        draft_status = Status.objects.get(name="archieve")
        context["post_list"] = Post.objects.filter(
            status = draft_status
        ).filter(
            author = self.request.user
        ).order_by("created_on").reverse()
        return context

#class PostCreateView(LoginRequiredMixin, )

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post

class PostCreateView(LoginRequiredMixin, CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]

    def form_valid(self, form):
        form.instance.author = self.request.user
        draft_status = Status.objects.get(name="draft")
        form.instance.status = draft_status
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    template_name = "posts/edit.html"
    model = Post
    fields = ["title", "subtitle", "body", "status"]

    def test_func(self):
        # you can d anythinh you want here
        # as long as this returns True or False in the end
        post = self.get_object()
        return post.author == self.request.user

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin,  DeleteView):
    template_name = "posts/delete.html"
    model = Post
    success_url = reverse_lazy("post_list")

    def test_func(self):
        # The mane of the function has to be test_func, this comes from View
    # you can d anythinh you want here
       # as long as this returns True or False in the end
        post = self.get_object()
        return post.author == self.request.user