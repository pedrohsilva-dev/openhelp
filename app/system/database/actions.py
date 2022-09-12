def shell_context(app, db, *models):
    '''
    Creates a shell context wrapper to flask cli
    :param app: application object
    :param db: database ORM instance
    :param models: list of model objects
    '''
    models = dict((m.__name__, m) for m in models)
    return dict(app=app, db=db, **models)
