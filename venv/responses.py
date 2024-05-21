import http.client
import spacy
from random import choice, randint
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import logging

nlp = spacy.load("en_core_web_sm")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


api_instance = giphy_client.DefaultApi()
api_key = 'SUWQSugiOru9NsmGzExBsldHF8luulFI'
DANCE_GIF_URL = "https://giphy.com/gifs/party-raccoon-racoon-ZJPSFNLmADueHvzoZ8"
MONKEY_GIF_URL = "https://giphy.com/gifs/wahalaroom-help-ouch-oh-snap-lprIQG8Pl3T4gktKOZ"

smart_mode = False

def handle_hello():
    return 'wa3alaykum salam!'

def handle_roll():
    roll_result = randint(1, 100)
    return f"you rolled {roll_result} (1-100)"

def handle_bye():
    return 'sir t9wd a khoya sir far3lia a kerri'

def handle_help():
    return ('Here are some commands you can try: Pedro hello - Pedro /roll - Pedro bye - Pedro dance '
            'or say something random I can respond to that too, who knows!')

def handle_dance():
    return 'Pedro Pedro Pedroo\n' + DANCE_GIF_URL

def handle_mal_zwa9():
    return 'chkun? ما الأمر مع الدهون؟ rah ghlid khalih'

def handle_finahuwa_sohlofia():
    return 'bayna bark kaykft'

def handle_ch7al_10_plus_10():
    return 'darham'

def handle_how_good_is_that_dick():
    return 'amaazing!'

def handle_terma_dazet():
    return 'terma 9oziba dayza Nooo!\n' + MONKEY_GIF_URL

def handle_gif():
    try:
        logger.info("Attempting to fetch a random GIF from Giphy.")
        response = api_instance.gifs_random_get(api_key=api_key, rating='g', tag='funny')
        
        # Log the full response for debugging
        logger.info(f"Giphy API response: {response}")
        
        gif_url = response.data.url if response.data else None
        if gif_url:
            logger.info(f"GIF URL fetched: {gif_url}")
            return gif_url
        else:
            logger.warning("No GIF found in the response.")
            return 'No GIF found. Try again later.'
    except ApiException as e:
        logger.error(f"ApiException when calling Giphy API: {e}")
        return 'Error fetching GIF. Try again later.'
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 'Unexpected error occurred. Try again later.'

def get_response(user_input: str) -> str:
    global smart_mode

    lowered = user_input.lower()

    if lowered == '':
        return ''
    elif 'pedro' in lowered:
        if 'be smart' in lowered:
            smart_mode = True
            return "I'm getting smarter!"
        elif 'be normal' in lowered:
            smart_mode = False
            return "Back to normal mode!"
        elif smart_mode:
            return generate_smart_response(user_input)
        else:
            command_mapping = {
                'hello': handle_hello,
                '/roll': handle_roll,
                'bye': handle_bye,
                'help': handle_help,
                'dance': handle_dance,
                'chta7': handle_dance,
                'mal zwa9?': handle_mal_zwa9,
                'finahuwa sohlofia?': handle_finahuwa_sohlofia,
                'ch7al 10+10': handle_ch7al_10_plus_10,
                'how good is that dick': handle_how_good_is_that_dick,
                'terma dazet': handle_terma_dazet,
                'pedro gif': handle_gif,
            }

            for command, handler in command_mapping.items():
                if command in lowered:
                    return handler()
            
            return choice([
                'Wallah ma3reftek ach katgoul',
                'sbr sbr dak l3wr ga3 magalia kifach njwd 3la had l blan',
                'bayna l ghlid li dawi m3aya db',
                'swl l haj yahia العرندس',
                'l3ezzi a sa7bi how good is that dick',
            ])

def generate_smart_response(user_input: str) -> str:
    # Use an AI model to generate responses based on the input
    # For demonstration purposes, return a static response
    return "I'm feeling smarter!"
