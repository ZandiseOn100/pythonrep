import csv 

#Read data from a csv file
def read_csv(file_name):
    data = []
    with open(file_name, mode="r") as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            data.append(row)
    return data

#Process the data (calculate avarage salary)
def calculate_average_salary(data):
    total_salary = 0
    employee_count = 0
    
    for row in data:
        total_salary += float(row["Salary"])
        employee_count += 1
    return total_salary / employee_count if employee_count > 0 else 0

#Save the results to a new csv file
def save_results(file_name, average_salary):
    with open(file_name, mode="w", newline="") as file:
        csv_writer = csv.writer(file)
        csv_writer.writerow(["Metric", "Value"])
        csv_writer.writerow(["Average Salary", average_salary])                    

#Main Program
if __name__ == "__main__":
    input_file = "employees.csv"
    output_file = "summary.csv"
    
    try:
        data = read_csv(input_file)
        avg_salary = calculate_average_salary(data)
        save_results(output_file, avg_salary)
        print(f"Average salary: {avg_salary}")       
        print(f"Results saved to: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")           