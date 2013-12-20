#!/bin/bash
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

git status | egrep "Untracked|modified|deleted|new file"
if [ $? == 0 ]; then
    echo "There are local changes which need to get committed!"
    exit 1
fi

git status | grep "Your branch is ahead"
if [ $? == 0 ]; then
    echo "There are local repo commits which need to get pushed!"
    exit 1
fi
exit 0
