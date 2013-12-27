# Copyright 2013 Jon Moore
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

import logging
import mimeparse.mimeparse as mimeparse
import os
import urlparse
import webapp2

from google.appengine.ext.webapp import template

from views.etag_view import EtagView
from views.html_view import HtmlView
from views.xml_view import AtomServiceDocumentView
import servicedoc

class HomeHandler(webapp2.RequestHandler):
    def _get_baseurl(self):
        parts = urlparse.urlparse(self.request.url)
        return "%s://%s" % (parts.scheme, parts.netloc)

    def get(self):
        supported_mtypes = ['application/atomsvc+xml',
                            'application/xml',
                            'text/html']
        if 'Accept' in self.request.headers:
            accept_hdr = self.request.headers['Accept']
        else:
            accept_hdr = '*/*'
        best_mtype = mimeparse.best_match(supported_mtypes, accept_hdr)
        if best_mtype == 'text/html':
            view = HtmlView("home.html", {})
        else:
            baseurl = self._get_baseurl()
            view = AtomServiceDocumentView(servicedoc.generate_service_doc(baseurl))

        view = EtagView(view)
        self.response.headers['Content-Type'] = view.get_content_type()
        view.render(self.response.out)
        self.response.headers['Etag'] = "\"%s\"" % (view.get_etag(),)
