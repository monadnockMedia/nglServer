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
	'/story', 'story',
	'/story/(.*)', 'singleStory',
	'/', 'index',
	'/lifeSaving/LAKE/(.*)','lifeSaving',
	'/lifeSaving/ID/(.*)','singleLife'
	
	
	
)

class index:
	def GET(self):
		raise webpy.seeother('static/lifeAboard/index.html')

class singleStory:
	def GET(self, hoot):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		with con:
			#cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? and CategoryID = ?",(1,1))
			cur.execute("SELECT * FROM story WHERE ID = ?",(hoot))
			rows = cur.fetchall()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
		#return rows
		return render.single(rows)

class story:
	def GET(self):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		with con:
			#cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? and CategoryID = ?",(1,1))
			cur.execute("SELECT * FROM story ORDER BY last ASC")
			rows = cur.fetchall()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
		return render.stories(rows)

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
		return render.pages(rows,_author)
		
class singleLife:
	def GET(self, id):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		with con:
			#cur.execute("SELECT * FROM lifeAboard WHERE AuthorID = ? and CategoryID = ?",(1,1))
			cur.execute("SELECT * FROM lifeSaving WHERE ID = ?",[id])
			row = cur.fetchone()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
		#return rows
		return render.life_single(row)

class lifeSaving:
	def GET(self, lake):
		webpy.header('Access-Control-Allow-Origin',      '*')
		webpy.header('Access-Control-Allow-Credentials', 'true')
		webpy.header('Content-Type','text/html; charset=utf-8', unique=True) 
		_q = "SELECT * FROM lifeSaving WHERE Lake = %s" %("'"+lake+"'")
		print(_q)
		with con:
			cur.execute(_q)
			rows = cur.fetchall()


		"""
		testRow1 = {'time':'Noon','dayofweek':'Monday','body':'Lorem Ipsum'}
		testRow2 = {'time':'9am','dayofweek':'Tuesday','body':'FOO BAR'}
		testRows = testRow1, testRow2;
		"""
		return render.life_all(rows)

if __name__ == "__main__":
    app = webpy.application(urls, globals())
    app.run()
