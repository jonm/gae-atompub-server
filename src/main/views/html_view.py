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
import os

from google.appengine.ext.webapp import template

from abstract_view import AbstractView

class HtmlView(AbstractView):
    def __init__(self, template_name, model):
        self._template_name = template_name
        self._model = model

    def get_content_type(self):
        return "text/html;charset=utf-8"

    def render(self, out):
        basedir = os.path.dirname(__file__)
        t_file = os.path.join(basedir, "..", "templates",
                              self._template_name)
        out.write(template.render(t_file, self._model))
