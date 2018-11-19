import os
import re

directoryShare = '/Volumes/photo/Фотоальбом/2018'
patterns = {r'январ\w': 'январь',
            r'феврал\w': 'февраль',
            r'март\w': 'март',
            r'апрел\w': 'апрель',
            r'ма\w': 'май',
            r'июн\w': 'июнь',
            r'июл\w': 'июль',
            r'август\w': 'август',
            r'сентябр\w': 'сентябрь',
            r'октябр\w': 'октябрь',
            r'ноябр\w': 'ноябрь',
            r'дкабр\w': 'декабрь',
            }
# june = re.match(pattern,)
# directoryLocal =
# dirPhoto = os.listdir(directoryShare)
# dirPhoto.sort()
# for folder in dirPhoto:
#     for pattern in patterns:
#         if re.search(pattern, folder) is not None:
#             print(folder, patterns.get(pattern))
#             break

files = os.walk(directoryShare)
# june = re.search(pattern, dirPhoto[1])
# print(dirPhoto[3])
# print(* dirPhoto, sep='\n')
# print(june.group(0))
for file in files:
    print(file)
