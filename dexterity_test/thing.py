from five import grok
from plone.directives import form


class IThing(form.Schema):
    form.model('project.xml')

    
class View(grok.View):
    grok.context(IThing)
    grok.require('zope2.View')
