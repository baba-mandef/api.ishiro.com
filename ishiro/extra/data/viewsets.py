from rest_framework import viewsets, status
from rest_framework.response import Response
from ishiro.extra.data.populate_category import populate_category
from ishiro.extra.rest.permission import IsStaffOnly


class PopulateViewSet(viewsets.ViewSet):
    permission_classes = [IsStaffOnly]
    
    def create(self, request, *args, **kwargs):
        
        try:
            populate_category()
        except Exception as e:
            print(e)
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
        return Response("Success", status=status.HTTP_200_OK)



