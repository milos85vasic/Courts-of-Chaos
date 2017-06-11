from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('Courts-Of-Chaos')


def my_view(request):
    return {'project': 'Courts-Of-Chaos'}
