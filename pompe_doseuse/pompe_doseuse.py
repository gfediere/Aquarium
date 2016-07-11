#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import sys
import datetime
import ConfigParser

Config = ConfigParser.ConfigParser()
Config.read("./pompe_doseuse.conf")
produit = sys.argv[1].lower()
duration = sys.argv[2] # Need to be string

GPIO.setmode(GPIO.BCM)

def ConfigSectionMap(section):
  dict1 = {}
  options = Config.options(section)
  for option in options:
    try:
      dict1[option] = Config.get(section, option)
      if dict1[option] == -1:
        DebugPrint("skip: %s" % option)
    except:
          print("exception on %s!" % option)
          dict1[option] = None
  return dict1

def WriteLog ( log ):
  print datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), "|", produit, "|" ,log
  return

def inject( id, produit, duration ):
  WriteLog( "Injecting during: " + duration )
  GPIO.setup(id, GPIO.OUT)
  GPIO.output(id, GPIO.HIGH)

  try:
    GPIO.output(id, GPIO.LOW)
    time.sleep(float(duration));
    GPIO.output(id, GPIO.HIGH)
  # Clean
    WriteLog ( "End" )
    GPIO.cleanup()
  except KeyboardInterrupt:
    print "  Quit"
  return

if produit == 'ca':
  gpio_id = ConfigSectionMap('gpio_id')['ca']
if produit == 'mg':
  gpio_id = ConfigSectionMap('gpio_id')['mg']
if produit == 'sel':
  gpio_id = ConfigSectionMap('gpio_id')['sel']

inject( gpio_id, produit, duration )
