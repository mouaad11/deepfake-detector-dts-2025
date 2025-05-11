# myapp/views.py

from django.shortcuts import render

def deepfake_detector(request):
    """
    Renders the deepfake_form.html template.
    All uploading & prediction calls are done client-side via JS.
    """
    base_url = "https://9053-34-122-15-234.ngrok-free.app"

    return render(request, "deepfake_form.html", {
        "single_api": f"{base_url}/predict",
        "batch_api":  f"{base_url}/predict/batch",
        "video_api":  f"{base_url}/predict/video",
    })
