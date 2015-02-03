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
from functools import reduce
from json import dumps as dump_json
from operator import or_
from zope.cachedescriptors.property import Lazy
from gs.profile.email.base.interfaces import IGSEmailUser
from gs.profile.view.page import GSProfileView


class JSONView(GSProfileView):
    'The JSON view of a profile'

    @Lazy
    def emailUser(self):
        retval = IGSEmailUser(self.user)
        return retval

    def is_admin(self, group):
        roles = self.request.AUTHENTICATED_USER.getRolesInContext(group)
        retval = ('GroupAdmin' in roles) or ('DivisionAdmin' in roles)
        return retval

    @Lazy
    def userOrGroupAdmin(self):
        retval = ((self.loggedInUserInfo.id == self.userInfo.id) or
                  reduce(or_, [self.is_admin(g.groupObj)
                               for g in self.groupMembership()], False))
        return retval

    def __call__(self):
        outDict = OrderedDict()
        outDict['id'] = self.userInfo.id

        if (not self.loggedInUserInfo.anonymous):
            for propId in self.props.keys():
                val = self.get_property(propId)
                outDict[propId] = val

        if self.userOrGroupAdmin:
            outDict['email'] = self.emailUser.get_verified_addresses()
        else:
            outDict['email'] = []

        self.request.response.setHeader(b'Content-Type',
                                        b'application/json')
        retval = dump_json(outDict)
        return retval
