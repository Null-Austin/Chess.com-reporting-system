import json
import checkuser
import jinja2

def render_temp(file_name,**context): #https://stackoverflow.com/questions/30382187/render-jinja2-template-without-a-flask-context

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates/')
    ).get_template(file_name).render(context)

def returnhtml(username):
    if checkuser.requestuser(username) == True:
        