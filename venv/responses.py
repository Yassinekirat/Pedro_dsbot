from random import choice, randint




def get_response(user_input: str) -> str:
    lowered: str = user_input.lower()
    
    if lowered == '':
        return
    elif 'pedro' in lowered:
        if any(keyword in lowered for keyword in ['hello', '/roll', 'bye', 'help', 'dance', 'mal zwa9?', 'finahuwa sohlofia?']):
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
            elif 'dance' in lowered:
                return 'Pedro Pedro Pedroo! I can\'t use a gif just yet, sorry!'
            elif 'mal zwa9?' in lowered:
                return 'chkun? ما الأمر مع الدهون؟ rah ghlid khalih'
            elif 'finahuwa sohlofia?' in lowered:
                return 'bayna bark ykft'
        else:
            # Respond with default message if the command is not recognized
            return choice(['Wallah ma3reftek ach katgoul',
                       'sbr sbr dak l3wr ga3 magalia kifach njwd 3la had l blan',
                       'bayna l ghlid li dawi m3aya db',
                       'swl l haj yahia العرندس',
                       "khoya wallah mafhamtek ach katkhwr",
                       'l3ezzi a sa7bi how good is that dick',
                       ])
