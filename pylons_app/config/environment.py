"""Pylons environment configuration"""
import logging
import os

from mako.lookup import TemplateLookup
from pylons.configuration import PylonsConfig
from pylons.error import handle_mako_error
from sqlalchemy import engine_from_config

import pylons_app.lib.app_globals as app_globals
import pylons_app.lib.helpers
from pylons_app.config.routing import make_map
from pylons_app.model import init_model

log = logging.getLogger(__name__)

def load_environment(global_conf, app_conf):
    """Configure the Pylons environment via the ``pylons.config``
    object
    """
    config = PylonsConfig()
    
    # Pylons paths
    root = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    paths = dict(root=root,
                 controllers=os.path.join(root, 'controllers'),
                 static_files=os.path.join(root, 'public'),
                 templates=[os.path.join(root, 'templates')])

    # Initialize config with the basic options
    config.init_app(global_conf, app_conf, package='pylons_app', paths=paths)

    config['routes.map'] = make_map(config)
    config['pylons.app_globals'] = app_globals.Globals(config)
    config['pylons.h'] = pylons_app.lib.helpers
    
    # Setup cache object as early as possible
    import pylons
    pylons.cache._push_object(config['pylons.app_globals'].cache)
    

    # Create the Mako TemplateLookup, with the default auto-escaping
    config['pylons.app_globals'].mako_lookup = TemplateLookup(
        directories=paths['templates'],
        error_handler=handle_mako_error,
        module_directory=os.path.join(app_conf['cache_dir'], 'templates'),
        input_encoding='utf-8', default_filters=['escape'],
        imports=['from webhelpers.html import escape'])

    #sets the c attribute access when don't existing attribute ar accessed
    config['pylons.strict_tmpl_context'] = False
    
    #MULTIPLE DB configs
    # Setup the SQLAlchemy database engine
#    if config['debug']:
#        #use query time debugging.
#        from pylons_app.lib.timer_proxy import TimerProxy
#        sa_engine_db1 = engine_from_config(config, 'sqlalchemy.db1.',
#                                                            proxy=TimerProxy())
#    else:
#        sa_engine_db1 = engine_from_config(config, 'sqlalchemy.db1.')

    #init_model(sa_engine_db1)

    # CONFIGURATION OPTIONS HERE (note: all config options will override
    # any Pylons config options)
    
    return config
