import xlsxwriter
import json

with open('data.json', 'r') as f:
    restaurants = json.load(f)

workbook = xlsxwriter.Workbook(filename="data.xlsx")
spreadsheet = workbook.add_worksheet(name="Miami")
bold = workbook.add_format({"bold": 1})
spreadsheet.write("A1", "ID", bold)
spreadsheet.write("B1", "Restaurant", bold)
spreadsheet.write("C1", "Type", bold)
spreadsheet.write("D1", "Phone Number", bold)
row = 1
col = 0
for restaurant in restaurants:
    spreadsheet.write(row, col, restaurant.get("id"))
    spreadsheet.write(row, col+1, restaurant.get("title"))
    spreadsheet.write(row, col+2, restaurant.get("type"))
    spreadsheet.write(row, col+3, restaurant.get("phone_number"))
    row += 1

workbook.close()
