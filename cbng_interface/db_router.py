class AppRouter(object):
    def db_for_read(self, model, **hints):
        '''
        Route the cbng_review app to the review database
        and the cbng_report app to the bot database
        :param model:
        :param hints:
        :return:
        '''
        if model._meta.app_label == 'cbng_report':
            return 'bot'
        return 'default'

    def db_for_write(self, model, **hints):
        '''
        Route the cbng_review app to the review database
        and the cbng_report app to the bot database
        :param model:
        :param hints:
        :return:
        '''
        if model._meta.app_label == 'cbng_report':
            return 'bot'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        '''
        Prevent relationships between the external apps
        :param obj1:
        :param obj2:
        :param hints:
        :return:
        '''
        if obj1._meta.app_label == 'cbng_report' and obj2._meta.app_label != 'cbng_report':
            return False
        if obj2._meta.app_label == 'cbng_report' and obj1._meta.app_label != 'cbng_report':
            return False

        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'cbng_report':
            return False
        return None
