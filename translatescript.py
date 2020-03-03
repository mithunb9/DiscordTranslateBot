# Import Translator from Googletrans API
from googletrans import Translator

# Client
client = Translator()

# Main Function
def translate(target,text):
    try:
        return client.translate(f'{text}', dest=f'{target.lower()}').text
    except:
        return "Error"
