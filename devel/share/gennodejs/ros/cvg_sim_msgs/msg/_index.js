
"use strict";

let Compass = require('./Compass.js');
let MotorStatus = require('./MotorStatus.js');
let Altimeter = require('./Altimeter.js');
let VelocityZCommand = require('./VelocityZCommand.js');
let MotorPWM = require('./MotorPWM.js');
let ControllerState = require('./ControllerState.js');
let ServoCommand = require('./ServoCommand.js');
let HeadingCommand = require('./HeadingCommand.js');
let Altitude = require('./Altitude.js');
let PositionXYCommand = require('./PositionXYCommand.js');
let HeightCommand = require('./HeightCommand.js');
let VelocityXYCommand = require('./VelocityXYCommand.js');
let ThrustCommand = require('./ThrustCommand.js');
let RawMagnetic = require('./RawMagnetic.js');
let YawrateCommand = require('./YawrateCommand.js');
let RawImu = require('./RawImu.js');
let RawRC = require('./RawRC.js');
let AttitudeCommand = require('./AttitudeCommand.js');
let MotorCommand = require('./MotorCommand.js');
let RC = require('./RC.js');
let RuddersCommand = require('./RuddersCommand.js');
let Supply = require('./Supply.js');

module.exports = {
  Compass: Compass,
  MotorStatus: MotorStatus,
  Altimeter: Altimeter,
  VelocityZCommand: VelocityZCommand,
  MotorPWM: MotorPWM,
  ControllerState: ControllerState,
  ServoCommand: ServoCommand,
  HeadingCommand: HeadingCommand,
  Altitude: Altitude,
  PositionXYCommand: PositionXYCommand,
  HeightCommand: HeightCommand,
  VelocityXYCommand: VelocityXYCommand,
  ThrustCommand: ThrustCommand,
  RawMagnetic: RawMagnetic,
  YawrateCommand: YawrateCommand,
  RawImu: RawImu,
  RawRC: RawRC,
  AttitudeCommand: AttitudeCommand,
  MotorCommand: MotorCommand,
  RC: RC,
  RuddersCommand: RuddersCommand,
  Supply: Supply,
};
