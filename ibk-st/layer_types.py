#!/usr/bin/python3

from gi.repository import Gtk, Gdk, GdkPixbuf

class PlaneLayer(object):
    def __init__(self, treestore, treeview):
        self.data_treestore = treestore
        self.data_treeview = treeview
        self.type = "plane"
        self.label = "Plane layer"

        #Great circle / Small circle properties
        self.render_gcircles = True
        self.line_color = "#0000ff"
        self.line_width = 1.0
        self.line_style = "-"
        self.line_alpha = 1.0
        self.capstyle = "butt"

        #Pole properties
        self.render_poles = False
        self.pole_style = "o"
        self.pole_size = 8.0
        self.pole_fill = "#ff7e00"
        self.pole_edge_color = "#000000"
        self.pole_edge_width = 1.0
        self.pole_alpha = 1.0

        #Linear properties
        self.render_linears = True
        self.marker_style = "o"
        self.marker_size = 8.0
        self.marker_fill = "#1283eb"
        self.marker_edge_color = "#000000"
        self.marker_edge_width = 1.0
        self.marker_alpha = 1.0

        self.render_plane_contours = False
        self.render_line_contours = False

    def get_pixbuf(self):
        """
        Takes a color string (format: "#aabbcc") and assigns it to a
        Pixbuf. Pushes the pixbuf.
        Returns a pixbuf that can be assigned to a layer.
        """
        line_color_alpha = int("0x{0}ff".format(
            self.line_color[1:]), base=16)
        self.pixbuf_color = GdkPixbuf.Pixbuf.new(
            GdkPixbuf.Colorspace.RGB, True, 8, 16, 16)
        self.pixbuf_color.fill(line_color_alpha)
        return self.pixbuf_color

    def get_rgba(self):
        """
        Returns the RGBA for lines (great and small circles) of the
        current layer.
        __!!__ does not return alpha yet
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.line_color)
        return rgba.to_color()

    def get_marker_rgba(self):
        """
        Returns the marker RGBA of the current layer.
        __!!__ does not return alpha yet
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.marker_fill)
        return rgba.to_color()

    def get_pole_rgba(self):
        """
        Returns the pole RGBA of the current layer.
        __!!__ does not return alpha yet
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.pole_fill)
        return rgba.to_color()

    def get_pole_edge_rgba(self):
        """
        Returns the pole edge RGBA of the current layer.
        __!!__ does not return alpha yet
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.pole_edge_color)
        return rgba.to_color()

    def get_marker_edge_rgba(self):
        """
        Returns the marker edge RGBA of the current layer.
        __!!__ does not return alpha yet
        """
        rgba = Gdk.RGBA()
        rgba.parse(self.marker_edge_color)
        return rgba.to_color()

    def get_data_treestore(self):
        """
        Returns the data treestore associated with this layer.
        """
        return self.data_treestore

    def get_data_treeview(self):
        """
        Returns the data treeview associated with this layer.
        """
        return self.data_treeview
     
    def get_layer_type(self):
        """
        Returns the layer type of this object.
        """
        return self.type

    def get_line_color(self):
        """
        Returns the line color set for this layer.
        """
        return self.line_color

    def set_line_color(self, new_color):
        """
        Sets a new line color for this layer.
        """
        self.line_color = new_color

    def get_label(self):
        """
        Returns the label assigned to this layer.
        """
        return self.label

    def set_label(self, new_label):
        """
        Sets a new label for the layer.
        """
        self.label = new_label

    def get_line_width(self):
        """
        Returns the line width that is set for this layer.
        """
        return self.line_width

    def set_line_width(self, new_line_width):
        """
        Assigns a new line width to this layer.
        """
        self.line_width = new_line_width

    def get_line_style(self):
        """
        Returns the line style assigned to this layer.
        """
        return self.line_style

    def set_line_style(self, new_line_style):
        """
        Sets a new line style for this layer.
        """
        self.line_style = new_line_style

    def get_capstyle(self):
        """
        Returns the capstyle that is used in this layer.
        """
        return self.capstyle

    def set_capstyle(self, new_capstyle):
        """
        Sets a new capstyle for this layer.
        """
        self.capstyle = new_capstyle

    def get_pole_style(self):
        """
        Returns the pole style of this layer.
        """
        return self.pole_style

    def get_pole_size(self):
        """
        Returns the pole size of this layer.
        """
        return self.pole_size

    def set_pole_size(self, new_pole_size):
        """
        Sets a new pole size for this layer.
        """
        self.pole_size = new_pole_size

    def get_pole_fill(self):
        """
        Returns the pole fill of this layer.
        """
        return self.pole_fill

    def set_pole_fill(self, new_pole_fill):
        """
        Sets a new pole fill for this layer.
        """
        self.pole_fill = new_pole_fill

    def get_pole_edge_color(self):
        """
        Return the pole edge color of this layer.
        """
        return self.pole_edge_color

    def set_pole_edge_color(self, new_pole_edge_color):
        """
        Sets a new pole edge color for this layer.
        """
        self.pole_edge_color = new_pole_edge_color

    def get_pole_edge_width(self):
        """
        Returns the pole edge width of this layer.
        """
        return self.pole_edge_width

    def set_pole_edge_width(self, new_pole_edge_width):
        """
        Sets a new pole edge width of this layer.
        """
        self.pole_edge_width = new_pole_edge_width

    def get_pole_alpha(self):
        """
        Returns the transparency of the pole of this layer.
        """
        return self.pole_alpha

    def get_marker_style(self):
        """
        Returns the marker style set for this layer.
        """
        return self.marker_style

    def get_pole_style(self):
        """
        Returns the pole style set for this layer.
        """
        return self.pole_style

    def set_pole_style(self, new_pole_style):
        """
        Sets a new pole style for this layer.
        """
        self.pole_style = new_pole_style

    def set_marker_style(self, new_marker_style):
        """
        Assigns a new marker style to this layer.
        """
        self.marker_style = new_marker_style

    def get_marker_size(self):
        """
        Returns the marker size of this layer.
        """
        return self.marker_size

    def set_marker_size(self, new_marker_size):
        """
        Sets a new maker size for this layer.
        """
        self.marker_size = new_marker_size

    def get_marker_fill(self):
        """
        Returns the fill color of the makers of this layer.
        """
        return self.marker_fill

    def set_marker_fill(self, new_marker_fill):
        """
        Sets a new fill color for the markers in this layer.
        """
        self.marker_fill = new_marker_fill

    def set_marker_edge_color(self, new_marker_edge_color):
        """
        Sets a new edge color for the markers in this layer.
        """
        self.marker_edge_color = new_marker_edge_color

    def get_marker_edge_width(self):
        """
        Returns the width of the marker edges of this layer.
        """
        return self.marker_edge_width

    def set_marker_edge_width(self, new_marker_edge_width):
        """
        Sets a new edge width for the markers in this layer.
        """
        self.marker_edge_width = new_marker_edge_width

    def get_marker_edge_color(self):
        """
        Returns the color of the marker edges in this layer.
        """
        return self.marker_edge_color

    def set_marker_edge_color(self, new_marker_edge_color):
        """
        Sets a new edge color for the markers in this layer.
        """
        self.marker_edge_color = new_marker_edge_color

    def get_line_alpha(self):
        """
        Returns the transparency of the lines of this layer.
        """
        return self.line_alpha

    def set_line_alpha(self, new_line_alpha):
        """
        Sets a new transparency for the lines of this layer.
        """
        self.line_alpha = new_line_alpha

    def get_marker_alpha(self):
        """
        Returns the transparency of the markers of this layer.
        """
        return self.marker_alpha

    def set_marker_alpha(self, new_marker_alpha):
        """
        Sets a new transparency for the markers of this layer.
        """
        self.marker_alpha = new_marker_alpha

    def get_render_gcircles(self):
        """
        Returns if great circles should be rendered for this layer.
        """
        return self.render_gcircles

    def set_render_gcircles(self, new_render_gcircles_state):
        """
        Sets if great circles should be drawn for this layer.
        """
        self.render_gcircles = new_render_gcircles_state

    def get_render_poles(self):
        """
        Returns if poles should be rendered for this layer.
        """
        return self.render_poles

    def set_render_poles(self, new_render_poles_state):
        """
        Sets if poles should be rendered for this layer.
        """
        self.render_poles = new_render_poles_state

    def get_render_linears(self):
        """
        Returns if linears should be rendered for this layer.
        """
        return self.render_linears

    def set_render_linears(self, new_render_linears_state):
        """
        Sets if linears should be rendered for this layer.
        """
        self.render_linears = new_render_linears_state

    def get_render_plane_contours(self):
        """
        Returns if contours should be drawn for the poles of this layer.
        """
        return self.render_plane_contours

