# Import and starting
from settingsPacket import settings, img_edit
from PIL import Image, ImageFont, ImageDraw
import sys

files = {
    'settingsfilename': "settings.json",
    'backupfilename': 'Settingsbackup.properties',
    'imagefilename': sys.argv[1]
}
print(sys.argv[1])
sfn = files['settingsfilename']
bfn = files['backupfilename']
imgfn = files['imagefilename']

set = open(sfn, 'r+')
img = Image.open(imgfn)
# Для роботи з текстом
# font = ImageFont.truetype("Pillow/Tests/fonts/FreeMono.ttf", 40)
draw = ImageDraw.Draw(img)

# Settings load
settings2 = set.read()
settings3 = 0

# Settings checking
# Поки що в файлі має бути 0 на початку щоб згенерувались налаштування за замовчуванням
# Інакше виб'є помилку (Вже виправлено)

if len(settings2) >= 1:
    if settings2[0] == "1":
        print("settings loaded")
    else:
        settings.backup(bfn, r)
else:
    settings2.append('0')
    if settings2[0] == "1":
        print("settings loaded")
    else:
        settings.backup(bfn, r)

print(settings2[22:24])

img.resize((int(settings2[11:13]), int(settings2[22:24])))
pixel = img.getpixel((8,8))
print(pixel)
colors = img_edit.eclipse((8,8),5,5,"pack.png")
draw.line((8,8,10,10),colors, 1)
# img.show()
london = {'name': 'London1', 'location': 'London Str'}
london = london + {'gandon': 'longdon'}
print(london)

