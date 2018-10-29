from flask import Flask, request, redirect, render_template
import cgi

app = Flask(__name__)

app.config['DEBUG'] = True

def un_error():
    if not un_value:
        return "You didn't type anything! Please try again."
    elif len(un_value) > 20 or len(un_value) < 3:
        return "Your username must be atleast 3 characters long, and not more than 20. Please try again"
    elif ' ' in un_value == True:
        return "Your username cannot contain any spaces. Please try again."
    else:
        return ''

def pw_error():
    if not pw_value:
        return "You didn't type anything! Please try again."
    elif len(pw_value) > 20 or len(pw_value) < 3:
        return "Your password must be atleast 3 characters long, and not more than 20. Please try again."
    elif ' ' in pw_value:
        return "Your password cannot contain any spaces. Please try again."
    else:
        return ''

def vpw_value():
    if vpw_value != pw_value:
        return "Your passwords don't match. Please try again"
    else:
        return ''

def email_error():
    if not email_value:
        return ''
    elif ' ' in email_value == True:
        return "Your email cannot contain any spaces. Please try agian."
    elif len(email_value) > 20 or len(email_value) < 3:
        return "Your email must be atleast 3 characters long, and not more than 20."
    elif '@' not in email_value or '.' not in email_value:
        return "Your email must have an '@' and a '.' Please try again."
    else:
        return ''

@app.route("/", methods="GET")
def main():
    un_value = ''
    email_value = ''
    return render_template('index.html', un_value='', un_error='', pw_error='', vpw_error='', email_value='', ev_error='')

@app.route("/", methods="POST")
def attempt():
    un_value = request.args.get('username')
    email_value = request.args.get('email')
    pw_value = request.args.get('password')
    vpw_value = request.args.get('vpassword')
    unv_escaped = cgi.escape(un_value, quote=True)
    ev_escaped = cgi.escape(email_value, quote=True)

    if un_error == '' and pw_error == '' and vpw_error == '' and email_error == '':
        return render_template('success.html', username=unv_escaped())
    else:
        return render_template('index.html',un_value=unv_escaped() , un_error=un_error(), pw_error=pw_error(), vpw_error=vpw_error(), email_value=ev_escaped(), email_error=email_error())


if __name__ == '__main__':
    app.run()