import pyttsx3
import goslate

# engine = pyttsx3.init()
# engine.say('You')
# engine.say('......okay nah sit down for their')
# engine.say('you are a big fat oaf damilare', 'fr')
# engine.runAndWait()
def select_lang(Language):
    # Language list
    if Language == 'English':
        Language = 'en'
    elif Language == 'Dutch' or Language == 'German':
        Language = 'de'
    elif Language == 'French':
        Language = 'fr'
    elif Language == 'Greek':
        Language = 'el'
    elif Language == 'Arabic':
        Language = 'ar'
    elif Language == 'Albanian':
        Language = 'sq'
    elif Language == 'Spanish':
        Language = 'sp'
    elif Language == 'Bulgarian':
        Language = 'bg'
    elif Language == 'Chinese':
        print('Choose one of the two options available')
        simp_or_trad = input('1. Simplified = S \n2. Traditional = T \n:').title()
        if simp_or_trad == 'S':
            Language = 'zh'
        elif simp_or_trad == 'T':
            Language = 'zho'
        else: print('Invalid option!')
    elif Language == 'Croatian':
        Language = 'hr'
    elif Language == 'Czech':
        Language = 'cs'
    elif Language == 'Danish':
        Language = 'da'
    elif Language == 'Filipino':
        Language = 'fil'
    elif Language == 'Finnish':
        Language = 'fi'
    elif Language == 'Japanese':
        Language = 'ja'
    else:
        print('Invalid Language!')
    return Language

def translator():
    gs = goslate.Goslate()
    Language = input('Input the language would you like to translate to: ').title()
    To = select_lang(Language)

    Text_to_tranlate = input('Type in what you want to tranlate:\n')

    return gs.translate(Text_to_tranlate, To)

if __name__ == '__main__':
    print(translator())
