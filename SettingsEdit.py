from settingsPacket set_edit

MainMenu = '[1]Height\n' \
           '[2]Width\n' \
           '[3]Language\n' \
           '[0]Exit\n'

H_and_W = '[1]Set Default\n' \
          '[2]Set Costom\n' \
          '[0]Exit\n'

LangMenu = '[1]Ukranian\n' \
           '[2]English\n' \
           '[0]Exit\n'

set = open('settings.json',"r+")
settings = []

MainMenuInteract = input(MainMenu)

if MainMenuInteract == '1':
    HWInteract = input(H_and_W)
    if HWInteract == '1':
        settingsWidth = '16'
    elif HWInteract == '2':
        settingsWidth = int(input('Enter new width value\n'))
    elif HWInteract == '0':

elif MainMenuInteract == '2':
    HWInteract = input(H_and_W)
    if HWInteract == '1':
        settingsHeight = '16'
    elif HWInteract == '2':
        settingsHeight = int(input('Enter new width value\n'))

elif MainMenuInteract == '3':
    LangInteract = input(LangMenu)
    if LangInteract == '1':
        Lang = 'Ukrainian'
        print('Soon')
    elif LangInteract == '2':
        Lang = 'English'
        print('Soon')
else:
    exit("Unsupported List Object")
