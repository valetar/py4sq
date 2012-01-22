from foursquare import Foursquare, FoursquareAuth

cid = 'KJITBPO4H14VL234I5JV4LPWBGIJXGMGSSHDZCZ2MGGYJQ53'
cs = 'G5AHKPQNGP2M0QQOJYJZNQQICRU4XOJFGE1TGOZATT2QIW4Y'

ruri = 'http://highscorehero.appspot.com/auth'

def query_4sq():
    foursq_auth = FoursquareAuth(cid, cs, ruri)
    foursq_api = Foursquare(foursq_auth)
    return foursq_api.request('venues',
	                    resource_id='4b4f1ef3f964a520c2fa26e3',
                        #aspect='', 
                        #ll='48.7,9.1', 
                        #limit=1, 
                        locale='de',
                        #query='edelight'
                        )
	
if __name__ == "__main__":
    import pprint
    pprint.pprint(query_4sq())
