from django.shortcuts import render


def forum(request):
    """
    forum view
    """
    return render(request, 'forum.html')
