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

from abstract_view import AbstractView
from hashbuf import HashingWriteBuffer

class EtagView(AbstractView):
    def __init__(self, wrapped):
        self._wrapped = wrapped
        self._etag = None

    def get_content_type(self): return self._wrapped.get_content_type()
    
    def render(self, out):
        f = HashingWriteBuffer(out)
        self._wrapped.render(f)
        self._etag = f.hexdigest()
    
    def get_etag(self):
        return self._etag
