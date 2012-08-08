from django import template
from django.utils.html import escape
from django.contrib.auth.models import User
from django.conf import settings
from django.utils.hashcompat import md5_constructor

import urllib

"""
Copyright (c) 2008, James Tauber
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are
met:

    * Redistributions of source code must retain the above copyright
      notice, this list of conditions and the following disclaimer.
    * Redistributions in binary form must reproduce the above
      copyright notice, this list of conditions and the following
      disclaimer in the documentation and/or other materials provided
      with the distribution.
    * Neither the name of the author nor the names of other
      contributors may be used to endorse or promote products derived
      from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
"AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR
A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT
OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL,
SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT
LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY
THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
(INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

GRAVATAR_URL_PREFIX = getattr(settings, "GRAVATAR_URL_PREFIX", "http://www.gravatar.com/")
GRAVATAR_DEFAULT_IMAGE = getattr(settings, "GRAVATAR_DEFAULT_IMAGE", "")

register = template.Library()

def get_user(user):
    if not isinstance(user, User):
        try:
            user = User.objects.get(username=user)
        except User.DoesNotExist:
            # TODO: make better? smarter? strong? maybe give it wheaties?
            raise Exception, "Bad user for gravatar."
    return user

def gravatar_for_email(email, size=80):
    url = "%savatar/%s/?" % (GRAVATAR_URL_PREFIX, md5_constructor(email).hexdigest())
    url += urllib.urlencode({"s": str(size), "default": GRAVATAR_DEFAULT_IMAGE})
    return escape(url)

def gravatar_for_user(user, size=80):
    user = get_user(user)
    return gravatar_for_email(user.email, size)

def gravatar_img_for_email(email, size=80):
    url = gravatar_for_email(email, size)
    return """<img src="%s" height="%s" width="%s"/>""" % (escape(url), size, size)

def gravatar_img_for_user(user, size=80):
    user = get_user(user)
    url = gravatar_for_user(user)
    return """<img src="%s" alt="Avatar for %s" height="%s" width="%s"/>""" % (escape(url), user.username, size, size)

def gravatar(user, size=80):
    # backward compatibility
    return gravatar_img_for_user(user, size)

register.simple_tag(gravatar)
register.simple_tag(gravatar_for_user)
register.simple_tag(gravatar_for_email)
register.simple_tag(gravatar_img_for_user)
register.simple_tag(gravatar_img_for_email)