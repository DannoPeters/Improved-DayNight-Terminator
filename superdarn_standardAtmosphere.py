# Copyright (C) SuperDARN Canada, University of Saskatchewan
# Authors: Marina Schmidt and Danno Peters

"""
This module contains SuperDARN radar information
"""
from typing import NamedTuple


"""
_Radar Class - Used to store relevent information about the SuperDARN Radars
      Nested inside of _Radar Named Tuple, composed of three floats representing location and boresight direction
      
      name: full text of radar name
      stid: station number
      acronym: three letter station acronym
      beams: number of possible beams
      gates: number of range gates per beam
      geographic: Named Tuple containing geographic latitude longitude and boresight
      geomagnetic: Named Tuple containing geomagnetic latitude longitude and boresight
      hemisphere: _Hemisphere
      institute: full text name of institution operating the radar site
"""

def temperature(altitude):
  try:
    temp = AtmospericConstants.standard[altitude].temperature
  except:
    alt = -2000
    lower = None
    upper = None
    for alt in AtmospericConstants.standard
      if alt.altitude < altitude:
        lower = alt.altitude
    
  return temp


class _Atmosphere(NamedTuple):
    layer: str
    temperature: float #Kelvin
    pressure: float #Pascals
    density: float #kilograms per cubicmeter
    altitude: int #meters

