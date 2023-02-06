from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Drink
from .serializers import DrinkSerializer


class DrinksList(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """

    def get(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        drinks = Drink.objects.all()
        serializer = DrinkSerializer(drinks, many=True)
        data = {
            'all-drinks': serializer.data
        }
        return Response(data, status=status.HTTP_200_OK)

    def post(self, request):
        """_summary_

        Args:
            request (_type_): _description_

        Returns:
            _type_: _description_
        """
        serializer = DrinkSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)


class DrinksDetail(APIView):
    """_summary_

    Args:
        APIView (_type_): _description_
    """

    def get(self, request, id_):
        """_summary_

        Args:
            request (_type_): _description_
            id_ (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            drink = Drink.objects.get(pk=id_)
            serializer = DrinkSerializer(drink)
            data = {
                'drink': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)
        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request, id_):
        """_summary_

        Args:
            request (_type_): _description_
            id_ (_type_): _description_

        Returns:
            _type_: _description_
        """
        drink = Drink.objects.get(pk=id_)
        serializer = DrinkSerializer(drink, data=request.data)
        if serializer.is_valid():
            serializer.save()
            data = {
                'updated': serializer.data
            }
            return Response(data, status=status.HTTP_200_OK)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id_):
        """_summary_

        Args:
            request (_type_): _description_
            id_ (_type_): _description_

        Returns:
            _type_: _description_
        """
        try:
            drink = Drink.objects.get(pk=id_)
            drink.delete()
            return Response(status=status.HTTP_200_OK)
        except Drink.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
