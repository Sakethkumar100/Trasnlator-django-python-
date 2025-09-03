from django.shortcuts import render,HttpResponse
from translate import Translator

def home(request):
    translation = None
    if request.method == "POST":
        text = request.POST["translate"]
        language = request.POST["language"]
        translator = Translator(to_lang=language)
        try:
            translation = translator.translate(text)
            if not translation or translation.strip() == text.strip():
                translation = "Sorry, can't translate this text."
        except Exception:
            translation = "Sorry, can't translate this text."
    return render(request, "main/index.html", {"translation": translation})