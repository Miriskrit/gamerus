from django.shortcuts import redirect

def base_redirect(request):
    return redirect('index_page_url', permanent=False)