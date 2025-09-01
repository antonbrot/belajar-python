best_pictures = [
'2019 - Parasite',
'2018 - Green Book',
'2017 - The Shape of Water',
'2016 - Moonlight',
'2015 - Spotlight',
'2014 - Birdman',
'2013 - 12 Years a Slave',
'2012 - Argo',
'2011 - The Artist'
]

winners_new = [
    '2024 - Anora',
    '2023 - Oppenheimer',
    '2022 - Everything Everywhere All at Once',
    '2021 - CODA',
    '2020 - Nomadland'
]

for winner in winners_new[::-1]:
    best_pictures.insert(0, winner)


for i in best_pictures:
    print(i)