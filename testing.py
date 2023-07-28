import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

class Employee:
    def __init__(self, company, level, title, location, years_of_experience, years_at_company, total_yearly_compensation, base_salary, stock_grant_value, bonus, gender, race, education):
        self.company = company
        self.level = level
        self.title = title
        self.location = location
        self.years_of_experience = years_of_experience
        self.years_at_company = years_at_company
        self.total_yearly_compensation = total_yearly_compensation
        self.base_salary = base_salary
        self.stock_grant_value = stock_grant_value
        self.bonus = bonus
        self.gender = gender
        self.race = race
        self.education = education
        
    def __repr__(self):
        return f"Employee(company='{self.company}', title='{self.title}', location='{self.location}')"

class EmployeeData:
    def __init__(self, file_path):
        self.df = pd.read_csv(file_path)
        self.employees = [Employee(**row) for index, row in self.df.iterrows()]
        
    def get_highest_paid(self, n=5):
        return sorted(self.employees, key=lambda x: x.total_yearly_compensation, reverse=True)[:n]
    
    def get_average_compensation_by_race(self):
        return self.df.groupby('Race')['total yearly compensation'].mean()
    
    def get_average_compensation_by_education(self):
        return self.df.groupby('Education')['total yearly compensation'].mean()

class EmployeeVisualizer:
    def __init__(self, data):
        self.data = data
        
    def plot_highest_paid(self, n=5):
        highest_paid = self.data.get_highest_paid(n)
        x = [employee.title for employee in highest_paid]
        y = [employee.total_yearly_compensation for employee in highest_paid]
        plt.bar(x, y)
        plt.title(f"Highest paid employees (top {n})")
        plt.xlabel("Title")
        plt.ylabel("Total yearly compensation")
        plt.show()
        
    def plot_average_compensation_by_race(self):
        avg_compensation_by_race = self.data.get_average_compensation_by_race()
        x = avg_compensation_by_race.index
        y = avg_compensation_by_race.values
        plt.bar(x, y)
        plt.title("Average compensation by race")
        plt.xlabel("Race")
        plt.ylabel("Average total yearly compensation")
        plt.show()
        
    def plot_average_compensation_by_education(self):
        avg_compensation_by_education = self.data.get_average_compensation_by_education()
        x = avg_compensation_by_education.index
        y = avg_compensation_by_education.values
        plt.bar(x, y)
        plt.title("Average compensation by education")
        plt.xlabel("Education")
        plt.ylabel("Average total yearly compensation")
        plt.show()

input = 'PyMeth_DataSci_Salaries.csv'
output = 'new_file.csv'
def main(input, output):
    data = EmployeeData(input)
    visualizer = EmployeeVisualizer(data)
    
    # Plot highest paid employees
    visualizer.plot_highest_paid()
    
    # Plot average compensation by race
    visualizer.plot_average_compensation_by_race()
    
    # Plot average compensation by education
    visualizer.plot_average_compensation_by_education()
    
    # Write insights to output file
    with open(output, 'w') as f:
        f.write(f"Top 5 highest paid employees:\n")
        for i, employee in enumerate(data.get_highest_paid()):
            f.write(f"{i+1}. {employee.title} at {employee.company} in {employee.location}: ${employee.total_yearly_compensation:.2f}\n")
            
        f.write(f"\nAverage compensation by race:\n")
        f.write(f"{data.get_average_compensation_by_race()}\n")
        
        f.write(f"\nAverage compensation by education:\n")
        f.write(f"{data.get_average_compensation_by_education()}\n")


main(input, output)