from PIL import Image, ImageDraw
import random

files = {
    'settingsfilename': "settings.json",
    'backupfilename': 'Settingsbackup.properties',
    'imagefilename': 'pack.png'
}
sfn = files['settingsfilename']
bfn = files['backupfilename']
imgfn = files['imagefilename']

x = 0
v = 0
settings3 = 0

class settings:
    def help():
        while True:
            chs = str(input('Інформація про команди\n'
                            'список команд можна подивитись в коді Settingspacket\n'
                            'щоб вийти напишіть exit\n'))
            if chs == 'open':
                print('перший аргумент э імя файлу та шлях до нього\n'
                      'другий аргумент режим відкриття')
                print('Не реалізовано!!!')
            elif chs == 'print':
                print('Виводить налаштування')
            elif chs == 'load':
                print('Підвантажує данні з файлу в список')
                print('Не реалізовано!!!')
            elif chs == 'backup':
                print('Виконує копіювання налаштувань з резервного файлу')
            elif chs == 'eclipse':
                print('Затемнює вибрані пікселі\n'
                      'перший аргумент - кординати (x,y)\n'
                      'другий аргумент - мінімальне затемнення\n'
                      'третій аргумент - максимальне затемнення\n'
                      'четвертий аргумент - файл\n'
                      'img_edit.eclipse((1,1),5,5,setings.json)\n')
            elif chs == 'lighting':
                print('Освітлює вирані пікселі\n'
                      'перший аргумент - кординати (x,y)\n'
                      'другий аргумент - мінімальне освітлення\n'
                      'третій аргумент - максимальне освітлення\n'
                      'четвертий аргумент - файл\n'
                      'img_edit.lighting(1,1),5,5,setings.json\n')
            elif chs == 'drawframe':
                print('Малює рамку в вибраному радіусі\n'
                      'перший аргумент - радіус\n'
                      'другий аргумент - колір\n'
                      'третій аргумент - файл\n'
                      'settings.drawframe(8,(255,255,255,255),settins.json\n')
            elif chs == 'pixelchoise':
                print('Дозволяє вибрати пікселі')
            elif chs == 'Exit':
                break
            else:
                print('Unknown command')

    # def load():
    #    set = open("E:\PyProjectsFiles\PixelMixer\Settings.json", 'r')
    #    setting = list(set.read)
    #    print(setting)

    def print():
        global x, sfn
        set = open(sfn, 'r')
        settings = set.read()
        while x < len(settings):
            print(settings[x])
            x = +1
            pass

    def backup(filename,backupfilename):
        set = open(filename, 'r+')
        backup = open(backupfilename,'r')
        set.write(backup.read())
        print("Backup complete")

    # def close():
    #     set.close

    # def clearing(divider):
    #     global v
    #     global settings3
    #     set = open("Settings.json", 'r+')
    #     settings = set.read()
    #     while v <= int('2'):
    #         settings3 = settings.split(divider)
    #         settings3.pop(settings3.index(divider))
    #     return settings3

class img_edit:
    def eclipse(cordxy, maxeclipse, mineclipse, filename=imgfn):
        img = Image.open(filename)
        pixel = img.getpixel(cordxy)
        red = random.randint(pixel[0] - mineclipse, pixel[0] - maxeclipse)
        blue = random.randint(pixel[1] - mineclipse, pixel[1] - maxeclipse)
        green = random.randint(pixel[2] - mineclipse, pixel[2] - maxeclipse)
        alpha = pixel[3]
        colors = (red, blue, green, alpha)
        print(colors)
        return colors

    def lighting(cordxy, maxeclipse, mineclipse, filename=imgfn):
        img = Image.open(filename)
        pixel = img.getpixel(cordxy)
        red = random.randint(pixel[0] + mineclipse, pixel[0] + maxeclipse)
        blue = random.randint(pixel[1] + mineclipse, pixel[1] + maxeclipse)
        green = random.randint(pixel[2] + mineclipse, pixel[2] + maxeclipse)
        alpha = pixel[3]
        colors = tuple(red, blue, green, alpha)
        print(colors)
        return colors

    def pixelchoice():
        while True:
            pixellist = []
            pixelinput = input('Enter pixel cords\n[0]Exit\nCoordinate start from upper lefp angle')
            if pixelinput == '0':
                print('Pixel cords returned')
                break
            else:
                pixellist.append(pixelinput)
        return pixellist

    def drawframe():
        pass

    def softfller():
        pass

class set_edit:
    def exit(H='16',W='16',L='English'):
        settingslist = [H,W,L]
        set = open(sfn,'w')
        sett = open(sfn,'r')
        sett.readlines()
        set.writelines(settingslist)
        exit('Program Complete')