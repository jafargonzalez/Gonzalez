
# this is a controller
# u can copy this and past this in controllers folder
# and rename this to your desired name for creating a new repository
# also u can create a new row in controllers.json file in your root folder
# if u want to assign this controller to a view or to a model or both
def index(TemplateEngine,Id=None):
    dictionary = {"title": "rotic",
                    "lable_name": "name:"}
    result = TemplateEngine.Engine(TemplateEngine,"Views/user.html", dictionary)
    return result

# we will observe rest-api standards  here
def GET():
    pass

def POST():
    pass

def PUT():
    pass

def DELET():
    pass

def GETCOUNT():
    pass

def FINDBYID():
    pass

