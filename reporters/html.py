# This program is free software; you can redistribute it and/or modify it under
# the terms of the GNU General Public License as published by the Free Software
# Foundation; either version 2 of the License, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
# FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with
# this program; if not, write to the Free Software Foundation, Inc.,
# 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
""" Copyright (c) 2002-2006 LOGILAB S.A. (Paris, FRANCE).
 http://www.logilab.fr/ -- mailto:contact@logilab.fr

HTML reporter
"""

__revision__ = "$Id: html.py,v 1.14 2006-03-08 15:53:41 syt Exp $"

import sys
from cgi import escape

from logilab.common.ureports import HTMLWriter, Section, Table

from pylint.interfaces import IReporter
from pylint.reporters import BaseReporter


class HTMLReporter(BaseReporter):
    """report messages and layouts in HTML
    """

    __implements__ = IReporter
    extension = 'html'
    
    def __init__(self, output=sys.stdout):
        BaseReporter.__init__(self, output)
        self.msgs = []

    def add_message(self, msg_id, location, msg):
        """manage message of different type and in the context of path"""
        module, obj, line = location[1:]
        if self.include_ids:
            sigle = msg_id
        else:
            sigle = msg_id[0]
        self.msgs += [sigle, module, obj, str(line), escape(msg)]

    def _display(self, layout):
        """launch layouts display
        
        overriden from BaseReporter to add a blank line...
        """
        if self.msgs:
            # add stored messages to the layout
            msgs = ['type', 'module', 'object', 'line', 'message']
            msgs += self.msgs
            sect = Section('Messages')
            layout.append(sect)
            sect.append(Table(cols=5, children=msgs, rheaders=1))
            self.msgs = []
        HTMLWriter().format(layout, self.out)
