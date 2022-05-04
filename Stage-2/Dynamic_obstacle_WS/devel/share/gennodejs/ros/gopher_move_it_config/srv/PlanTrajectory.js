// Auto-generated. Do not edit!

// (in-package gopher_move_it_config.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;
let Joints = require('../msg/Joints.js');
let geometry_msgs = _finder('geometry_msgs');

//-----------------------------------------------------------

let moveit_msgs = _finder('moveit_msgs');

//-----------------------------------------------------------

class PlanTrajectoryRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.joints = null;
      this.target = null;
    }
    else {
      if (initObj.hasOwnProperty('joints')) {
        this.joints = initObj.joints
      }
      else {
        this.joints = new Joints();
      }
      if (initObj.hasOwnProperty('target')) {
        this.target = initObj.target
      }
      else {
        this.target = new geometry_msgs.msg.Pose();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PlanTrajectoryRequest
    // Serialize message field [joints]
    bufferOffset = Joints.serialize(obj.joints, buffer, bufferOffset);
    // Serialize message field [target]
    bufferOffset = geometry_msgs.msg.Pose.serialize(obj.target, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PlanTrajectoryRequest
    let len;
    let data = new PlanTrajectoryRequest(null);
    // Deserialize message field [joints]
    data.joints = Joints.deserialize(buffer, bufferOffset);
    // Deserialize message field [target]
    data.target = geometry_msgs.msg.Pose.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += Joints.getMessageSize(object.joints);
    return length + 56;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gopher_move_it_config/PlanTrajectoryRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '3bf313e1fc1f20a5ae89d4cd4412d92e';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    Joints joints
    geometry_msgs/Pose target
    
    ================================================================================
    MSG: gopher_move_it_config/Joints
    float64[] joints
    
    ================================================================================
    MSG: geometry_msgs/Pose
    # A representation of pose in free space, composed of position and orientation. 
    Point position
    Quaternion orientation
    
    ================================================================================
    MSG: geometry_msgs/Point
    # This contains the position of a point in free space
    float64 x
    float64 y
    float64 z
    
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PlanTrajectoryRequest(null);
    if (msg.joints !== undefined) {
      resolved.joints = Joints.Resolve(msg.joints)
    }
    else {
      resolved.joints = new Joints()
    }

    if (msg.target !== undefined) {
      resolved.target = geometry_msgs.msg.Pose.Resolve(msg.target)
    }
    else {
      resolved.target = new geometry_msgs.msg.Pose()
    }

    return resolved;
    }
};

class PlanTrajectoryResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.trajectory = null;
    }
    else {
      if (initObj.hasOwnProperty('trajectory')) {
        this.trajectory = initObj.trajectory
      }
      else {
        this.trajectory = new moveit_msgs.msg.RobotTrajectory();
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type PlanTrajectoryResponse
    // Serialize message field [trajectory]
    bufferOffset = moveit_msgs.msg.RobotTrajectory.serialize(obj.trajectory, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type PlanTrajectoryResponse
    let len;
    let data = new PlanTrajectoryResponse(null);
    // Deserialize message field [trajectory]
    data.trajectory = moveit_msgs.msg.RobotTrajectory.deserialize(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += moveit_msgs.msg.RobotTrajectory.getMessageSize(object.trajectory);
    return length;
  }

  static datatype() {
    // Returns string type for a service object
    return 'gopher_move_it_config/PlanTrajectoryResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '054c09e62210d7faad2f9fffdad07b57';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    moveit_msgs/RobotTrajectory trajectory
    
    
    ================================================================================
    MSG: moveit_msgs/RobotTrajectory
    trajectory_msgs/JointTrajectory joint_trajectory
    trajectory_msgs/MultiDOFJointTrajectory multi_dof_joint_trajectory
    
    ================================================================================
    MSG: trajectory_msgs/JointTrajectory
    Header header
    string[] joint_names
    JointTrajectoryPoint[] points
    
    ================================================================================
    MSG: std_msgs/Header
    # Standard metadata for higher-level stamped data types.
    # This is generally used to communicate timestamped data 
    # in a particular coordinate frame.
    # 
    # sequence ID: consecutively increasing ID 
    uint32 seq
    #Two-integer timestamp that is expressed as:
    # * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')
    # * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')
    # time-handling sugar is provided by the client library
    time stamp
    #Frame this data is associated with
    string frame_id
    
    ================================================================================
    MSG: trajectory_msgs/JointTrajectoryPoint
    # Each trajectory point specifies either positions[, velocities[, accelerations]]
    # or positions[, effort] for the trajectory to be executed.
    # All specified values are in the same order as the joint names in JointTrajectory.msg
    
    float64[] positions
    float64[] velocities
    float64[] accelerations
    float64[] effort
    duration time_from_start
    
    ================================================================================
    MSG: trajectory_msgs/MultiDOFJointTrajectory
    # The header is used to specify the coordinate frame and the reference time for the trajectory durations
    Header header
    
    # A representation of a multi-dof joint trajectory (each point is a transformation)
    # Each point along the trajectory will include an array of positions/velocities/accelerations
    # that has the same length as the array of joint names, and has the same order of joints as 
    # the joint names array.
    
    string[] joint_names
    MultiDOFJointTrajectoryPoint[] points
    
    ================================================================================
    MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint
    # Each multi-dof joint can specify a transform (up to 6 DOF)
    geometry_msgs/Transform[] transforms
    
    # There can be a velocity specified for the origin of the joint 
    geometry_msgs/Twist[] velocities
    
    # There can be an acceleration specified for the origin of the joint 
    geometry_msgs/Twist[] accelerations
    
    duration time_from_start
    
    ================================================================================
    MSG: geometry_msgs/Transform
    # This represents the transform between two coordinate frames in free space.
    
    Vector3 translation
    Quaternion rotation
    
    ================================================================================
    MSG: geometry_msgs/Vector3
    # This represents a vector in free space. 
    # It is only meant to represent a direction. Therefore, it does not
    # make sense to apply a translation to it (e.g., when applying a 
    # generic rigid transformation to a Vector3, tf2 will only apply the
    # rotation). If you want your data to be translatable too, use the
    # geometry_msgs/Point message instead.
    
    float64 x
    float64 y
    float64 z
    ================================================================================
    MSG: geometry_msgs/Quaternion
    # This represents an orientation in free space in quaternion form.
    
    float64 x
    float64 y
    float64 z
    float64 w
    
    ================================================================================
    MSG: geometry_msgs/Twist
    # This expresses velocity in free space broken into its linear and angular parts.
    Vector3  linear
    Vector3  angular
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new PlanTrajectoryResponse(null);
    if (msg.trajectory !== undefined) {
      resolved.trajectory = moveit_msgs.msg.RobotTrajectory.Resolve(msg.trajectory)
    }
    else {
      resolved.trajectory = new moveit_msgs.msg.RobotTrajectory()
    }

    return resolved;
    }
};

module.exports = {
  Request: PlanTrajectoryRequest,
  Response: PlanTrajectoryResponse,
  md5sum() { return '66d002794b60389592f498a78cfe1427'; },
  datatype() { return 'gopher_move_it_config/PlanTrajectory'; }
};
