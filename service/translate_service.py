import translators as ts


def translate_text(text: str, language: str):
    translated_text = ts.translate_text(text, translator="bing", from_language= 'es', to_language= language)

    return {
        "text": translated_text,
        "from": 'es',
        "to": language
    }