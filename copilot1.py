from flask import Flask, render_template_string

app = Flask(__name__)

EMPLOYEES = [
	{"name": "Ava Patel", "role": "Developer", "department": "Engineering", "experience": 1},
	{"name": "Noah Kim", "role": "Designer", "department": "Product", "experience": 4},
	{"name": "Mia Garcia", "role": "Engineering Manager", "department": "Engineering", "experience": 9},
]

# Copy into templates/base.html:
TEMPLATES = {
	"base.html": '''<!doctype html><title>{% block title %}Employee Directory{% endblock %}</title><h1>Employee Directory</h1><nav><a href="{{ url_for('home') }}">Home</a> <a href="{{ url_for('employees') }}">Employees</a> <a href="{{ url_for('department') }}">Departments</a></nav>{% block content %}{% endblock %}''',
	"home.html": '''{% extends "base.html" %}{% block content %}<h2>Welcome</h2><p>{{ employees|length }} employees across {{ departments|length }} departments.</p>{% endblock %}''',
	"employees.html": '''{% extends "base.html" %}{% block title %}Employees{% endblock %}{% block content %}<h2>Employees</h2>{% for employee in employees %}<article><h3>{{ employee.name }}</h3><p>{{ employee.role }} — {{ employee.department }}</p><p>Experience: {{ employee.experience }} years</p></article>{% endfor %}{% endblock %}''',
	"department.html": '''{% extends "base.html" %}{% block title %}Departments{% endblock %}{% block content %}<h2>Departments</h2>{% for department in departments %}<h3>{{ department }}</h3><ul>{% for employee in employees if employee.department == department %}<li>{{ employee.name }} — {{ employee.role }}</li>{% endfor %}</ul>{% endfor %}{% endblock %}''',
}

@app.route("/")
def home():
	return render_template_string(TEMPLATES["home.html"], employees=EMPLOYEES, departments=sorted({e["department"] for e in EMPLOYEES}))

@app.route("/employees")
def employees():
	return render_template_string(TEMPLATES["employees.html"], employees=EMPLOYEES)

@app.route("/departments")
def department():
	return render_template_string(TEMPLATES["department.html"], employees=EMPLOYEES, departments=sorted({e["department"] for e in EMPLOYEES}))

if __name__ == "__main__":
	app.run()
