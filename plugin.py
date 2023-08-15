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

    named = {
        'build_system': False,
        'command': False,
        'control_tree': False,
        'fps': False,
        'index': False,
        'input': False,
        'result_regex': False,
    }  # type: dict

    def run(self, logger=None, enable=None) -> None:
        if enable is not None:
            flag = self.enabled = enable
            for named in self.named:
                self.named[named] = flag
        elif logger:
            flag = self.named[logger] = not self.named[logger]
        else:
            flag = self.enabled = not self.enabled
            for named in self.named:
                self.named[named] = flag

        if logger == 'command' or not logger:
            sublime.log_commands(flag)

        if logger == 'input' or not logger:
            sublime.log_input(flag)

        if logger == 'result_regex' or not logger:
            sublime.log_result_regex(flag)

        if int(sublime.version()) >= 3009:
            if logger == 'index' or not logger:
                sublime.log_indexing(flag)

        if int(sublime.version()) >= 3076:
            if logger == 'build_system' or not logger:
                sublime.log_build_systems(flag)

        if int(sublime.version()) >= 4064:
            if logger == 'control_tree' or not logger:
                sublime.log_control_tree(flag)

        if int(sublime.version()) >= 4075:
            if logger == 'fps' or not logger:
                sublime.log_fps(flag)

    def description(self, logger=None) -> str:
        if logger:
            return '%s %s' % ('Disable' if self.named[logger] else 'Enable', logger)

        return '%s Debug Mode' % ('Disable' if self.enabled else 'Enable')
