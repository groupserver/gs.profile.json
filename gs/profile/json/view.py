# -*- coding: utf-8 -*-
############################################################################
#
# Copyright © 2015 OnlineGroups.net and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
############################################################################
from __future__ import absolute_import, unicode_literals
from collections import OrderedDict
from json import dumps as dump_json
from zope.cachedescriptors.property import Lazy
from gs.profile.email.base.interfaces import IGSEmailUser
from gs.profile.view.page import GSProfileView


class JSONView(GSProfileView):
    'The JSON view of a profile'

    @Lazy
    def emailUser(self):
        retval = IGSEmailUser(self.user)
        return retval

    def __call__(self):
        outDict = OrderedDict()
        outDict['id'] = self.userInfo.id

        for propId in self.props.keys():
            val = self.get_property(propId)
            outDict[propId] = val

        outDict['email'] = self.emailUser.get_verified_addresses()

        self.request.response.setHeader(b'Content-Type',
                                        b'application/json')
        retval = dump_json(outDict)
        return retval
