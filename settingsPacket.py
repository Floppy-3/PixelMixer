x=0
v=0
settings3=0

class settings:
    def help():
        chs = str(input('Інформація про команди'))
        if chs == 'open':
            print('перший аргумент э імя файлу та шлях до нього\nдругий аргумент режим відкриття')
            print('Не реалізовано!!!')
        elif chs == 'print':
            print('Виводить налаштування')
        elif chs == 'load':
            print('Підвантажує данні з файлу в список')
            print('Не реалізовано!!!')
        elif chs == 'backup':
            print('Виконує копіювання налаштувань з резервного файлу')
    #def load():
    #    set = open("E:\PyProjectsFiles\PixelMixer\Settings.json", 'r')
    #    setting = list(set.read)
    #    print(setting)

    def print():
        global x
        set = open("Settings.json", 'r')
        settings = set.read()
        while x < len(settings):
            print(settings[x])
            x=+1
            pass

    def backup(filename,mode):
        set = open("Settings.json", 'r+')
        backup = open(filename,mode)
        set.write(backup.read())
        print("Backup complete")


    def close():
        set.close

    def clearing(divider):
        global v
        global settings3
        set = open("Settings.json", 'r+')
        settings = set.read()
        while v <= int('2'):
            settings3 = settings.split(divider)
            settings3.pop(settings3.index(divider))
        return settings3
