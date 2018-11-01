from Database import Challenge
import hashlib
from Persister import Persister

persister = Persister()

class ChallengeApi():
	def __init__(self):
		print("creating challengeApi")

	def getAllChallenges(self):
		challenges = persister.getAllChallenges()
		returnData = []
		for entry in challenges:
			challenge = {}
			ownerUser = persister.getUserById(entry.owner)
			challenge['id'] = entry.id
			challenge['ownerId'] = entry.owner
			challenge['title'] = entry.title
			challenge['description'] = entry.description
			challenge['deadLine'] = entry.deadLine
			challenge['createdAt'] = entry.createdAt
			challenge['contactInfo'] = entry.contactInfo
			challenge['owner'] = ownerUser.name
			challenge['profilePhoto'] = ownerUser.profilePhoto
			challenge['organisation'] = ownerUser.organisation
			returnData.append(challenge)
		return returnData