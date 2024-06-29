import http.client
import spacy
from random import choice, randint
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import logging
import discord
import requests

nlp = spacy.load("en_core_web_sm")

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

api_instance = giphy_client.DefaultApi()
api_key = 'SUWQSugiOru9NsmGzExBsldHF8luulFI'
DANCE_GIF_URL = "https://giphy.com/gifs/party-raccoon-racoon-ZJPSFNLmADueHvzoZ8"
MONKEY_GIF_URL = "https://giphy.com/gifs/wahalaroom-help-ouch-oh-snap-lprIQG8Pl3T4gktKOZ"

smart_mode = False

WEATHER_API_KEY = 'cf200b22dab18b5be0c59d5b1c2389dc'  # Your OpenWeatherMap API key

def handle_hello():
    return 'Hello! How can I assist you today?'

def handle_roll():
    roll_result = randint(1, 100)
    return f"You rolled {roll_result} (1-100)"

def handle_bye():
    return 'Goodbye! Have a great day!'

def handle_weather(user_input):
    if 'in' not in user_input:
        return 'Please provide the location for the weather update.'
    
    location = user_input.split('in')[1].strip()
    weather_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={WEATHER_API_KEY}&units=metric"
    
    try:
        response = requests.get(weather_url)
        response.raise_for_status()
        data = response.json()
        
        if data["cod"] != 200:
            return f"Error: {data['message']}"
        
        weather_description = data["weather"][0]["description"]
        temperature = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        
        return (
            f"Weather in {location.capitalize()}:\n"
            f"Description: {weather_description}\n"
            f"Temperature: {temperature}°C\n"
            f"Humidity: {humidity}%\n"
            f"Wind Speed: {wind_speed} m/s"
        )
    except requests.RequestException as e:
        logger.error(f"RequestException when calling OpenWeatherMap API: {e}")
        return 'Error fetching weather data. Try again later.'
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return 'Unexpected error occurred. Try again later.'


def handle_time():
    from datetime import datetime
    now = datetime.now()
    return f'The current time is {now.strftime("%H:%M:%S")}'

def handle_date():
    from datetime import datetime
    today = datetime.today()
    return f"Today's date is {today.strftime('%Y-%m-%d')}"

def handle_joke():
    jokes = [
        'Why don’t scientists trust atoms? Because they make up everything!',
        'Why did the scarecrow win an award? Because he was outstanding in his field!',
        'Why don’t skeletons fight each other? They don’t have the guts.',
    ]
    return choice(jokes)

def handle_quote():
    quotes = [
        'The greatest glory in living lies not in never falling, but in rising every time we fall. - Nelson Mandela',
        'The way to get started is to quit talking and begin doing. - Walt Disney',
        'Your time is limited, so don’t waste it living someone else’s life. - Steve Jobs',
    ]
    return choice(quotes)

def handle_fact():
    facts = [
        'Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.',
        'Octopuses have three hearts.',
        'Bananas are berries, but strawberries aren’t.'
    ]
    return choice(facts)

def handle_definition(word):
    # This is a placeholder. In a real application, you would call a dictionary API.
    definitions = {
        'example': 'a representative form or pattern',
        'bot': 'a computer program that performs automated tasks',
        'AI': 'artificial intelligence, the simulation of human intelligence in machines'
    }
    return definitions.get(word.lower(), f'Sorry, I don’t have a definition for {word}.')

def handle_translate(text, target_language='en'):
    # This is a placeholder. In a real application, you would call a translation API.
    translations = {
        ('hola', 'en'): 'hello',
        ('bonjour', 'en'): 'hello',
        ('ciao', 'en'): 'hello',
    }
    return translations.get((text.lower(), target_language), f'Sorry, I can’t translate {text} to {target_language}.')

def handle_help():
    return (
        "**Here are the commands you can use with Pedro:**\n\n"
        "`Pedro hello`: Greet Pedro.\n"
        "`Pedro /roll`: Roll a dice (1-100).\n"
        "`Pedro bye`: Bid farewell to Pedro.\n"
        "`Pedro help`: Display this help message.\n"
        "`Pedro dance` or `Pedro chta7`: Watch Pedro dance!\n"
        "`Pedro gif`: Get a random funny GIF.\n"
        "`Pedro weather <location>`: Get the weather for a specific location.\n"
        "`Pedro time`: Get the current time.\n"
        "`Pedro date`: Get the current date.\n"
        "`Pedro joke`: Hear a joke.\n"
        "`Pedro quote`: Get an inspirational quote.\n"
        "`Pedro fact`: Learn an interesting fact.\n"
        "`Pedro define <word>`: Get the definition of a word.\n"
        "`Pedro translate <text> to <language>`: Translate text to a specified language.\n"
        "\n"
        "Feel free to use these commands anytime to interact with Pedro!\n"
        "I will have a smart mode soon by using `Pedro be smart` and a normal mode `Pedro be normal`\n"
        "but if I don’t understand you, I'll just say some random responses."
    )

def handle_dance():
    return 'Pedro Pedro Pedroo\n' + DANCE_GIF_URL

def handle_gif():
    try:
        logger.info("Attempting to fetch a random funny meme GIF from Giphy.")
        # Specify tags related to memes and humor
        tags = ['funny', 'meme', 'humor']
        response = api_instance.gifs_random_get(api_key=api_key, rating='g', tag='+'.join(tags))
        
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
                'hi': handle_hello,
                '/roll': handle_roll,
                'bye': handle_bye,
                '/help': handle_help,
                'dance': handle_dance,
                'chta7': handle_dance,
                'pedro gif': handle_gif,
                'weather': lambda: handle_weather(user_input),
                'time': handle_time,
                'date': handle_date,
                'joke': handle_joke,
                'quote': handle_quote,
                'fact': handle_fact,
                'define': lambda: handle_definition(user_input.split('define ')[1]),
                'translate': lambda: handle_translate(user_input.split('translate ')[1].split(' to ')[0], user_input.split(' to ')[1] if ' to ' in user_input else 'en'),
            }

            for command, handler in command_mapping.items():
                if command in lowered:
                    return handler()
            
            return choice([
                'I am not sure what you are saying.',
                'Please hold on while I figure this out.',
                'It appears I did not understand your request.',
                'Could you please clarify your query?',
                'How good is that rating?',
            ])

def generate_smart_response(user_input: str) -> str:
    return "I'm feeling smarter!"
