import string

class MainConfiguration:
    # We are using this class to only store the configurable entities like URLs or some keys.
    # These properties shall be referenced in multiple other classes.
    
    url_endpoint: string = "https://www.thesportsdb.com/api/v1/json/2/searchplayers.php"