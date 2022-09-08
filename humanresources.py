with open('hr_system.txt') as hr_sys:
    for line in hr_sys:
        new_line = line.strip()
        line = new_line.split(' ')
        name = line[0]
        id_number = line[1]
        job_title = line[2]
        salary = float(line[3])
        pay_check = salary / 24

        if job_title == 'Engineer':
            pay_check += 1000

        print(f'{name} (ID: {id_number}), {job_title} - ${pay_check:.2f}')
