#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import webapp2
import caesar 
import cgi

form = """
<form method= "post">
	<h1>Web Caesar</h1>
	<br>
	<p>Input a Number to rotate:</p>
	<input type="number" name="number"/>
	<br>
	<p>Input the text you would like rotated:</p>
	<textarea name="crip" ></textarea>
	<br>
	<br>
	<input type="submit">
		
</form>"""





class MainHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write(form)

    def post(self, crip=""):
    	answer = self.request.get('crip')
    	number = self.request.get("number")
    	newstr = caesar.encrypt(answer,int(number))
    	escaped_message = cgi.escape(newstr)
    	form2 = """<form method= "post"><h1>Enter some text to ROT13:</h1><p>Your coded message rotated by """+ number + """!</p><textarea name="crip">""" + escaped_message +"""</textarea><br><br><input type="submit"></form>"""
    	self.response.write(form2)

app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
