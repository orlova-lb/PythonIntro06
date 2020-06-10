file_name_in = 'src.txt'
file_name_out = 'dst.txt'

template = '{name:<25}{avr:<7}\n'

with open(file_name_in, encoding='utf-8') as src, open(file_name_out, 'w', encoding='utf-8') as dst:
    avr_per_class = 0
    cnt = 0
    for line in src:
        tmp = line.strip('\n').strip().split()
        avr_per_st = round(sum([int(x) for x in tmp[2:]]) / len(tmp[2:]), 2)
        avr_per_class += avr_per_st
        cnt += 1
        st_name = tmp[1] + ' ' + tmp[0][0] + '.'
        str_out = template.format(name=st_name, avr=avr_per_st)

        dst.write(str_out)
        if avr_per_st <= 5.0:
            print(str_out, end='')

    print('Average per class:', round(avr_per_class / cnt, 2))

