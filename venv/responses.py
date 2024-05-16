from random import choice, randint
from discord.ext import commands
import giphy_client
from giphy_client.rest import ApiException
import http.client


api_instance = giphy_client.DefaultApi()
DANCE_GIF_URL = "https://giphy.com/gifs/party-raccoon-racoon-ZJPSFNLmADueHvzoZ8"
MONKEY_GIF_URL = "https://giphy.com/gifs/wahalaroom-help-ouch-oh-snap-lprIQG8Pl3T4gktKOZ"

def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return
    elif 'pedro' in lowered:
        if any(keyword in lowered for keyword in ['hello', '/roll', 'bye', 'help', 'dance', 'mal zwa9?',
                                                  'finahuwa sohlofia?', 'ch7al 10+10', 'how good is that dick',
                                                  '9oziba dayza', 'gif', 'chta7', 'terma dazet']):
            # Handle specific commands
            if 'hello' in lowered:
                return 'wa3alaykum salam!'
            elif '/roll' in lowered:
                roll_result = randint(1, 100)
                return f"you rolled {roll_result} (1-100)"
            elif 'bye' in lowered:
                return 'sir t9wd a khoya sir far3lia a kerri'
            elif 'help' in lowered:
                return 'Here are some commands you can try: Pedro hello - Pedro /roll - Pedro bye - Pedro dance or say something random I can respond to that too, who knows!'
            elif 'dance' in lowered or 'chta7' in lowered:
                return 'Pedro Pedro Pedroo\n' + DANCE_GIF_URL
            elif 'mal zwa9?' in lowered:
                return 'chkun? ما الأمر مع الدهون؟ rah ghlid khalih'
            elif 'finahuwa sohlofia?' in lowered:
                return 'bayna bark kaykft'
            elif 'ch7al 10 za2id 10' in lowered:
                return 'darham'
            elif 'how good is that dick' in lowered:
                return 'amaazing!'
            elif 'terma dazet' in lowered:
                return 'terma 9oziba dayza Nooo!\n' + MONKEY_GIF_URL
            elif lowered.startswith('pedro gif'):  # Moved this block outside of the 'pedro' block
                try:
                    # Make a request to Giphy API to fetch a random GIF
                    response = api_instance.gifs_random_get(api_key='GE8TkZoEgN65O98vgrc1NoSugVQIIIlW', rating='g', tag='funny')
                    gif_url = response.data.image_url
                    if gif_url:
                        print("GIF URL:", gif_url)  # Add this line to check the URL being fetched
                        return gif_url
                    else:
                        return 'Error fetching GIF. Try again later.'
                except ApiException as e:
                    print("Error fetching GIF:", e)  # Add this line to check for API errors
                    return 'Error fetching GIF. Try again later.'

        else:
            # Respond with default message if the command is not recognized
            return choice(['Wallah ma3reftek ach katgoul',
                       'sbr sbr dak l3wr ga3 magalia kifach njwd 3la had l blan',
                       'bayna l ghlid li dawi m3aya db',
                       'swl l haj yahia العرندس',
                       "khoya wallah mafhamtek ach katkhwr",
                       'l3ezzi a sa7bi how good is that dick',
                       ])
            