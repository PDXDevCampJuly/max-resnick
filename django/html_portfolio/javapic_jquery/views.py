from django.shortcuts import render


def javapic(request):
    """
    JavaPic homepages
    """
    return render(request, 'javapic_jquery.html')

def join_javapic(request):
    """
    JavaPic form
    """
    return render(request, 'jq_join.html')

def gallery_javapic(request):
    """
    Javapic gallery
    """
    return render(request, 'jq_gallery.html')
