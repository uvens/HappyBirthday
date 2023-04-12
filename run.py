from servis1 import HappyBirthday

try:
    hapy=HappyBirthday()
    hapy('file.csv')
except Exception as e:
    print('Ошибка '+str(e))
