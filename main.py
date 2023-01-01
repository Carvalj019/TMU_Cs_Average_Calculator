import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = #holds a list of google spreadsheet links
creds = ServiceAccountCredentials.from_json_keyfile_name("JSON credentials file here", scope)
client = gspread.authorize(creds)
spr = client.open_by_url('spreadsheet link here')
spreadsheet = spr.worksheet('Sheet1') #spreadsheet variable contains all the Ontario entrance admission data

averagesTotal = []
rows1 = spreadsheet.findall("Ryerson") + spreadsheet.findall("ryerson") + spreadsheet.findall("Ryerson University") + spreadsheet.findall("TMU")+ spreadsheet.findall("tmu") + spreadsheet.findall("ryerson(tmu)") + spreadsheet.findall("toronto metropolitan university")#finds all rows with ryerson admission averages
rows2 = spreadsheet.findall("computer science") + spreadsheet.findall("Computer Science") + spreadsheet.findall("cs") + spreadsheet.findall("CS") + spreadsheet.findall("Computer Science (Co-op available)") #finds all rows with computer science admission averages

rows1 = [x.row for x in rows1] #all rows containing ryerson entrance average information
rows2 = [x.row for x in rows2] #all rows containing computer science entrance average information
rowsTotal = [x for x in rows1 if x in rows2] #The intersection of lists rows1 and rows2 will provide the ryerson computer science entrance average information

sum = 0
for i in rowsTotal:
    averageInput = spreadsheet.cell(i, 4).value #averageInput is whatever the students inputted within the spreadsheet for their admission average (input data could include non-digit characters that need to be filtered)
    actualAverageInput = '' #This variable holds the filtered admission average
    for char in averageInput:
        if char.isdigit() or char == '.':
            actualAverageInput += char
        else:
            break
    sum += float(actualAverageInput)
print('Optimal TMU Computer Science Average for 2021-2022 Academic Year: ' + (str(sum/len(rowsTotal)))[0:5] + '%')
