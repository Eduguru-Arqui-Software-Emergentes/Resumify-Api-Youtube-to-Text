import goslate

gs = goslate.Goslate()

def translate_text(text: str, language: str):
    language_id = gs.detect(text)
    translated_text = gs.translate(text, language)

    return {
        "text": translated_text,
        "from": language_id,
        "to": language
    }