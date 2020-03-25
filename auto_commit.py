#!/usr/bin/python
# -*- coding: UTF-8 -*-
import git
import datetime
repo = git.Repo('C:/Users/max/Desktop/Algorithm')
try:
	print repo.git.add('.')
	comit_info = datetime.date.today() 
	print repo.git.commit('-m',str(comit_info)+' commit')
	print repo.git.push()
except Exception, e:
	print "opps~",e