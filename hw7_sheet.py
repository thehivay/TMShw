''' Даны три столбца: Name, PRlink, Note. Cделать с 7 по 22 листа на каждом список имен группы.'''


import xlsxwriter

workbook = xlsxwriter.Workbook('hw7_sheet.xlsx')

for i in range(7, 22):

    worksheet1 = workbook.add_worksheet('Homework'+str(i))

    sheet1 = (['NAME', 'PRlink', 'NOTE'],
              ['Дмитрий Горский', '',''], ['Екатерина Гучек', '', ''],
              ['Роман Завадский', '', ''], ['Денис Копейкин', '',''],
              ['Дмитрий Лис', '', ''], ['Дмитрий Прусевич', '',''],
              ['Дарья Силантьева', '', ''], ['Вячеслав Станкевич', '', '']
    )

    row, col = 0, 0

    for names, prlink, note in sheet1:

        worksheet1.write(row, col,     names)
        worksheet1.write(row, col + 1, prlink)
        worksheet1.write(row, col + 2, note)
        row += 1

workbook.close()
