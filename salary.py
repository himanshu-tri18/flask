# Create a Flask application that stores an employee’s details (Employee ID, Name,
# Department, Basic Salary) in predefined variables, calculates HRA (20%), DA (12%),
# TA (8%), PF (10%), Gross Salary and Net Salary, and displays a salary slip on the
# home page.
# gross_salary = basic_salary + hra + da + ta
# net_salary = gross_salary - pf

from flask import Flask
app=Flask(__name__)

@app.route('/')
def page1():
    emp_id="01" 
    name='himanshu'
    department='cs'
    salary=5000
    hra=salary*0.2
    da=salary*0.12
    ta=salary*0.08
    pf=salary*0.1
    gross=salary+hra+da+ta
    net=gross-pf
    return f"""
        <h2>name: {name}</h2>
        <h2>department: {department}<br>
        salary: {salary}<br>
        hra: {hra}<br>
        da: {da}<br>
        ta: {ta}<br>
        pf: {pf}<br>
        gross: {gross}<br>
        net : {net}<br>
        <h2>
        """
if __name__=='__main__':
    app.run(debug=True)