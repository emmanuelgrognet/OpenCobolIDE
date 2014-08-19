# Copyright (c) <2013-2014> Colin Duquesnoy
#
# This file is part of OpenCobolIDE.
#
# OpenCobolIDE is free software: you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation, either version 3 of the License, or (at your option) any later
# version.
#
# OpenCobolIDE is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# OpenCobolIDE. If not, see http://www.gnu.org/licenses/.
"""
Gives an easy and safe access to the app settings
"""
import os
import sys
from pyqode.core.qt import QtCore, QtGui
from pyqode.core.qt.QtCore import QSettings
# from .constants import CobolStandard


class Settings(object):
    def __init__(self):
        self._settings = QSettings("OpenCobolIDE", "OpenCobolIDE")

    def clear(self):
        self._settings.clear()

    # Geometry and state (visible windows, ...) + working settings (last path)
    # ------------------------------------------------------------------------
    @property
    def geometry(self):
        v = self._settings.value("mainWindowGeometry")
        if v:
            return bytes(v)
        return None

    @geometry.setter
    def geometry(self, geometry):
        self._settings.setValue("mainWindowGeometry", geometry)

    @property
    def state(self):
        v = self._settings.value("mainWindowState")
        if v:
            return bytes(v)
        return None

    @state.setter
    def state(self, state):
        self._settings.setValue("mainWindowState", state)

    @property
    def maximised(self):
        return bool(int(self._settings.value("maximised", "0")))

    @maximised.setter
    def maximised(self, value):
        self._settings.setValue("maximised", int(value))

    @property
    def fullscreen(self):
        return bool(int(self._settings.value("fullscreen", "0")))

    @fullscreen.setter
    def fullscreen(self, value):
        self._settings.setValue("fullscreen", int(value))

    @property
    def size(self):
        return self._settings.value("size", QtCore.QSize(1200, 800))

    @size.setter
    def size(self, value):
        self._settings.setValue("size", value)

    @property
    def outline_visible(self):
        return bool(int(self._settings.value("navigationPanelVisible", "1")))

    @outline_visible.setter
    def outline_visible(self, value):
        self._settings.setValue("navigationPanelVisible", int(value))

    @property
    def last_path(self):
        """
        Returns the last used open/save path
        """
        default_value = ""
        if sys.platform == "win32":
            default_value = "c:\\"
        return self._settings.value("lastUsedPath", default_value)

    @last_path.setter
    def last_path(self, path):
        """
        Sets the last used path (save or open path):

        :param path: path string
        :type path: str or unicode
        """
        self._settings.setValue("lastUsedPath", os.path.dirname(path))

    #
    # Editor settings settings
    #
    @property
    def display_lines(self):
        return bool(int(self._settings.value('displayLineNumbers', '1')))

    @display_lines.setter
    def display_lines(self, value):
        self._settings.setValue('displayLineNumbers', int(value))

    @property
    def highlight_caret(self):
        return bool(int(self._settings.value('highlightCurrentLine', '1')))

    @highlight_caret.setter
    def highlight_caret(self, value):
        self._settings.setValue('highlightCurrentLine', int(value))

    @property
    def highlight_matching(self):
        return bool(int(self._settings.value('highlightMatchingBraces', '1')))

    @highlight_matching.setter
    def highlight_matching(self, value):
        self._settings.setValue('highlightMatchingBraces', int(value))

    @property
    def show_whitespaces(self):
        return bool(int(self._settings.value('highlightWhitespaces', '0')))

    @show_whitespaces.setter
    def show_whitespaces(self, value):
        self._settings.setValue('highlightWhitespaces', int(value))

    @property
    def tab_len(self):
        return int(self._settings.value('tabWidth', '4'))

    @tab_len.setter
    def tab_len(self, value):
        self._settings.setValue('tabWidth', int(value))

    @property
    def enable_autoindent(self):
        return bool(int(self._settings.value('enableAutoIndent', '1')))

    @enable_autoindent.setter
    def enable_autoindent(self, value):
        self._settings.setValue('enableAutoIndent', int(value))

    @property
    def code_completion_trigger(self):
        return int(self._settings.value('ccTriggerLen', '1'))

    @code_completion_trigger.setter
    def code_completion_trigger(self, value):
        self._settings.setValue('ccTriggerLen', value)

    #
    # Editor style settings
    #
    @property
    def dark_style(self):
        return bool(int(self._settings.value("dark_style", "0")))

    @dark_style.setter
    def dark_style(self, value):
        self._settings.setValue("dark_style", value)

    @property
    def font(self):
        font = self._settings.value("fontName")
        if not font:
            font = "Adobe Source Code"
        return font

    @font.setter
    def font(self, font):
        self._settings.setValue("fontName", font)

    @property
    def font_size(self):
        return int(self._settings.value('fontSize', '10'))

    @font_size.setter
    def font_size(self, value):
        self._settings.setValue('fontSize', value)

    @property
    def color_scheme(self):
        return self._settings.value('colorScheme', 'qt')

    @color_scheme.setter
    def color_scheme(self, value):
        self._settings.setValue('colorScheme', value)

    # Build and Run settings
    # ----------------------
    @property
    def external_terminal(self):
        return bool(int(self._settings.value('runInShell', "0")))

    @external_terminal.setter
    def external_terminal(self, value):
        self._settings.setValue('runInShell', int(value))

    @property
    def external_terminal_command(self):
        # works on gnome, what about KDE and how do I detect that?
        # at the moment just go with gnome, user can change that in the
        # settings dialog anyway
        default_shell_cmd = "gnome-terminal -e"
        return str(self._settings.value("shell", default_shell_cmd))

    @external_terminal_command.setter
    def external_terminal_command(self, cmd):
        self._settings.setValue("shell", cmd)

    @property
    def custom_compiler_path(self):
        return self._settings.value('customCompilerPath', '')

    @custom_compiler_path.setter
    def custom_compiler_path(self, value):
        # add to PATH
        sep = ';' if sys.platform == 'win32' else ':'
        os.environ['PATH'] += sep + value
        self._settings.setValue('customCompilerPath', value)


    # Cobol settings
    # ----------------------
    @property
    def free_format(self):
        return bool(int(self._settings.value('free_format', '0')))

    @free_format.setter
    def free_format(self, value):
        self._settings.setValue('free_format', int(value))

    @property
    def comment_indicator(self):
        return self._settings.value('comment_indicator', '*> ')

    @comment_indicator.setter
    def comment_indicator(self, value):
        self._settings.setValue('comment_indicator', value)

    # @property
    # def cobol_standard(self):
    #     return CobolStandard(int(self._settings.value('cobc_standard', '0')))
    #
    # @cobol_standard.setter
    # def cobol_standard(self, value):
    #     self._settings.setValue('cobc_standard', int(value))
