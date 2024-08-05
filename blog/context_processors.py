def breadcrumbs(request):
    path = request.path.strip('/').split('/')
    breadcrumbs = [
        {'name':'Home', 'url':'/'}
    ]
    for i,p in enumerate(path):
        url = '/' + '/'.join(path[:i+1])+'/'
        breadcrumbs.append({'name':p.capitalize(), 'url':url})
    return {'breadcrumbs':breadcrumbs}
