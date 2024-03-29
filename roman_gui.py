#!/usr/bin/env python

# PyRoman - Convert between Roman numeral and integer
# Copyright (C) 2019 ncdulo
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import roman

class RomanWindow(Gtk.Window):

    mode = "numeral"

    def __init__(self):
        # Main Gtk.Window() setup
        Gtk.Window.__init__(self, title="PyRoman")
        
        # Create a new Grid() for layout
        grid = Gtk.Grid()
        self.add(grid)

        # Text labels
        self.label_pyroman = Gtk.Label()
        self.label_input = Gtk.Label()
        self.label_output = Gtk.Label()
        self.label_mode = Gtk.Label()

        self.label_pyroman.set_markup("<big>PyRoman</big>\n© ncdulo 2019")
        self.label_input.set_text("Input:")
        self.label_output.set_text("Output:")
        self.label_mode.set_text("Output Mode:")

        # Text entry
        self.entry_input = Gtk.Entry()
        self.entry_output = Gtk.Entry()

        self.entry_output.set_editable(None)

        # Radio Buttons for mode
        self.modebox = Gtk.Box(spacing=6)
        
        self.button_mode_numeral = Gtk.RadioButton.new_with_label_from_widget(None, "Numeral")
        self.button_mode_integer = Gtk.RadioButton.new_from_widget(self.button_mode_numeral)
        self.button_mode_integer.set_label("Integer")

        self.modebox.pack_start(self.label_mode, False, False, 0)
        self.modebox.pack_end(self.button_mode_numeral, False, False, 0)
        self.modebox.pack_end(self.button_mode_integer, False, False, 0)
        

        # Buttons
        self.button_convert = Gtk.Button(label="Convert")
        self.button_quit = Gtk.Button(label="Quit")

        # Callbacks
        self.button_mode_numeral.connect("toggled", self.on_mode_toggled, "numeral")
        self.button_mode_integer.connect("toggled", self.on_mode_toggled, "integer")
        self.button_convert.connect("clicked", self.on_convert_clicked)
        self.button_quit.connect("clicked", Gtk.main_quit)

        # Add it all to the Grid()

        # Grid.attach(child, left, top, width, height)
        # Grid.attach_next_to(child, sibling, side, width, height)

        # Original grid, reference material
        #grid.add(self.button_convert)
        #grid.attach_next_to(self.button_quit, self.button_convert, Gtk.PositionType.RIGHT, 2, 1)
        #grid.attach(self.label_pyroman, 0, 1, 2, 1)
        # The real grid
        # Top Row (title, description)
        grid.add(self.label_pyroman)

        # Input row
        grid.attach(self.label_input, 0, 1, 1, 1)
        grid.attach_next_to(self.entry_input, self.label_input, Gtk.PositionType.RIGHT, 1, 1)

        # Output row
        grid.attach(self.label_output, 0, 2, 1, 1)
        grid.attach_next_to(self.entry_output, self.label_output, Gtk.PositionType.RIGHT, 1, 1)

        # Mode row
        grid.attach(self.modebox, 0, 4, 2, 2)

        # Button/Command row
        grid.attach(self.button_convert, 0, 6, 1, 1)
        grid.attach_next_to(self.button_quit, self.button_convert, Gtk.PositionType.RIGHT, 2, 1)


    # Callback defs

    # Change conversion mode
    def on_mode_toggled(self, widget, mode):
        self.mode = mode
      
        # Copy output to input. Makes for easy "round trip" conversion
        self.entry_input.set_text(self.entry_output.get_text())

        # I would like to clear the output entry box here. But doing so
        # also clears the input entry box as well. get_text() returns a point
        # so an alternative method will probably need to be used.
        #self.entry_output.set_text("")

    # Convert button has been pressed
    def on_convert_clicked(self, widget):
        input_text = self.entry_input.get_text()
        output_text = ""

        print(input_text, type(input_text), self.mode)

        # Numeral output mode
        if self.mode == "numeral":
            print("to_roman(",int(input_text),")")
            output_text = roman.to_roman(int(input_text))
        # Integer output mode
        elif self.mode == "integer":
            print("from_roman(",input_text,")")
            output_text = roman.from_roman(input_text)

        self.entry_output.set_text(str(output_text))

# Create an instance of our window class and display it
win = RomanWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()

# Enter main GTK event processing loop
Gtk.main()

