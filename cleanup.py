
import transaction

from Testing.makerequest import makerequest ; app=makerequest(app) ; import AccessControl; AccessControl.SecurityManagement.newSecurityManager(None, AccessControl.SpecialUsers.system)

site_id = 'coopcoffees'
site = app[site_id]
obj_metatypes = ['ZWiki Page', 'ZWiki', 'Zwiki Outline Cache']

for i in app.ZopeFindAndApply(site, obj_metatypes=obj_metatypes, search_sub=1):
    print i
    relpath = '/'.join(i[0].split('/')[:-1])
    path = site_id + '/' + relpath
    obj_id = i[1].getId()
    app.restrictedTraverse(path).manage_delObjects([obj_id])
    transaction.commit()
