from django.shortcuts import render

def zen_mockup(request):
    """
    Zen Mockup Render template
    """
    return render(request, 'zen_mockup.html')
