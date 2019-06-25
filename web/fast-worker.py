
import os
import inspect
import sys

import werkzeug.serving
import thread

import controllers
import controllers.configuration

# Get the default configuration file location
absolute_location = os.path.abspath(inspect.getfile(inspect.currentframe()))
absolute_path = os.path.dirname(absolute_location)
absolute_root_path = os.path.abspath(os.path.join(absolute_path, ".."))

# Load configuration from default location
local_config_file = os.path.join(absolute_root_path, "node.conf.local")
if os.path.isfile(local_config_file):
    config_file = local_config_file
else:
    config_file = os.path.join(absolute_root_path, "node.conf")
controllers.configuration.parse_config_file(config_file)

# Add the code path to the system path
code_dir = controllers.configuration.NodeConfiguration.Paths.code_root
sys.path.insert(0, code_dir)

import controllers.worker

if __name__ == '__main__':
    controllers.worker.foreground_thread()
