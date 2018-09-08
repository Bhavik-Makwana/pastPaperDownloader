import requests
import config

session = requests.Session()                                                            # start a session
login_url = "https://websignon.warwick.ac.uk/origin/slogin?shire=https%3A%2F%2Fwww2.warwick.ac.uk%2Fsitebuilder2%2Fshire-read&providerId=urn%3Awww2.warwick.ac.uk%3Asitebuilder2%3Aread%3Aservice&target=https%3A%2F%2Fwarwick.ac.uk%2Fservices%2Fexampapers&status=notloggedin"
session.get(login_url)                                                                  # go to login url page 
session.post(login_url, data={'userName': config.WARWICK_USERNAME,                      # login to form, retrieving login details from a config.py file 
                              'password': config.WARWICK_PASSWORD
                             })

# get paper details
module = input("Please enter the module number: ")
year = input("Please enter the paper year: ")

# get save locatiom
download_loc = #input("Please enter the file path save location: ")

r = session.get("https://warwick.ac.uk/services/exampapers/cs/"+year+"/"+module+".pdf") # go to pdf location, site uses basic php to navigate to the pdf lcoations so can be easily accessed via url

'''
    If statement to be expanded to deal with multiple error code responses, 
    e.g. file not found, permission denied
'''
if (r.status_code == 200):
    with open(download_loc, 'wb') as f:  
        f.write(r.content)
    print("File saved successfully")
else: 
    # Retrieve HTTP meta-data                                                                
    print(r.status_code,"error, please make sure you have entered the correct module and year")
    print(r.headers['content-type'])  
    print(r.encoding)  

