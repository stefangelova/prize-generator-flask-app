from flask import render_template
from application import app
from application.forms import GenerateForm

@app.route('/generate', methods=['GET', 'POST'])
@login_required
def generate():
    form=GenerateForm()
    if form.submit.data:
        res = requests.get("http://service3gen:5003").json()["prize"]
        db.session.add(postData)
        db.session.commit()
    return render_template ('generate.html', title='Generate Prize', form=form)
