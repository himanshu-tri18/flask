# Create a Flask Contact Form containing Name, Email, Subject, and Message. Check
# whether all fields are filled and display an appropriate flash message.
from flask import Flask,request,flash,get_flashed_messages
app=Flask(__name__)
app.secret_key='qwerty'

@app.route('/',methods=['POST','GET'])
def home():
    if request.method=='POST':
        name=request.form.get('name')
        email=request.form.get('email')
        subject=request.form.get('subject')
        message=request.form.get('message')

        if not name or not email or not subject or not message:
            flash("all fields are required")
        else:
            flash(f'name {name}\nemail:{email}\nsubject:{subject}\nmessage{message}')
    n1=get_flashed_messages()
    message1=""
    for m1 in n1:
        message1=message1+m1

    return f'''
        <h1>{message1}</h1><hr>
        <form method ="POST">
        Name :<input type="text" name="name"><br>
        Email: <input type="email" name="email"><br>
        Subject : <select name="subject">
        <option value='english'>engish</option>
        <option value='hindi'>hindi</option>
        </select>
        Message :<input type="text" name="message"><br>
        <button type="submit">submit</button>
        </form>
        '''
if __name__=='__main__':
    app.run(debug=True)