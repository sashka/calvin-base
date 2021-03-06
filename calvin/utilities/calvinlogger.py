# -*- coding: utf-8 -*-

# Copyright (c) 2015 Ericsson AB
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import logging
from colorlog import ColoredFormatter

_name = "calvin"
_log = None
_use_color = False

def _create_logger():
    global _log
    global _name
    if _log is None:
        _log = logging.getLogger(_name)
        _log.setLevel(logging.INFO)

        # create console handler and set level to debug
        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        # create formatter
        colored = ColoredFormatter(
            "%(asctime)-15s %(log_color)s%(levelname)-8s %(name)s%(reset)s: %(message)s",
            datefmt=None,
            reset=True,
            log_colors={
                'DEBUG': 'cyan',
                'INFO': 'green',
                'WARNING': 'yellow',
                'ERROR': 'red',
                'CRITICAL': 'red',
            }
        )

        plain = ColoredFormatter(
            "%(asctime)-15s %(levelname)-8s %(name)s: %(message)s",
            datefmt=None,
            reset=False,
            log_colors={}
        )


        # formatter = logging.Formatter('%(asctime)-15s - %(levelname)-7s - %(name)s: %(message)s')s

        # add formatter to ch
        ch.setFormatter(colored if _use_color else plain)

        # add ch to logger
        _log.addHandler(ch)

    return _log


def get_logger(name=None):
    log = _create_logger()
    if name is None:
        return log
    return log.getChild("%s" % (name))


def get_actor_logger(name):
    log = _create_logger()
    return log.getChild("%s.%s" % ("actors", name))
