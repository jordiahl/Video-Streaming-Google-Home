#! /usr/bin/python3.6
import logging
import sys
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0, '/home/pi/Desktop/Home-Automation/Controlling-switchbot/Video-Streaming-Google-Home/streamingProjectorGoogleHome/')
from main import app as application
application.secret_key = 'anything you wish'