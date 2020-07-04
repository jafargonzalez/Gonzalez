#!C:\Users\Hossein\AppData\Local\Programs\Python\Python38\Python.exe
from Core.TemplateEngine import TemplateEngine as TemplateEngine
import os
import json
import route


_id = None


path = os.environ.get('REQUEST_URI')
method = os.environ.get('REQUEST_METHOD')

# method = "GET"
# path= "/user"



if path in route.routes:
    if method in route.routes[path]["accepted_method"].split(','):
        controller = route.routes[path]["controller"]
    else:
        controller = "error.method_not_allowed"
else:
    controller = "error.not_found"




controller_items = controller.split('.')
_module = controller_items[0]
_attribute = controller_items[1]






def run(TemplateEngine, Controller, Function, Id):
    Method = getattr(Controller, Function)
    if Id != None:
        return Method(TemplateEngine,Id)
    else:
        return Method(TemplateEngine)


def route(_module, TemplateEngine, _attribute, _id=None):
    module = __import__('Controllers.' + _module)
    instance = getattr(module, _module)
    return run(TemplateEngine, instance, _attribute, _id)

def load_json(file_name):
    with open("Jsons/"+file_name+".json",encoding='utf-8') as json_file:
        return json.load(json_file)

if _module == 'api' :
    print('Content-type: application/json\r\n\r')
    #result = load_json("sample")
    result = "{\"" \
             "name\":\"Gonzalez\"}"
else:
    result = route(_module, TemplateEngine, _attribute, _id)
    print('Content-type: text/html\r\n\r')

if method == 'POST':
    result = os.environ

# print('Content-type: text/html\r\n\r')

print(result)
