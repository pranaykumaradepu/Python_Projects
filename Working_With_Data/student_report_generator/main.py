# csv.reader - will read the CSV file and return each row as a list
# csv.DictReader - will read the CSV file and return each row as a dictionary

# with open('file name', 'w' newline='') as file:
# cs.writer(file) - will create a writer object to write to the CSV file
# csv.writerow(list) - will write a single row to the CSV file
# csv.writerows(list of lists) - will write multiple rows to the CSV file

# csv.DictWriter(file, fieldnames=list) - will create a DictWriter object to write to the CSV file
# csv.writeheader() - will write the header row to the CSV file
# csv.writerow(dict) - will write a single row to the CSV file using a dictionary
# csv.writerows(list of dicts) - will write multiple rows to the CSV file using a list of dictionaries

# create a csv file contain studnet data 
# def create_student_data_csv(filename):
#     fieldnames = ['Name', 'Math', 'Science', 'English']
#     students = [
#         {'Name': 'Alice Johnson', 'Math':50, 'Science':60, 'English':70},
#         {'Name': 'Bob Smith', 'Math':80, 'Science':70, 'English':60},
#         {'Name': 'Charlie Brown', 'Math':90, 'Science':80, 'English':70},
#         {'Name': 'Diana Prince', 'Math':70, 'Science':90, 'English':80},
#         {'Name': 'Ethan Hunt', 'Math':60, 'Science':50, 'English':90},
#     ]
#     with open(filename, 'w', newline='') as file:
#         writer = csv.DictWriter(file, fieldnames=fieldnames)
#         writer.writeheader()
#         for student in students:
#             writer.writerow(student)

# create_student_data_csv('students.csv')



import csv

# reading data from csv
def process_data(input_file):
    try:
        with open(input_file,'r') as infile:
            reader = csv.DictReader(infile)
            student_reports = []

            for row in reader:
                name = row['Name']
                math = int(row.get('Math',{}))
                science = int(row.get("Science",{}))
                english = int(row.get("English",{}))
                average = round((math+science+english) /3,2)
                status = 'pass' if average > 40 else 'fail'

                student_reports.append({
                    'name' : name,
                    'math' : math,
                    'science':science,
                    'english' : english,
                    'average' : average,
                    'status' : status
                })
        
        # writing processed data into new file
        with open('student_report.csv','w',newline='') as outfile:
            fieldnames = ['name','math','science','english','average','status']
            writer = csv.DictWriter(outfile,fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(student_reports)

        print(f'processed data updates in student_reports sucessfully')

    except FileNotFoundError:
        print(f'{input_file} not found')
    except KeyError:
        print('error : invalid column names in input file')
    except Exception as e:
        print(f'error : {e}')

input_file = 'students.csv'
process_data(input_file)