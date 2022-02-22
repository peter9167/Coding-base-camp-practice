import xlsxwriter

#엑셀 파일 생성하기
workbook = xlsxwriter.Workbook('test.xlsx')

#파일 안에 워크 시트 생성하기
worksheet = workbook.add_worksheet('jejucodingcamp')

#셀 안에 문자값 입력하기
worksheet.write('A1', 'A')
worksheet.write('B1', 'B')
worksheet.write('C1', 'C')
worksheet.write('D1', 'D')
worksheet.write('E1', 'E')

#셀 안에 숫자값 입력하기
worksheet.write('A2', 1)
worksheet.write('B2', 2)
worksheet.write('C2', 3)
worksheet.write('D2', 4)
worksheet.write('E2', 5)

#좌표로 셀 안에 문자값 입력하기
#worksheet.write(row값, column값, 원하는 입력 값)
worksheet.write(2, 0, 'a')
worksheet.write(2, 1, 'b')
worksheet.write(2, 2, 'c')
worksheet.write(2, 3, 'd')
worksheet.write(2, 4, 'e')

#좌표로 셀 안에 숫자값 입력하기
worksheet.write(3, 0, 10)
worksheet.write(3, 1, 20)
worksheet.write(3, 2, 30)
worksheet.write(3, 3, 40)
worksheet.write(3, 4, 50)

workbook.close()