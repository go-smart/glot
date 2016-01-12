# This file is part of the Go-Smart Simulation Architecture (GSSA).
# Go-Smart is an EU-FP7 project, funded by the European Commission.
#
# Copyright (C) 2013-  NUMA Engineering Ltd. (see AUTHORS file)
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
import os
import pkgutil
import sys


# Check through the current directory for modules and load them. If they contain
# classes extending Family, the FamilyClass metaclass on which it is based will
# add them to the family register
def scan():
    iter_modules = pkgutil.iter_modules([
        os.path.dirname(os.path.realpath(__file__))
    ])

    for loader, name, ispkg in iter_modules:
        if name not in sys.modules:
            loader.find_module(name).load_module(name)
