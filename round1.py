import json

productDict=dict()
queryDict=dict()
artistDict=dict()


queryJsonFile='query.json'
dataJsonFile='data.json'

def readJson(a):
	return json.loads(a)
	
def addQueryToArtistDict(artist,query):
	try:
		artistHashEntry=artistDict[artist]
		artistHashEntry.add(query["query"])
	except KeyError:
		artistDict[artist]={query["query"]}

def createProductDataStore(dataStr):
	products=readJson(dataStr)
	for product in products:

		pId=product["productId"]
		productDict[pId]=product
def createQueriesDataStore(queryStr):
	queries=readJson(queryStr)
	for query in queries:
		queryStr=query["query"]	
		pId=query["productId"]
		
		artist=productDict[pId]["artist"]
		addQueryToArtistDict(artist,query)
		try:
			queryHashEntry=queryDict[queryStr]
			queryHashEntry.append(query)
		except KeyError :
			queryDict[queryStr]=[query]
		
# print productDict
# print queryDict
# print artistDict



# print '$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$'


def searchProductsForQuery(query):
	try :
		queryHashEntry=queryDict[query]
	except KeyError:
		print 'stderr: new query. did not encounter it earlier'
		return
	for query in queryHashEntry:
		pId = query["productId"]
		product = productDict[pId]
		print product
def searchQueryForArtists(artist):
	try:
		queryStringList=artistDict[artist]
	except KeyError:
		print 'stderr: new artist. did not encounter it earlier'
		return
	for queryString in queryStringList:
		queryList=queryDict[queryString]
		for query in queryList:
			print query
def main():
	queryStr=open(queryJsonFile).read()
#r'[{"query": "Paul Overstreet", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44133},{"query": "Paul Overstreet", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44134},{"query": "Paul Overstreet", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44134},{"query": "Devo", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44135},{"query": "Beastie Boys", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "I Should", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "David Thomas", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "Vida Tem Um So", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "Popular", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "Rantanplan", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "Peace", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137},{"query": "Rond\u00f2 Veneziano", "timestamp": "2012-12-28T00:00:00.045000+00:00", "productId": 44137}]'
	dataStr=open(dataJsonFile).read()
#r'[{"genre": "Popular", "productName": "Gabber Up Your Ass", "artist": "Rob Gee", "productId": 44133},{"genre": "Popular", "productName": "Wanna Be a Gangsta", "artist": "D.O.A.", "productId": 44134},{"genre": "Popular", "productName": "Ya Mutha", "artist": "D.O.A.", "productId": 44135},{"genre": "Popular", "productName": "Cunt Face", "artist": "Bloody Fist", "productId": 44136},{"genre": "Popular", "productName": "Cock Sucker", "artist": "Bloody Fist", "productId": 44137}]'
	createProductDataStore(dataStr)
	createQueriesDataStore(queryStr)

########################## Plug and Play ######################################3
	searchProductsForQuery('Paul Overstreet')
	searchQueryForArtists('D.O.A.')
	
################################################################


if __name__=="__main__":
	main()

