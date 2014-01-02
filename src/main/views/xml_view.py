# Copyright 2013 Jon Moore
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

from abstract_view import AbstractView

class XmlView(AbstractView):
    def __init__(self, doc):
        self._doc = doc

    def get_content_type(self):
        return "application/xml;charset=utf-8"

    def render(self, out):
        out.write(etree.tostring(self._doc, encoding='UTF-8'))

class AtomServiceDocumentView(XmlView):
    def get_content_type(self):
        return "application/atomsvc+xml;charset=utf-8"
