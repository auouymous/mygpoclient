# -*- coding: utf-8 -*-
# gpodder.net API Client
# Copyright (C) 2009-2010 Thomas Perl
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
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

__version__ = '1.2'
__url__ = 'http://thpinfo.com/2010/mygpoclient/'

# Default settings for the API client (server hostname and API version)
HOST = 'gpodder.net'
VERSION = 2
TOPLIST_DEFAULT = 50

# You can overwrite this value from your application if you want
user_agent = 'mygpoclient/%s (+%s)' % (__version__, __url__)

