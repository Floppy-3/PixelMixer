# Import and starting
from settingsPacket import settings
from PIL import Image, ImageShow

set = open("Settings.json", 'r+')
img = Image.open("pack.png")

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
        settings.backup(Settingsbackup.properties, r)
else:
    settings2.append('0')
    if settings2[0] == "1":
        print("settings loaded")
    else:
        settings.backup(Settingsbackup.properties, r)

print(settings2[22:24])

img.resize((settings2[11:13], settings2[22:24]))

#img.