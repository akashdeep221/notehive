from django.urls import path
from .views import NoteListCreateView, NoteDetailView, NoteSearchView, SignupView, LoginView

urlpatterns = [
    path('api/notes/', NoteListCreateView.as_view(), name='note-list-create'),
    path('api/notes/<int:pk>/', NoteDetailView.as_view(), name='note-detail'),
    path('api/auth/signup/', SignupView.as_view(), name='signup'),
    path('api/auth/login/', LoginView.as_view(), name='login'),
    path('api/search/', NoteSearchView.as_view(), name='note-search'),
]