# Imports the Google Cloud client library
from google.cloud import translate

# Instantiates a client
translate_client = translate.Client()

# The text to translate
text = u'です by Glamour'
# The target language
target = 'pt'

# Translates some text into Russian
translation = translate_client.translate(text, source_language = 'ja', target_language = target)

#translate_client.get

print(u'Text: {}'.format(text))
print(u'Translation: {}'.format(translation['translatedText']))
