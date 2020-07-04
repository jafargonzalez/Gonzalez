def index(TemplateEngine,Id=None):
    dictionary = {"title": "rotic",
                  "lable_name": "name:"}
    result = TemplateEngine.Engine(TemplateEngine,"Views/home.html", dictionary)
    return result