from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import CustomUserSerializer, UserSummarySerializer
from .models import CustomUser


class UserListCreate(APIView):
    def post(self, request, *args, **kwargs):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            response_data = {
                "id": user.id,
                "username": user.username,
                "message": "User created successfully"
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserList(APIView):
    def get(self, request, *args, **kwargs):
        users = CustomUser.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class UserDetail(APIView):
    def get_object(self, identifier):
        try:
            if identifier.isdigit():
                return CustomUser.objects.get(id=identifier)
            else:
                return CustomUser.objects.get(username=identifier)
        except CustomUser.DoesNotExist:
            return None
    
    def get(self, request, identifier, *args, **kwargs):
        user = self.get_object(identifier)
        if user is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        
        serializer = UserSummarySerializer(user)
        return Response(serializer.data)
    

    def put(self, request, identifier, *args, **kwargs):
            user = self.get_object(identifier)
            if user is None:
                return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)

            updated_data = request.data
            updated_fields = {}

            if 'password' in updated_data:
                user.set_password(updated_data['password'])
                updated_fields['password'] = "Updated"

            for field, value in updated_data.items():
                if field != 'password':
                    setattr(user, field, value)
                    updated_fields[field] = value

            user.save()

            updated_user_data = {}
            for field, value in updated_fields.items():
                updated_user_data[field] = getattr(user, field)

            return Response({
                "detail": "User details updated successfully.",
                "updated_fields": updated_user_data
            }, status=status.HTTP_200_OK)
    

    def delete(self, request, identifier, *args, **kwargs):
        user = self.get_object(identifier)
        if user is None:
            return Response({"detail": "Not found."}, status=status.HTTP_404_NOT_FOUND)
        user.delete()
        return Response({"detail": f"User '{identifier}' deleted successfully."}, status=status.HTTP_204_NO_CONTENT)