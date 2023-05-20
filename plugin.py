import sublime
import sublime_plugin


class ToggleDebugModeCommand(sublime_plugin.ApplicationCommand):

    enabled = False

    def description(self):
        return '%s Debug Mode' % ('Disable' if self.enabled else 'Enable',)

    def run(self):
        self.enabled = not self.enabled

        sublime.log_commands(self.enabled)
        sublime.log_input(self.enabled)
        sublime.log_result_regex(self.enabled)

        if int(sublime.version()) >= 3009:
            sublime.log_indexing(self.enabled)

        if int(sublime.version()) >= 3076:
            sublime.log_build_systems(self.enabled)

        if int(sublime.version()) >= 4064:
            sublime.log_control_tree(self.enabled)

        if int(sublime.version()) >= 4075:
            sublime.log_fps(self.enabled)
