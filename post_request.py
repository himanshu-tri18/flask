from flask import Flask,request
app=Flask(__name__)

@app.route('/',methods=['GET',"POST"])
def home():
    if request.method=="POST":
        return f'''
            <h2>display</h2><hr><hr>
            <h3>id : {request.form['emp_id']}<br>
            name: {request.form['emp_name']}<br>
            salary: {request.form['salary']}<br><br>
        '''
    return '''
        <form method="POST">
        id: <input type='text' name='emp_id'><br>
        name: <input type='text' name='emp_name'><br>
        salary :<input type='text' name='salary'><br>
        <button type="submit">submit</button>
        </form>
        '''

if __name__=='__main__':
    app.run(debug=True)