# Copyright (C) 2023 Gerard Roche
#
# This file is part of ToggleDebugMode.
#
# ToggleDebugMode is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# ToggleDebugMode is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with ToggleDebugMode.  If not, see <https://www.gnu.org/licenses/>.

import sublime
import sublime_plugin


class ToggleDebugMode(sublime_plugin.ApplicationCommand):

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
