"""
plugin.py

Base plugin for Grouper plugins. These are plugins that can be written to extend Grouper
functionality.
"""

from annex import Annex

Plugins = []


class PluginsAlreadyLoaded(Exception):
    pass


def load_plugins(plugin_dir):
    """Load plugins from a directory"""
    global Plugins
    if Plugins:
        raise PluginsAlreadyLoaded("Plugins already loaded; can't load twice!")
    Plugins = Annex(BasePlugin, [plugin_dir], raise_exceptions=True)


class BasePlugin(object):
    def start_request(self, request):
        """Called when a request is started; note that other plugins may have their method called before the request is actually processed; order is not guaranteed.

        returns some data to be used in "finish_request" (optional)
        """
        return None

    def finish_request(self, request, data):
        """Called when the given requests completes with the data returned from "start_request", if applicable."""
        pass

    def user_created(self, user):
        """Called when a new user is created

        When new users enter into Grouper, you might have reason to set metadata on those
        users for some reason. This method is called when that happens.

        Args:
            user (models.User): Object of new user.

        Returns:
            The return code of this method is ignored.
        """
        pass
