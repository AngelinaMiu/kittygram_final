import time
import logging
from rest_framework.response import Response
from rest_framework.decorators import api_view

logger = logging.getLogger(__name__)

@api_view(['GET'])
def my_view(request):
    start_time = time.time()

    try:
        result = some_database_query()

        logger.info("Время выполнения запроса: %s секунд", time.time() - start_time)
        return Response(result)

    except Exception as e:
        logger.error("Ошибка в my_view: %s", e)
        return Response({"error": "Произошла ошибка"}, status=500)
