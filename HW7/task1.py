vowels = {"а", "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"}

song = input("Напойте песню: ")

is_rythm = len(set(map(lambda phrase: len(list(filter(lambda char: char.lower() in vowels, phrase))), song.split()))) == 1

if is_rythm:
    print('Парам пам-пам')
else:
    print('Пам парам')