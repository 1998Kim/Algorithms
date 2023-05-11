def solution(new_id):
    new_id = new_id.lower()
    processing_id = ''

    for i in new_id:
        if i.isalpha() or i.isdigit() or i in '-_.':
            processing_id += i

    while '..' in processing_id:
        processing_id = processing_id.replace('..', '.')

    if processing_id[0] == '.':
        processing_id = processing_id[1:]
    if processing_id != '' and processing_id[-1] == '.':
        processing_id = processing_id[:-1]

    if processing_id == '':
        processing_id = 'a'
    
    if len(processing_id) > 15:
        processing_id = processing_id[:15]
        if processing_id[-1] == '.':
            processing_id = processing_id[:-1]

    while len(processing_id) < 3:
        processing_id += processing_id[-1]

    return processing_id