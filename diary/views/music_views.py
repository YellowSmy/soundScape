from django.http import JsonResponse
from utils.get_youtube_id import get_youtube_id_and_thumbnail

def Search(request):
    query = ""
    query = request.GET.get("query", "")

    if query:
        results = get_youtube_id_and_thumbnail(query)

        # 제목 & 노래제목 불러오기
        info = {
            'artist': query.split(" ", maxsplit=1)[0],
            'music_title': query.split(" ", maxsplit=1)[1],
        }
        return JsonResponse({'results' : results, 'info': info})

    #except
    return JsonResponse({"error": "No query provided."}, status=400)
