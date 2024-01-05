from datetime import datetime
from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from .models import Note
from .serializers import NoteSerializer, UserSerializer
from .permissions import IsOwner
from rest_framework.views import APIView
from django.contrib.auth import authenticate


class NoteListCreateView(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        title = self.request.data.get('title')
        content = self.request.data.get('content')

        note_data = {
            'title': title,
            'content': content,
            'owner': self.request.user,  
            'created_at': datetime.now(), 
            #'shared_with': []  
        }

        serializer.save(**note_data)

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Note.objects.filter(owner=self.request.user)
        return Note.objects.none()
        


class NoteDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated, IsOwner]

    def perform_update(self, serializer):
        title = self.request.data.get('title')
        content = self.request.data.get('content')
        
        note_data = {
            'title': title,
            'content': content
        }

        serializer.save(**note_data)

    def get_object(self):
        return Note.objects.get(pk=self.kwargs['pk'])
    
    def perform_destroy(self, instance):
        try:
            instance.delete()
        except:
            return Response({"message": "note not found"},status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"message": "note deleted"},status=status.HTTP_204_NO_CONTENT)


class NoteSearchView(generics.ListAPIView):
    serializer_class = NoteSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        if self.request.user.is_authenticated:
            query = self.request.query_params.get('q', '')
            user = self.request.user
            queryset = Note.objects.filter(owner=user, title__icontains=query) | Note.objects.filter(owner=user, content__icontains=query)
            return queryset
        return Note.objects.none()


class SignupView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message":"user created"}  ,status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        if username and password:
            user = authenticate(username=username, password=password)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)
    