"""
SuperDARNRadars Class - contains a dictionary of Nested Named Tuples with information about each radar
    Dictioanry index is the radar station ID number
    
    Accessed using SuperDARNRadars.radar[**StationID**].**Tuple Name**
        Where:  
                **StationID** is an integer station ID, ie 5
                **Tuple Name** is the name of a tuple, ie institute 

        Example:
                SuperDARNRadars.radar[5].institute retuns the string "University of Saskatchewan"
"""
class AtmospericConstants():
    # Information obtained from http://vt.superdarn.org/tiki-index.php?page=Radar+Overview
    standard = {-2000:  _Atmosphere( 'Troposphere',   301.15,         127774.0,         1.47808,              -2000), 
                -1000:  _Atmosphere( 'Troposphere',   294.65,         113929.0,         1.3470,               -1000), 
                0:      _Atmosphere( 'Troposphere',   288.15,         101325.0,         1.2250,               0), 
                1000:   _Atmosphere( 'Troposphere',   281.65,         89874.6,          1.11164,              1000), 
                2000:   _Atmosphere( 'Troposphere',   275.15,         79495.2,          1.00649,              2000), 
                3000:   _Atmosphere( 'Troposphere',   268.65,         70108.5,          0.909122,             3000), 
                4000:   _Atmosphere( 'Troposphere',   262.15,         61640.2,          0.819129,             4000), 
                5000:   _Atmosphere( 'Troposphere',   255.65,         54019.9,          0.736116,             5000), 
                6000:   _Atmosphere( 'Troposphere',   249.15,         47181.0,          0.659697,             6000), 
                7000:   _Atmosphere( 'Troposphere',   242.65,         41060.7,          0.589501,             7000), 
                8000:   _Atmosphere( 'Troposphere',   236.15,         35599.8,          0.525168,             8000), 
                9000:   _Atmosphere( 'Troposphere',   229.65,         30742.5,          0.466348,             9000), 
                10000:  _Atmosphere( 'Troposphere',   223.15,         26436.3,          0.412707,             10000), 
                12000:  _Atmosphere( 'Stratosphere',  216.65,         19330.4,          0.310828,             12000), 
                15000:  _Atmosphere( 'Stratosphere',  216.65,         12044.6,          0.193674,             15000), 
                20000:  _Atmosphere( 'Stratosphere',  216.65,         5474.89,          0.08803490,           20000), 
                25000:  _Atmosphere( 'Stratosphere',  221.65,         2511.02,          0.03946580,           25000), 
                30000:  _Atmosphere( 'Stratosphere',  226.65,         1171.87,          0.01801190,           30000), 
                35000:  _Atmosphere( 'Stratosphere',  237.05,         558.9240,         0.00821392,           35000), 
                40000:  _Atmosphere( 'Stratosphere',  251.05,         277.5220,         0.00385101,           40000), 
                45000:  _Atmosphere( 'Stratosphere',  265.05,         143.1350,         0.00188129,           45000), 
                50000:  _Atmosphere( 'Stratosphere',  270.65,         75.9448,          0.000977525,          50000), 
                60000:  _Atmosphere( 'Mesosphere',    245.45,         20.3143,          0.000288321,          60000), 
                70000:  _Atmosphere( 'Mesosphere',    217.45,         4.63422,          0.0000742,            70000), 
                80000:  _Atmosphere( 'Mesosphere',    196.65,         0.88628,          0.00001570,           80000), 
                84852:  _Atmosphere( 'Mesosphere',    186.95,         0.373384,         0.00000696,           84852), 
                100000: _Atmosphere( 'Thermosphere',  184.016,        0.0281,           0.000000508,          100000), 
                120000: _Atmosphere( 'Thermosphere',  374.97150,      0.00217,          0.000000018,          120000), 
                140000: _Atmosphere( 'Thermosphere',  635.57030,      0.000703,         0.000000003260,       140000), 
                160000: _Atmosphere( 'Thermosphere',  787.55320,      0.000331,         0.000000001180,       160000), 
                180000: _Atmosphere( 'Thermosphere',  877.67290,      0.00018,          0.000000000551,       180000), 
                200000: _Atmosphere( 'Thermosphere',  931.28060,      0.000105,         0.000000000291,       200000), 
                220000: _Atmosphere( 'Thermosphere',  963.27010,      0.00006440,       0.000000000166,       220000), 
                240000: _Atmosphere( 'Thermosphere',  982.41910,      0.00004090,       0.0000000000991,      240000), 
                260000: _Atmosphere( 'Thermosphere',  993.91730,      0.00002660,       0.0000000000616,      260000), 
                280000: _Atmosphere( 'Thermosphere',  1000.84270,     0.00001770,       0.0000000000394,      280000), 
                300000: _Atmosphere( 'Thermosphere',  1005.02670,     0.000012,         0.0000000000258,      300000), 
                320000: _Atmosphere( 'Thermosphere',  1007.562,       0.00000820,       0.0000000000172,      320000), 
                340000: _Atmosphere( 'Thermosphere',  1009.103,       0.00000569,       0.0000000000116,      340000), 
                360000: _Atmosphere( 'Thermosphere',  1010.04230,     0.00000398,       0.00000000000799,     360000), 
                380000: _Atmosphere( 'Thermosphere',  1010.61660,     0.00000281,       0.00000000000555,     380000), 
                400000: _Atmosphere( 'Thermosphere',  1010.96880,     0.00000201,       0.00000000000389,     400000), 
                420000: _Atmosphere( 'Thermosphere',  1011.18530,     0.00000144,       0.00000000000275,     420000), 
                440000: _Atmosphere( 'Thermosphere',  1011.319,       0.00000104,       0.00000000000196,     440000), 
                460000: _Atmosphere( 'Thermosphere',  1011.40140,     0.000000755,      0.0000000000014,      460000), 
                480000: _Atmosphere( 'Thermosphere',  1011.45260,     0.000000553,      0.00000000000101,     480000), 
                500000: _Atmosphere( 'Thermosphere',  1011.48450,     0.000000407,      0.00000000000073,     500000), 
                520000: _Atmosphere( 'Thermosphere',  1011.50430,     0.000000303,      0.0000000000005310,   520000), 
                540000: _Atmosphere( 'Thermosphere',  1011.51680,     0.000000227,      0.0000000000003880,   540000), 
                560000: _Atmosphere( 'Thermosphere',  1011.52450,     0.000000171,      0.0000000000002850,   560000), 
                580000: _Atmosphere( 'Thermosphere',  1011.52940,     0.000000131,      0.0000000000002110,   580000), 
                600000: _Atmosphere( 'Thermosphere',  1011.53250,     0.000000101,      0.0000000000001560,   600000), 
                620000: _Atmosphere( 'Exosphere',     1011.53450,     0.0000000789,     0.0000000000001170,   620000), 
                640000: _Atmosphere( 'Exosphere',     1011.53570,     0.0000000624,     0.0000000000000879,   640000), 
                660000: _Atmosphere( 'Exosphere',     1011.53650,     0.0000000501,     0.0000000000000665,   660000), 
                680000: _Atmosphere( 'Exosphere',     1011.537,       0.0000000407,     0.0000000000000508,   680000), 
                700000: _Atmosphere( 'Exosphere',     1011.53740,     0.0000000336,     0.0000000000000391,   700000), 
                720000: _Atmosphere( 'Exosphere',     1011.53750,     0.0000000282,     0.0000000000000304,   720000), 
                740000: _Atmosphere( 'Exosphere',     1011.53770,     0.0000000239,     0.0000000000000239,   740000), 
                760000: _Atmosphere( 'Exosphere',     1011.53770,     0.0000000206,     0.0000000000000190,   760000), 
                780000: _Atmosphere( 'Exosphere',     1011.53780,     0.0000000179,     0.0000000000000153,   780000), 
                800000: _Atmosphere( 'Exosphere',     1011.53780,     0.0000000158,     0.0000000000000125,   800000), 
                820000: _Atmosphere( 'Exosphere',     1011.53780,     0.000000014,      0.0000000000000103,   820000), 
                840000: _Atmosphere( 'Exosphere',     1011.53790,     0.0000000126,     0.00000000000000864,  840000), 
                860000: _Atmosphere( 'Exosphere',     1011.53790,     0.0000000114,     0.00000000000000732,  860000), 
                880000: _Atmosphere( 'Exosphere',     1011.53790,     0.0000000104,     0.00000000000000628,  880000), 
                900000: _Atmosphere( 'Exosphere',     1011.53790,     0.000000009470,   0.00000000000000546,  900000)

              }
