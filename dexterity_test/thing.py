from five import grok
from plone.directives import form


class IThing(form.Schema):
    form.model('thing.xml')
