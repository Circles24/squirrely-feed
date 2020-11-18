from rest_framework.response import Response
from rest_framework.decorators import api_view
from .data_queues import toi_queue

@api_view(['GET'])
def get_articles(request):
    try:
        return Response(toi_queue, 200)
    except Exception as ex:
        print('internal server error ->', ex)
        print_exc()
        return Response({'msg':'internal server error'}, 500)
