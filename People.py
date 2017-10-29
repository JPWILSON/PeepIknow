import sqlite3
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import parse_qs, unquote
import requests
import os

#Run this to check if the database has been set up:


#c.execute("""CREATE TABLE lists(
#    id integer primary key,
#    noun text,
#    adjective text)""")
#conn.commit()
#conn.close()


#conn = sqlite3.connect('employee.db')
#c = conn.cursor()
#c.execute("insert into lists(noun, adjective) values('houses', 'biggest')")
#conn.commit()
#c.execute("insert into lists(noun, adjective) values('people', 'richest')")
#conn.commit()
#c.execute("insert into lists(noun, adjective) values('cars', 'fastest')")
#conn.commit()
#c.execute("select * from lists")
#results = c.fetchall()
#for r in results:
#    print(r)
#conn.close()

#li = {"house":"biggest"}
page = """
<!doctype html>
<html lang="en">
<head>
    <title>P_I_K</title>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
</head>
<body>
    <div class='container'>
        <div class="row">
            <div class = "col-md-4"></div>
            <div class = "col-md-4">
                <h1 class="text-center bg-dark text-white">PEOPLE I KNOW</h1>
            </div>
            <div class = "col-md-4"></div>
        </div>
        <hr>
        <div class="row">
            <div class = "col-md-2"></div>
            <div class = "col-md-8">
                <p class="text-justify">This is a silly little db-backed app just listing all the people that I know and have interacted with. It doesn't include people from 
                school/ university/ where I live or work, that I do not interact with. I think the list will be surprisingly small. I will also include the interaction date, at a later date. It is a silly exercise, but is a way to learn to build web apps.</p>
            </div>
            <div class = "col-md-2"></div>
        </div>



        <h2>ADD PERSON</h2>
        <form method="POST">
            <div class="form-group">
              <label for="FirstName">First Name:</label>
              <input type="text" class="form-control" id="fname" name = "fname"  placeholder="Enter First Name">
          </div>
          <div class="form-group">
              <label for="LastName">Last Name:</label>
              <input type="text" class="form-control" id="lname" name = "lname" placeholder="Enter Last Name">
          </div>
          <div class="form-group">
              <label for="Relationship">Relationship:</label>
              <input type="text" class="form-control" id="rel" name = "rel" placeholder="Enter Relationship">
          </div>
          <button type="submit" class="btn btn-primary">Add Person</button>
      </form>

      <div class="row">&nbsp</div>
      <hr>
      <div class="row">&nbsp</div>

      <table class="table table-dark table-hover">
        <thead>
          <tr>
            <th>Firstname</th>
            <th>Lastname</th>
            <th>Relationship</th>
        </tr>
    </thead>
    <tbody class="bg-light">
      <tr>
        <td><pre>{}</pre></td>
        <td><pre>{}</pre></td>
        <td><pre>{}</pre></td>
    </tr>
</tbody>
</table>
"""
#print(type(results))
#print(len(results))
#print(results[0])

class ListMaker(BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200, "A ok")
		self.send_header("Content-type", "text/html; charset = utf-8")
		self.send_header("Location", "/")
		self.end_headers()
		#li = {}
		conn = sqlite3.connect('peeps.db')
		c = conn.cursor()
		c.execute("select * from people")
		results = c.fetchall()
		'''print(type(results))
		for result in results:
			li[0] = [result[1],result[2],result[3]]
			print(type(result[0]))
			print(result[0])
			print(result)
			print(type(result))
		print(results)
		print(type(results))'''
		conn.close()
        #ans = page.format("\n".join(str(results[1])),"\n".join(str(results[2])))
		#ans = page.format("\n".join(li.values()[0]),"\n".join(li.values())[1],"\n".join(li.values()[2]))
		ans = page.format("\n".join([e[1] for e in results]),"\n".join([e[2] for e in results]), "\n".join([e[3] for e in results]))
		self.wfile.write(ans.encode())

	def do_POST(self):
		length = int(self.headers.get("Content-Length", 0))
		posted_info = self.rfile.read(length).decode()
		data = parse_qs(posted_info)
		#print(data)
		print(data["fname"][0], data["lname"][0], data["rel"][0])
        #data is a dictionary: {'noun': ['Tallest'], 'adj': ['Person']}
		if ("fname" not in data) or ("lname" not in data) or ("rel" not in data):
			self.send_response(404)
			self.send_header("Content-type", "text/plain")
			self.end_headers()
			self.wfile.write("Please be sure to enter a first name, last name and a relationship".encode())
		else:
			fname, lname, rel = data["fname"][0], data["lname"][0], data["rel"][0]
		    #li[noun] = adj
			conn = sqlite3.connect('peeps.db')
			c = conn.cursor()
			c.execute("insert into people (fname, lname, relationship) values (?,?,?)",(fname, lname, rel))
			conn.commit()
			conn.close()
			self.send_response(303)
			self.send_header("Location", "/")
			self.end_headers()


if __name__ == '__main__':
  port = int(os.environ.get('PORT', 8000)) # Use port if it there...
  server_address = ('', port)
  httpd = HTTPServer(server_address, ListMaker)
  httpd.serve_forever()
