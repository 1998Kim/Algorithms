def solution(m, musicinfos):
    answer = '(None)'
    answer_time = 0
    m = m.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
    
    for music in musicinfos:
        start, end, name, melody = music.split(',')
        start_hour, start_min = start.split(':')
        end_hour, end_min = end.split(':')
        melody = melody.replace('A#', 'a').replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g')
        
        play_time = (int(end_hour) * 60 + int(end_min)) - (int(start_hour) * 60 + int(start_min))
        
        if len(melody) > play_time:
            play_melody = melody[:play_time]
        else:
            play_melody = melody * (play_time // len(melody)) + melody[:play_time%len(melody)]
        
        if m in play_melody and play_time > answer_time:
            answer = name
            answer_time = play_time

    return answer