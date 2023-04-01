
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config [ 'SQLALCHEMY_DATABASE_URI'] = 'sqlite:///records.db'
db = SQLAlchemy(app)

class HealthRecords(db.Model):
    id= db.Column(db.Integer, primary_key= True)

    FirstName = db.Column(db.String(100), nullable = False)
    LastName = db.Column(db.String(100), nullable = False)
    DOB = db.Column(db.String(12), nullable = False)
    Phone = db.Column(db.String(12), nullable = False)
    Address = db.Column(db.Text(100), nullable = False)

    Insurance_Name = db.Column(db.String(20), nullable = False)
    Insurance_Id = db.Column(db.String(20), nullable = False)

    Height = db.Column(db.String(12), nullable = False)
    Weight = db.Column(db.Text(12), nullable = False)

    Allergies = db.Column(db.Text(100), nullable = False)
    Health_Concerns = db.Column(db.String(300), nullable = False)
    Note = db.Column(db.Text(300), nullable = False)
    Health_Records = db.Column(db.Text(300), nullable = False)
    Prescribed_Drugs = db.Column(db.Text(300), nullable = False)
 
    Last_visited = db.Column(db.String(12), nullable = False)
    Next_appointment = db.Column(db.String(12), nullable = False)
    date_added = db.Column(db.DateTime, nullable= False, default = datetime.utcnow)

    def __repr__(self):
        return 'Patient Health Records' + str(self.id)



@app.route('/')
def index():
    return render_template('index.html')

@app.route('/records', methods = ['GET','POST'])
def records():

    if  request.method == 'POST':
        record_FirstName = request.form['FirstName']
        record_LastName = request.form['LastName']
        record_DOB = request.form['DOB']
        record_Phone = request.form['Phone']
        record_Address = request.form["Address"]
        record_Insurance_Name = request.form['Insurance_Name']

        record_Insurance_Id = request.form['Insurance_Id']
        record_Height = request.form['Height']
        record_Weight = request.form['Weight']
        record_Allergies = request.form['Allergies']
        record_Health_Concerns = request.form['Health_Concerns']
        record_Note = request.form['Note']
        record_Health_Records = request.form['Health_Records']
        record_Prescribed_Drugs = request.form['Prescribed_Drugs']

        record_Last_visited = request.form['Last_visited']
        record_Next_appointment = request.form['Next_appointment']
        


        new_record =  HealthRecords(FirstName = record_FirstName, 
                                    LastName = record_LastName,
                                    DOB = record_DOB,
                                    Phone = record_Phone,
                                    Address = record_Address,
                                    Insurance_Name = record_Insurance_Name,
                                    Insurance_Id = record_Insurance_Id,
                                    Height = record_Height,
                                    Weight = record_Weight,
                                    Allergies = record_Allergies,
                                    Health_Concerns = record_Health_Concerns,
                                    Note = record_Note, 
                                    Health_Records = record_Health_Records,
                                    Prescribed_Drugs = record_Prescribed_Drugs,
                                    Last_visited = record_Last_visited,
                                    Next_appointment = record_Next_appointment)
        db.session.add(new_record)
        db.session.commit()
        return redirect('/records')
    else:
        all_records = HealthRecords.query.order_by(HealthRecords.date_added).all()
        return render_template('records.html', all_records = all_records)

@app.route('/records/delete/<int:id>')
def delete(id):
    records = HealthRecords.query.get_or_404(id)
    db.session.delete(records)
    db.session.commit()
    return redirect('/records')


@app.route('/records/edit/<int:id>', methods = ['GET', 'POST'])
def edit(id):
    records = HealthRecords.query.get_or_404(id)
    
    if request.method == 'POST':
        records.FirstName = request.form['FirstName']
        records.LastName = request.form['LastName']
        records.DOB = request.form['DOB']
        records.Phone = request.form['Phone']
        records.Address = request.form['Address']
        records.Insurance_Name = request.form['Insurance_Name']

        records.Insurance_Id = request.form['Insurance_Id']
        records.Height = request.form['Height']
        records.Weight = request.form['Weight']
        records.Allergies = request.form['Allergies']
        records.Health_Concerns = request.form['Health_Concerns']
        records.Note = request.form['Note']
        records.Health_Records = request.form['Health_Records']
        records.Prescribed_Drugs = request.form['Prescribed_Drugs']

        records.Last_visited = request.form['Last_visited']
        records.Next_appointment = request.form['Next_appointment']


        db.session.commit()
        return redirect('/records')
    
    else:
        return render_template('edit.html', records = records)

if __name__ == "__main__":
    app.run(debug = True);
