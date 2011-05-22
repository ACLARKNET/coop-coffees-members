## Script (Python) "test2"
##bind container=container
##bind context=context
##bind namespace=
##bind script=script
##bind subpath=traverse_subpath
##parameters=
##title=test2
##
print [ s.strip() for s in container.config_links_dynamicportlet.Description().split('\n') if len(s.strip()) > 0 and s.strip()[0] != '#' ]
return printed
