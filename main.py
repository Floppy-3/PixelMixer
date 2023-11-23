# Import and starting
from settingsPacket import settings, img_edit
from PIL import Image, ImageFont, ImageDraw

#File name conect
files = {
    'settingsfilename': "settings.json",
    'backupfilename': 'Settingsbackup.properties',
    'imagefilename': 'pack.png'
}
sfn = files['settingsfilename']
bfn = files['backupfilename']
imgfn = files['imagefilename']

#File opening
set = open(sfn, 'r+')
img = Image.open(imgfn)
draw = ImageDraw.Draw(img)

# Settings load
settingslist = set.readlines()
try:
    SettingsDict = dict(FirstControlKey=settingslist[0], ImageHeight=settingslist[1], ImageWidth=settingslist[2],
                        LastControlKey=settingslist[3])
except:
    print('Завантаження завершене з критичною помилкою')

# Settings checking
# Поки що в файлі має бути 0 на початку щоб згенерувались налаштування за замовчуванням
# Інакше виб'є помилку (Вже виправлено)

l = input('Enter:\n'
          'Load - For continue program\n'
          'or\n'
          'Help - For get info about functions\n')

if l == 'Help':
    settings.help()

try:
    if SettingsDict['FirstControlKey'] == '1' and SettingsDict['LastControlKey'] == '2':
        print('Налаштування завантажені успішно')
    else:
        print('Налаштування втрачені, починаю відкат')
        settings.backup(sfn, bfn)
except:
    print("Налаштування пошкоджені, починаю бекап")
    settings.backup(sfn, bfn)

img.resize((int(SettingsDict['ImageHeight']), int(SettingsDict['ImageWidth'])))
colors = img_edit.eclipse((8, 8), 5, 5, imgfn)
draw.line((8, 8, 10, 10), colors, 1)
# img.show()
