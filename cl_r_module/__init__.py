# -*- coding: utf-8 -*-
"""
/***************************************************************************
 cl_r
                                 A QGIS plugin
 cl_r
 Generated by Plugin Builder: http://g-sherman.github.io/Qgis-Plugin-Builder/
                             -------------------
        begin                : 2022-12-08
        copyright            : (C) 2022 by A
        email                : A
        git sha              : $Format:%H$
 ***************************************************************************/

/***************************************************************************
 *                                                                         *
 *   This program is free software; you can redistribute it and/or modify  *
 *   it under the terms of the GNU General Public License as published by  *
 *   the Free Software Foundation; either version 2 of the License, or     *
 *   (at your option) any later version.                                   *
 *                                                                         *
 ***************************************************************************/
 This script initializes the plugin, making it known to QGIS.
"""


# noinspection PyPep8Naming
def classFactory(iface):  # pylint: disable=invalid-name
    """Load cl_r class from file cl_r.

    :param iface: A QGIS interface instance.
    :type iface: QgsInterface
    """
    #
    from .cl_r import cl_r
    return cl_r(iface)