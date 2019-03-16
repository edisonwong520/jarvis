import os
import importlib


class Platform:
    def __init__(self):
        self.plugin_list = self.get_all_plugin()

    def load_plugins(self, name, args):

        for filename in self.plugin_list:
            if filename == name:

                pluginName = os.path.splitext(filename)[0]

                try:
                    plugin = importlib.import_module('plugins.{}'.format(pluginName))
                    # plugin=__import__("plugins."+pluginName, fromlist=[pluginName])
                    # Errors may be occured. Handle it yourself.
                    print("load plugin name:" + name)

                    plugin.run(args)

                except Exception as e:
                    print("Error!" + str(e))
                    break

    def get_all_plugin(self):
        plugin_list = []
        for filename in os.listdir("plugins"):
            if not filename.startswith("__"):
                if not filename.startswith("."):
                    plugin_list.append(filename[:-3])

        return plugin_list
