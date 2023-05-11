from django.urls import path
from posts import views

urlpatterns = [
    path("", views.PostListView.as_view(), name="post_list"),
    path("drafts/", views.DraftPostListView.as_view(), name="drafts"),
    path("archive/", views.DraftPostListView.as_view(), name="archive"),
    path("<int:pk>/edit/", views.PostUpdateView.as_view(), name="post_edit"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="post_delete"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post_detail"),
    path("new/", views.PostCreateView.as_view(), name="post_new"),  
]