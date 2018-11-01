from flask import jsonify

from Database import Project, Like
import hashlib
from Persister import Persister
import os
import datetime

persister = Persister()


class ProjectApi():
	def __init__(self):
		print("creating projectApi")

	def getProjectById(self, id):
		return persister.getProjectById(id)

	def addProject(self, title, description, thumbnail, creator, beginDate, endDate):
		if persister.checkUserExists(creator):
			path = "C:/Users/Jelmer/Bos-Backend/thumbnails/"
			mediaPath = path + title + "Base64.txt"
			mediaFile = open(mediaPath, "w+")
			mediaFile.write(thumbnail)
			mediaFile.close()

			currentDate = datetime.datetime.now()

			projectObject = Project(
				title=title,
				description=description,
				thumbnail=mediaPath,
				creator=creator,
				beginDate=beginDate,
				endDate=endDate,
				createdAt=currentDate,
				likes=0
			)
			return persister.storeObject(projectObject)
		return False

	def addLike(self, projectId, userId):
		likeObject = Like(
			project=projectId,
			user=userId
		)
		persister.addLike(projectId)
		return persister.storeObject(likeObject)

	def removeLike(self, id):
		return persister.removeLike(id)

	def totalLikes(self, id):
		return jsonify({"totalLikes": persister.totalLikes(id)})

	def getAllProjects(self):
		projects = persister.getAllProjects()
	
		result = []
		if len(projects) != 0:
			for item in projects:
				creatorUser = persister.getUserById(item.creator)
				result.append(
					{"id": item.id, "title": item.title, "desc": item.description, "thumbnail": item.thumbnail,
					 "creator": item.creator,
					 "beginDate": item.beginDate, "endDate": item.endDate, "createdAt": item.createdAt,
					 "likes": item.likes, "creatorName": creatorUser.name})
		return result
