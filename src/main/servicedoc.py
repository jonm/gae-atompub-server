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

try:
    from lxml import etree
except ImportError:
    import xml.etree.ElementTree as etree

APP_NS = 'http://www.w3.org/2007/app'
ATOM_NS = 'http://www.w3.org/2005/Atom'

def generate_service_doc(baseurl):
    doc = etree.Element("{%s}service" % APP_NS)
    doc.attrib['xml:base'] = baseurl
    ws = etree.Element("{%s}workspace" % APP_NS)
    doc.append(ws)
    title = etree.Element("{%s}title" % ATOM_NS)
    title.text = "Default Workspace"
    ws.append(title)
    coll = etree.Element("{%s}collection" % APP_NS)
    coll.attrib['href'] = '/posts'
    ctitle = etree.Element("{%s}title" % ATOM_NS)
    ctitle.text = "Posts"
    coll.append(ctitle)
    accept = etree.Element("{%s}accept" % APP_NS)
    accept.text = "*/*"
    coll.append(accept)
    ws.append(coll)
    return etree.tostring(doc)
