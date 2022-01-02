def format_cell(value, width):
    value = f" {value} "
    spaces = width - len(value)
    for i in range(spaces):
        value += ' '
    return value


def format_separator(n1, n2, n3):
    c = ""
    c += "+"
    for i in range(n1):
        c += "-"
    c += "+"
    for i in range(n2):
        c += "-"
    c += "+"
    for i in range(n3):
        c += "-"
    c += "+"
    return c


def format_playlist(songs):
    songs = sorted(songs, key=lambda x: (x[2], x[0]))

    n1 = len('Name')
    n2 = len('Time')
    n3 = len('Artist')

    for i in range(len(songs)):
        song = songs[i]
        if len(song[0]) > n1:
            n1 = len(song[0])
        if len(song[1]) > n2:
            n2 = len(song[1])
        if len(song[2]) > n3:
            n3 = len(song[2])

    n1 += 2
    n2 += 2
    n3 += 2

    c = ""
    c += format_separator(n1, n2, n3)
    c += "\n"

    c += "|"
    c += format_cell("Name", n1)
    c += "|"
    c += format_cell("Time", n2)
    c += "|"
    c += format_cell("Artist", n3)
    c += "|"
    c += "\n"

    c += format_separator(n1, n2, n3)
    if len(songs) == 0:
        return c

    c += "\n"

    for song in songs:
        c += "|"
        c += format_cell(song[0], n1)
        c += "|"
        c += format_cell(song[1], n2)
        c += "|"
        c += format_cell(song[2], n3)
        c += "|"
        c += "\n"

    c += format_separator(n1, n2, n3)

    return c


songs = [
    ('In Da Club', '3:13', '50 Cent'),
    ('Candy Shop', '3:45', '50 Cent'),
    ('One', '4:36', 'U2'),
    ('Wicked', '2:53', 'Future'),
    ('Cellular', '2:58', 'King Krule'),
    ('The Birthday Party', '4:45', 'The 1975'),
    ('In The Night Of Wilderness', '5:26', 'Blackmill'),
    ('Pull Up', '3:35', 'Playboi Carti'),
    ('Cudi Montage', '3:16', 'KIDS SEE GHOSTS'),
    ('What Up Gangsta', '2:58', '50 Cent')
]

songs2 = [
    ('Stoned Again', '3:25', 'King Krule'),
    ('Serenade', '3:00', 'Travis Scott'),
    ('I Always Wanna Die (Sometimes)', '5:15', 'The 1975'),
    ('Stick Talk', '2:54', 'Future'),
    ('Nightcrawler', '5:22', 'Travis Scott')
]

print(format_playlist(songs2))
