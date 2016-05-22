class AppRouter(object):

    def db_for_read(self, model, **hints):
        '''
        Route the cbng_review app to the review database
        and the cbng_report app to the bot database
        :param model:
        :param hints:
        :return:
        '''
        if model._meta.app_label == 'cbng_review':
            return 'review'
        if model._meta.app_label == 'cbng_report':
            return 'bot'
        return None

    def db_for_write(self, model, **hints):
        '''
        Route the cbng_review app to the review database
        and the cbng_report app to the bot database
        :param model:
        :param hints:
        :return:
        '''
        if model._meta.app_label == 'cbng_review':
            return 'review'
        if model._meta.app_label == 'cbng_report':
            return 'bot'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        return None

    def allow_syncdb(self, db, model):
        '''
        Prevent the migration of the bot database

        :param db:
        :param model:
        :return:
        '''
        if model._meta.app_label == 'cbng_report':
            return False
        return None