class FaultPlaneLayer(PlaneLayer):
    def __init__(self, treestore, treeview):
        PlaneLayer.__init__(self, treestore, treeview)
        self.type = "faultplane"
        self.label = "Faultplane layer"

class LineLayer(PlaneLayer):
    """
    Inherits some functions and assignments from PlaneLayer, but doesn't use
    all of them. Seems a good way of keeping the class tree flat.
    """
    def __init__(self, treestore, treeview):
        PlaneLayer.__init__(self, treestore, treeview)
        self.type = "line"
        self.label = "Linear layer"

    def get_pixbuf(self):
        """
        Takes a color string (format: "#aabbcc") and assigns it to a
        Pixbuf. Pushes the pixbuf.
        Returns a pixbuf that can be assigned to a layer.
        """
        marker_color_alpha = int("0x{0}ff".format(
            self.marker_fill[1:]), base=16)
        self.pixbuf_color = GdkPixbuf.Pixbuf.new(
            GdkPixbuf.Colorspace.RGB, True, 8, 16, 16)
        self.pixbuf_color.fill(marker_color_alpha)
        return self.pixbuf_color

class SmallCircleLayer(PlaneLayer):
    def __init__(self, treestore, treeview):
        PlaneLayer.__init__(self, treestore, treeview)
        self.type = "smallcircle"
        self.label = "Small circle layer"

