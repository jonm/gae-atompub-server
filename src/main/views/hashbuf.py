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

import hashlib

class HashingWriteBuffer:
    def __init__(self, f):
        self._f = f
        self._hash = hashlib.md5()
        try:
            self.closed = f.closed
        except AttributeError:
            self.closed = False

    def write(self, s):
        self._f.write(s)
        self._hash.update(s)

    def close(self):
        self._f.close()
        self.closed = True

    def flush(self): self._f.flush()
    def fileno(self): return self._f.fileno()
    def isatty(self): return self._f.isatty()
    def next(self): return self._f.next()

    def read(self, sz=None):
        bytes = self._f.read(sz)
        self._hash.update(bytes)
        return bytes

    def readline(self, sz=None):
        bytes = self._f.readline(sz)
        self._hash.update(bytes)
        return bytes
    
    def readlines(self, sz=None):
        lines = self._f.readlines()
        for line in lines:
            self._hash.update(line)
        return lines

    def seek(self, offset, whence=None):
        self._f.seek(offset, whence)

    def tell(self): return self._f.tell()

    def truncate(self, sz=None):
        self._f.truncate(sz)

    def writelines(self, seq):
        for line in seq:
            self._hash.update(line)
            self._f.write(line)

    def hexdigest(self):
        return self._hash.hexdigest()

