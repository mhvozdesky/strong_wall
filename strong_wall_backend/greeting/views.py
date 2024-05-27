from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from .models import GreetingModel
from .serializers import GreetingSerializer


class GreetingView(APIView):
    """
    View to handle greetings.

    This view allows users to post a greeting with their name.
    If the name does not exist in the database, it will be added.
    If the name already exists, the user will be informed that the name exists.
    """

    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handle POST request to add a greeting.

        Validates the input data and checks if the name exists in the database.
        If the name does not exist, it adds the name and returns a success message.
        If the name exists, it returns a message indicating that the name already exists.
        """

        serializer = GreetingSerializer(data=request.data)
        if serializer.is_valid():
            name = serializer.validated_data['name']
            customer, created = GreetingModel.objects.get_or_create(name=name)
            if created:
                return Response({'detail': 'greeting added'}, status=201)
            return Response({'detail': 'name exists'}, status=200)
        return Response(serializer.errors, status=400)

