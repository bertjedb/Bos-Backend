from Database import NecessitiesRequest
import hashlib
from Persister import Persister
import datetime

persister = Persister()

class NecessitiesRequestApi():
	def __init__(self):
		print("creating necessitiesRequestApi")

	def makeRequest(self, owner, title, description, necessity, offered, picture):
		if persister.checkUserExists(owner):
			requestObject = NecessitiesRequest(	owner=owner,
												title=title,
												description=description,
												necessity=necessity,
												offered=offered,
												picture=picture,
												createdAt=datetime.datetime.now())
			return persister.storeObject(requestObject)
		return False

	def getRequestById(self, id):
		dbObject = persister.getRequestById(id)
		if dbObject != False:
			request = {
				"id": dbObject.id,
				"owner": dbObject.owner,
				"title": dbObject.title,
				"description": dbObject.description,
				"necessity": dbObject.necessity,
				"createdAt": dbObject.createdAt
			}
			return request
		return False

	def getAllRequests(self):
		requests = persister.getAllRequests()
		returnData = []
		for entry in requests:
			request = {}
			ownerUser = persister.getUserById(entry.owner)
			request['id'] = entry.id
			request['owner'] = ownerUser.name
			request['ownerId'] = entry.owner
			request['title'] = entry.title
			request['description'] = entry.description
			request['necessity'] = entry.necessity
			request['createdAt'] = entry.createdAt
			request['profilePhoto'] = ownerUser.profilePhoto
			request['location'] = ownerUser.locationCity
			request['offered'] = entry.offered
			request['picture'] = entry.picture
			returnData.append(request)
		return returnData