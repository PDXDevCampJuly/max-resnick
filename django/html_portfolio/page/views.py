from django.shortcuts import render


def about(request):
    """
    about view
    """
    return render(request, "about.html")

def table_of_contents(request):
    """
    table of contents app
    """
    return render(request, "toc.html")
