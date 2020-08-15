from django.urls import path
from . import views


urlpatterns = [
    path("", views.post_list, name="post_list"),
    path("post/<str:post_id>/", views.post),
    path("cv/", views.latest_cv),
    path("cv/<str:revision_date>/", views.cv),
]
