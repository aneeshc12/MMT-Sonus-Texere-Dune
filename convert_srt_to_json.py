import re
import os

op_path = './processed/dune/dune_transcript.json'
f = open('./processed/dune/dune_sub.srt')

sections = f.read()
sections = re.sub('<[\/a-z0-9="# ]*>', '', sections)
sections = re.sub('{.*}', '', sections)
sections = re.sub('[0-9]*\n([0-9][0-9]:[0-9][0-9])', r'\g<1>', sections)
sections = re.sub('\"', '\'', sections)
sections = sections.split('\n\n')

with open(op_path, 'w') as op:
    op.write("{\n")
    op.write("\"transcript\": [\n")

    for section in sections[:-1]:
        if section == '' or section == None:
            continue

        lines = section.split('\n')
        time = lines[0]
        
        line = ""
        for l in lines[1:]:
            line += l 
            line += " "

        op.write("{\"time\": \"%s\", \"line\": \"%s\"},\n" % (time, line))

    # last comma
    lines = sections[-1].split('\n')
    time = lines[0]
    
    line = ""
    for l in lines[1:]:
        line += l 
        line += " "

    op.write("{\"time\": \"%s\", \"line\": \"%s\"}\n" % (time, line))


    op.write("]}\n")



    
