# -*- coding: utf-8 -*-
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
"""
rhodecode.lib.middleware.errormator
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

middleware to handle errormator publishing of errors

:created_on: October 18, 2012
:author: marcink
:copyright: (c) 2013 RhodeCode GmbH.
:license: GPLv3, see LICENSE for more details.
"""


try:
    from errormator_client import make_errormator_middleware
except ImportError:
    Errormator = None
else:
    Errormator = make_errormator_middleware