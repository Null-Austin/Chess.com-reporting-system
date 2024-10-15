import json
import checkuser
import jinja2
import report

def render_temp(file_name,**context): #https://stackoverflow.com/questions/30382187/render-jinja2-template-without-a-flask-context

    return jinja2.Environment(
        loader=jinja2.FileSystemLoader('templates/')
    ).get_template(file_name).render(context)

def returnhtml(username):
    if checkuser.requestuser(username) == True:
        return(render_temp('user.html',username=username,reports=report.getreports(username)))
    else:
        return(render_temp('nouser.html',username=username))