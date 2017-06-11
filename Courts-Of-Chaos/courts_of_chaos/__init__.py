from pyramid.config import Configurator
from courts_of_chaos.resources import get_root


def main(global_config, **settings):
    """ This function returns a WSGI application.
    
    It is usually called by the PasteDeploy framework during 
    ``paster serve``.
    """
    settings = dict(settings)
    settings.setdefault('jinja2.i18n.domain', 'Courts-Of-Chaos')

    config = Configurator(root_factory=get_root, settings=settings)
    config.add_translation_dirs('locale/')
    config.include('pyramid_jinja2')

    config.add_static_view('static', 'static')
    config.add_view('courts_of_chaos.views.my_view',
                    context='courts_of_chaos.resources.MyResource', 
                    renderer="templates/mytemplate.jinja2")

    return config.make_wsgi_app()
