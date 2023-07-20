from django.urls import path
from .views import PostListApiView, PostCreateView, PostRetrieveUpdateDestroyView, PostCommentListView, PostCommentCreateView, \
 CommentListCreateApiView, PostLikeListView, CommentRetrievView, CommentLikeListView, PostLikeApiView, CommentLikeAPIView
urlpatterns = [
    path('list/', PostListApiView.as_view()),
    path('create/', PostCreateView.as_view()),
    path('<uuid:pk>/', PostRetrieveUpdateDestroyView.as_view()),
    path('<uuid:pk>/likes/', PostLikeListView.as_view()),
    path('<uuid:pk>/comments/', PostCommentListView.as_view()),
    path('<uuid:pk>/comments/create/', PostCommentCreateView.as_view()),
    path("comments/", CommentListCreateApiView.as_view()),
    path('comments/<uuid:pk>/', CommentRetrievView.as_view()),
    path('comments/<uuid:pk>/likes/', CommentLikeListView.as_view()),
    path("<uuid:pk>/create-delete-like/", PostLikeApiView.as_view()),
    path('comments/<uuid:pk>/create-delete-like/', CommentLikeAPIView.as_view()),
]