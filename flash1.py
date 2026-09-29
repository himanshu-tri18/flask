from flask import Flask,request,flash,get_flashed_messages
app=Flask(__name__)
app.secret_key='none'
@app.route("/",methods=["POST","GET"])
def home():
    if request.method=='POST':
        no=request.form.get('no')
        name=request.form.get('name')
        unit=int(request.form.get('unit'))

        if unit<100:
            u1=unit*3
        elif 100<=unit<200:
            u1=unit*5
        else:
            u1=unit*10
        flash(f"ID :{no},Name :{name},Unit :{unit},Cost :{u1}")

    message=get_flashed_messages()
    message1=""
    for msg in message:
        message1=message1+msg   

    return f'''
            {message1}
            <form method='POST'>
            Customer N0: <input type='text' name='no'><br>
            Customer Name: <input type='text' name='name'><br>
            Customer Unit: <input type='text' name='unit'><br>
            <button type='submit'>submit</button>
            </form>

    '''
if __name__=="__main__":
    app.run(debug=True)
