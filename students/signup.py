#! C:\Users\abhis\AppData\Local\Programs\Python\Python310\python.exe
print ("Content-type: text/html\n\n")
print(""" <!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <link rel="stylesheet" href="css/bootstrap.min.css">
    </head>""")
import cgi
import cgitb; cgitb.enable()

form = cgi.FieldStorage()
name=form.getvalue("email")
fileitem= form["filename"]
if fileitem.filename:
    fn = name
    with open(fn+".jpg",'wb') as f:
        f.write(fileitem.file.read())
    message = "The file was uploaded successfully"
else:
    message = "The file was not uploaded successfully"

print("<h1>"+message+"</h1>")
print("""<a href="http://localhost/face_recognition/login.html"><h3>Sign In</h3></a>""")