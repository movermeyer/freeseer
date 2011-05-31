#!/usr/bin/python
# -*- coding: utf-8 -*-

# freeseer - vga/presentation capture software
#
#  Copyright (C) 2010  Free and Open Source Software Learning Centre
#  http://fosslc.org
#
#  This program is free software: you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation, either version 3 of the License, or
#  (at your option) any later version.
#
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this program.  If not, see <http://www.gnu.org/licenses/>.

# For support, questions, suggestions or any other inquiries, visit:
# http://wiki.github.com/fosslc/freeseer/

import scp

def uploadFile(host, user, password, sourcePath, destinationPath):
    #client = scp.Client(host, user, keyfile)
    
    #client = scp.Client(host, user)
    #client.use_system_keys()
    
    client = scp.Client(host=host, user=user, password=password)
    client.transfer(sourcePath, destinationPath)

if __name__ == "__main__":
    host = input("Please enter a host:")
    user = input("Please enter a username:")
    password = input("Please enter a password:")
    uploadFile (host, user, password, './new.txt', '/home/mathieu/')