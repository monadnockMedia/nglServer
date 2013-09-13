#!/usr/local/bin/python
import web as webpy
import sqlite3 as lite
import string
import sys

render = webpy.template.render('templates/')

con = lite.connect('ngl.db', check_same_thread = False)
con.row_factory = lite.Row #dictionary for results
cur = con.cursor()


urls = (
    '/lifeAboard/', 'lifeAboard',
	'/Bio/(.*)', 'bio_id'
	
)

class index:
	def GET(self):
		raise webpy.seeother('/static/who.html')

class lifeAboard:
    def POST(self):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		url_vars = webpy.input()
		_authorID = url_vars.authorID
		_categoryID = url_vars.categoryID
		print "cat:"+_categoryID
		authorTest = bool(int(_authorID)-1)
		_author = "davy" if authorTest else "captain"
		print _author
		print authorTest
		with con:
			#cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? and CategoryID = ?",(1,1))
			cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? AND CategoryID = ?",(_authorID,_categoryID))
			rows = cur.fetchall()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
#		return rows
		return render.pages(rows)
		

    def GET(self):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		url_vars = webpy.input()
		_authorID = url_vars.authorID
		_categoryID = url_vars.categoryID
		print "cat:"+_categoryID
		authorTest = bool(int(_authorID)-1)
		_author = "davy" if authorTest else "captain"
		print _author
		print authorTest
		with con:
			#cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? and CategoryID = ?",(1,1))
			cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? AND CategoryID = ?",(_authorID,_categoryID))
			rows = cur.fetchall()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
		return render.pages(rows)
"""
class bio_id:
    def POST(self, _id):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		readable = int(webpy.input().readable)
		bio = ""
		with con:
			cur.execute("SELECT * FROM WhosWho WHERE id = ?",[_id])
			row = cur.fetchone()
			print("readable :: ", readable , bool(readable) )
			if readable == True:
				img = row["Photo"]
				bio+="<div class = 'half left readable'><img class = 'headshot' src ='%s%s' /></div>" % (imgurl,img)
				bio+="<div class = 'half right readable'><div id ='bio' class='readable'><h1>%s %s %s</h1><h1>(%s-%s)</h1><p>%s</p><p>%s</p></div>" % (row["First"],row["Middle"],row["Last"],row["Birth"],row["Death"],row["Body1"],row["Body2"])
				#	bio+="</div>"
				bio+=  "<ol id ='bioPage'><li id ='biop' class = '' dir = '-1' >&#8592prev</li><li>&#9674</li><li id ='bion' class = 'active' dir = '1'>next&#8594</li></ol></div>"
			else:
				img = row["Photo"]
				bio+="<div class = 'half left'><img class = 'headshot' src ='%s%s' /></div>" % (imgurl,img)
				bio+="<div class = 'half right'><div id ='bio'><h1>%s %s %s</h1><h1>(%s-%s)</h1><p>%s</p><p>%s</p></div>" % (row["First"],row["Middle"],row["Last"],row["Birth"],row["Death"],row["Body1"],row["Body2"])
				#	bio+="</div>"
				bio+=  "<ol id ='bioPage'><li id ='biop' class = '' dir = '-1' >&#8592prev</li><li>&#9674</li><li id ='bion' class = 'active' dir = '1'>next&#8594</li></ol></div>"
		
		
		
		return bio
		
"""
if __name__ == "__main__":
    app = webpy.application(urls, globals())
    app.run()
