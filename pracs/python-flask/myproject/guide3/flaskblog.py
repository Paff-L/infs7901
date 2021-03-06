### Example inspired by Tutorial at https://www.youtube.com/watch?v=MwZwr5Tvyxo&list=PL-osiE80TeTs4UjLw5MM6OjgkjFeUxCYH
### However the actual example uses sqlalchemy which uses Object Relational Mapper, which are not covered in this course. I have instead used natural sQL queries for this demo. 

from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, BlogForm
app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

posts = [
    {
        'username': 'James',
        'title': 'How to Build a Data Science Portfolio',
        'content': 'The best way to build a data science portfolio is to do a project',
    },
    {
        'username': 'Jane',
        'title': 'Blockchain Could Unlock Vital Funding to Tackle Climate Chang',
        'content': 'Billions of dollars in promised funding is failing to reach the world’s poorest countries — but technologists have a fix in mind .....',
    }
]
users = [(0, 'James'), (1, 'Jane')]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

#Add User
@app.route("/register", methods=['GET', 'POST'])
def register():

    # Load registration form from forms.py
    form = RegistrationForm()

    # If the input data is OK...
    if form.validate_on_submit():

        # Append user to list of users and notify user with flash. Then, redirect to home URL
        users.append((len(users), form.username.data))
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))

    # This is for GET requests. Load the form and register.html
    return render_template('register.html', title='Register', form=form)

#Add Blog
@app.route("/blog", methods=['GET', 'POST'])
def blog():

    # Load blog form from forms.py
    # Note that the username choices are prefilled with the list of users variable.
    form = BlogForm()
    form.username.choices = users


    if form.validate_on_submit():

        # Extract input data from form variable
        choices = form.username.choices
        user =  (choices[form.username.data][1])
        title = form.title.data
        content = form.content.data

        # Save data into posts variable, and then alert user with flash
        posts.insert(0, {
            'username': user,
            'title': title,
            'content': content
        })
        flash(f'Blog created for {user}!', 'success')
        return redirect(url_for('home'))

    # This is for GET requests. Load the form and blog.html
    return render_template('blog.html', title='Blog', form=form)

if __name__ == '__main__':
    app.run(debug=True)

