from django.shortcuts import render


def javapic(request):
    """
    JavaPic homepages.
    """
    return render(request, 'javapic.html')
