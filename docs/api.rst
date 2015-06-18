:mod:`gs.profile.json` API
==========================

The :mod:`gs.profile.json` module provides three utility
functions that provide dictionaries that can be easily converted
into a JSON object.

.. function:: user_info(siteInfo, userInfo)

   Turn a  user-info object into a dictionary

   :param siteInfo: The site-information object
   :type siteInfo: :class:`Products.GSContent.interfaces.IGSSiteInfo`
   :param userInfo: The user-information object
   :type userInfo: :class:`Products.GSProfile.interfaces.IGSUserInfo`
   :returns: A dictionary:

      * ``id``: the user-identifier
      * ``name``: the name of the user
      * ``url``: the URL of the profile page

   :rtype: collections.OrderedDict

.. function:: groups(siteInfo, userInfo)

   Get the groups that a person belongs to on a site

   :param siteInfo: The site-information object
   :type siteInfo: :class:`Products.GSContent.interfaces.IGSSiteInfo`
   :param userInfo: The user-information object
   :type userInfo: :class:`Products.GSProfile.interfaces.IGSUserInfo`
   :returns: The identifiers for the groups that the user belongs
             to on the site.
   :rtype: A list of strings

.. function:: email_info(siteInfo, userInfo)

   :param siteInfo: The site-information object
   :type siteInfo: :class:`Products.GSContent.interfaces.IGSSiteInfo`
   :param userInfo: The user-information object
   :type userInfo: :class:`Products.GSProfile.interfaces.IGSUserInfo`
   :returns: A dictionary:

      * ``all``: all the email addresses.
      * ``preferred``: the preferred delivery addresses.
      * ``other``: the verified addresses that are not preferred.
      * ``unverified``: the email addresses that are yet to be
        verified.

   :rtype: collections.OrderedDict

Example
-------

In the following example a ``userInfo`` object is created, and
turned into a dictionary. The list of email addresses and groups
are attached, and the entire thing is converted into a
JSON-formatted string.

.. code-block:: python

   r = {}
   userInfo = createObject('groupserver.UserFromId',
                           self.context, userId)
   if not userInfo.anonymous:
      r = user_info(self.siteInfo, userInfo)
      r['email'] = email_info(self.siteInfo, userInfo)
      r['groups'] = groups(self.siteInfo, userInfo)
   retval = json.dumps(r)
   return retval
