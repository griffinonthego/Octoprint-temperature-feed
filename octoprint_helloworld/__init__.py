import octoprint.plugin
import os
import time

class HelloWorldPlugin(octoprint.plugin.StartupPlugin,
                       octoprint.plugin.TemplatePlugin,
                       octoprint.plugin.SettingsPlugin):
    def on_after_startup(self):
        self._logger.info("Hello World! (more: %s)" % self._settings.get(["url"]))

    def get_settings_defaults(self):
        # stream = os.popen('python3 ~/examples/get_temp2.py')
        stream = os.popen('echo test')
        output = stream.read()
        stream.close()
        return dict(url="https://en.wikipedia.org/wiki/Hello_world", test=output)

    def get_template_configs(self):
        return [
            dict(type="navbar", custom_bindings=False),
            dict(type="settings", custom_bindings=False)
        ]

__plugin_name__ = "Hello World"
__plugin_pythoncompat__ = ">=3.7,<4"
__plugin_implementation__ = HelloWorldPlugin()
