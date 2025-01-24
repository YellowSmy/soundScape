from django.http import JsonResponse
from utils.get_youtube_id import get_youtube_id_and_thumbnail

def Search(request):
    query = request.GET.get("query", "")
    if query:
        result = get_youtube_id_and_thumbnail(query)
        return JsonResponse(result)

    #except
    return JsonResponse({"error": "No query provided."}, status=400)
