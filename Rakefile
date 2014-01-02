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

# Rakefile for gae-atompub-server
# Interesting targets are:
#   $ rake clean   : removes non-source artifacts
#   $ rake test    : runs unit tests
#   $ rake package : assembles the whole webapp in a form suitable for
#                    deployment or running with dev_appserver.py
#   $ rake run     : runs the existing webapp with dev_appserver.py

desc "remove generated artifacts"
task :clean do
  sh "rm -fr target"
  sh "find . -name \"*~\" | xargs rm -f"
  sh "find . -name \"*.pyc\" | xargs rm -f"
end

directory "target"
directory "target/webapp"
directory "target/webapp/templates"

# create a file with the current AppEngine deployment version in it
file "target/build.txt" => ["target","src/main/build.txt"] do
  sh "cp src/main/build.txt target/build.txt"
end

# create a sed script to substitute %BUILD% for the current Git hash
file "target/build.sed" => ["target/build.txt"] do
  sh "awk '{print \"s/%BUILD%/\" $1 \"/\"}' target/build.txt > target/build.sed"
end

desc "initialize build state"
task :initialize => ["target","target/webapp","target/build.sed"]

# generate build.py (apply %BUILD%)
file "target/webapp/build.py" => ["target/build.sed", "src/main/build.py"] do
  sh "sed -f target/build.sed src/main/build.py > target/webapp/build.py"
end

file "src/main/app.yaml" => ["target/build.sed", "src/main/app.yaml.template"] do
  sh "sed -f target/build.sed src/main/app.yaml.template > src/main/app.yaml"
end

file "src/main/build.py" => ["target/build.sed", "src/main/build.py.template"] do
  sh "sed -f target/build.sed src/main/build.py.template > src/main/build.py"
end

# generate app.yaml (apply %BUILD%)
file "target/webapp/app.yaml" => ["target/build.sed", "src/main/app.yaml"] do
  sh "sed -f target/build.sed src/main/app.yaml > target/webapp/app.yaml"
end

file "target/webapp/build.py" => ["target/build.sed", "src/main/build.py"] do
  sh "sed -f target/build.sed src/main/build.py.template > target/webapp/build.py"
end

task :static_dir => ["target/webapp","target/build.txt"] do
  sh "mkdir -p target/webapp/static"
end

desc "generate resources for inclusion in the package"
task :process_resources => [ :initialize, "target/webapp/app.yaml",
                             "target/webapp/build.py", :static_dir ] do
  sh "cp -r src/main/static/* target/webapp/static"
end

desc "run unit tests"
task :test => [] do
  sh "bin/run_test src/test"
end

desc "assemble app for deployment"
task :package => [:test, "target/webapp/templates"] do
  sh "cp -R src/main/* target/webapp"
end

desc "check for in/out of sync with git master"
task :git_sync => [:initialize] do
  sh "bin/git_check_local.sh"
  sh "bin/git_check_remote.sh"
end

desc "increment working version number"
task :incr => [:git_sync] do
  sh "bin/increment_version src/main/build.txt"
end

desc "commit updated version number"
task :commit_version => [] do
  sh "git commit -a -m \"Update version number to `cat src/main/build.txt`\""
  sh "git push origin master"
end

desc "upload to app engine"
task :push => [] do
  sh "appcfg.py update target/webapp"
end

desc "deploy current version to app engine"
task :deploy => [:clean, :git_sync, :incr, :package, :commit_version, :push]

desc "run the app in a dev server"
task :run => ["src/main/app.yaml", "src/main/build.py"] do
  sh "dev_appserver.py src/main"
end

# for convenience when programming
desc "Default task = package"
task :default => [:package]
