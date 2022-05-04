; Auto-generated. Do not edit!


(cl:in-package gopher_move_it_config-srv)


;//! \htmlinclude PlanTrajectory-request.msg.html

(cl:defclass <PlanTrajectory-request> (roslisp-msg-protocol:ros-message)
  ((joints
    :reader joints
    :initarg :joints
    :type gopher_move_it_config-msg:Joints
    :initform (cl:make-instance 'gopher_move_it_config-msg:Joints))
   (target
    :reader target
    :initarg :target
    :type geometry_msgs-msg:Pose
    :initform (cl:make-instance 'geometry_msgs-msg:Pose)))
)

(cl:defclass PlanTrajectory-request (<PlanTrajectory-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlanTrajectory-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlanTrajectory-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gopher_move_it_config-srv:<PlanTrajectory-request> is deprecated: use gopher_move_it_config-srv:PlanTrajectory-request instead.")))

(cl:ensure-generic-function 'joints-val :lambda-list '(m))
(cl:defmethod joints-val ((m <PlanTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gopher_move_it_config-srv:joints-val is deprecated.  Use gopher_move_it_config-srv:joints instead.")
  (joints m))

(cl:ensure-generic-function 'target-val :lambda-list '(m))
(cl:defmethod target-val ((m <PlanTrajectory-request>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gopher_move_it_config-srv:target-val is deprecated.  Use gopher_move_it_config-srv:target instead.")
  (target m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlanTrajectory-request>) ostream)
  "Serializes a message object of type '<PlanTrajectory-request>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'joints) ostream)
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'target) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlanTrajectory-request>) istream)
  "Deserializes a message object of type '<PlanTrajectory-request>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'joints) istream)
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'target) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlanTrajectory-request>)))
  "Returns string type for a service object of type '<PlanTrajectory-request>"
  "gopher_move_it_config/PlanTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanTrajectory-request)))
  "Returns string type for a service object of type 'PlanTrajectory-request"
  "gopher_move_it_config/PlanTrajectoryRequest")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlanTrajectory-request>)))
  "Returns md5sum for a message object of type '<PlanTrajectory-request>"
  "66d002794b60389592f498a78cfe1427")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlanTrajectory-request)))
  "Returns md5sum for a message object of type 'PlanTrajectory-request"
  "66d002794b60389592f498a78cfe1427")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlanTrajectory-request>)))
  "Returns full string definition for message of type '<PlanTrajectory-request>"
  (cl:format cl:nil "Joints joints~%geometry_msgs/Pose target~%~%================================================================================~%MSG: gopher_move_it_config/Joints~%float64[] joints~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlanTrajectory-request)))
  "Returns full string definition for message of type 'PlanTrajectory-request"
  (cl:format cl:nil "Joints joints~%geometry_msgs/Pose target~%~%================================================================================~%MSG: gopher_move_it_config/Joints~%float64[] joints~%~%================================================================================~%MSG: geometry_msgs/Pose~%# A representation of pose in free space, composed of position and orientation. ~%Point position~%Quaternion orientation~%~%================================================================================~%MSG: geometry_msgs/Point~%# This contains the position of a point in free space~%float64 x~%float64 y~%float64 z~%~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlanTrajectory-request>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'joints))
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'target))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlanTrajectory-request>))
  "Converts a ROS message object to a list"
  (cl:list 'PlanTrajectory-request
    (cl:cons ':joints (joints msg))
    (cl:cons ':target (target msg))
))
;//! \htmlinclude PlanTrajectory-response.msg.html

(cl:defclass <PlanTrajectory-response> (roslisp-msg-protocol:ros-message)
  ((trajectory
    :reader trajectory
    :initarg :trajectory
    :type moveit_msgs-msg:RobotTrajectory
    :initform (cl:make-instance 'moveit_msgs-msg:RobotTrajectory)))
)

(cl:defclass PlanTrajectory-response (<PlanTrajectory-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <PlanTrajectory-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'PlanTrajectory-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name gopher_move_it_config-srv:<PlanTrajectory-response> is deprecated: use gopher_move_it_config-srv:PlanTrajectory-response instead.")))

(cl:ensure-generic-function 'trajectory-val :lambda-list '(m))
(cl:defmethod trajectory-val ((m <PlanTrajectory-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader gopher_move_it_config-srv:trajectory-val is deprecated.  Use gopher_move_it_config-srv:trajectory instead.")
  (trajectory m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <PlanTrajectory-response>) ostream)
  "Serializes a message object of type '<PlanTrajectory-response>"
  (roslisp-msg-protocol:serialize (cl:slot-value msg 'trajectory) ostream)
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <PlanTrajectory-response>) istream)
  "Deserializes a message object of type '<PlanTrajectory-response>"
  (roslisp-msg-protocol:deserialize (cl:slot-value msg 'trajectory) istream)
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<PlanTrajectory-response>)))
  "Returns string type for a service object of type '<PlanTrajectory-response>"
  "gopher_move_it_config/PlanTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanTrajectory-response)))
  "Returns string type for a service object of type 'PlanTrajectory-response"
  "gopher_move_it_config/PlanTrajectoryResponse")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<PlanTrajectory-response>)))
  "Returns md5sum for a message object of type '<PlanTrajectory-response>"
  "66d002794b60389592f498a78cfe1427")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'PlanTrajectory-response)))
  "Returns md5sum for a message object of type 'PlanTrajectory-response"
  "66d002794b60389592f498a78cfe1427")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<PlanTrajectory-response>)))
  "Returns full string definition for message of type '<PlanTrajectory-response>"
  (cl:format cl:nil "moveit_msgs/RobotTrajectory trajectory~%~%~%================================================================================~%MSG: moveit_msgs/RobotTrajectory~%trajectory_msgs/JointTrajectory joint_trajectory~%trajectory_msgs/MultiDOFJointTrajectory multi_dof_joint_trajectory~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectory~%Header header~%string[] joint_names~%JointTrajectoryPoint[] points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectoryPoint~%# Each trajectory point specifies either positions[, velocities[, accelerations]]~%# or positions[, effort] for the trajectory to be executed.~%# All specified values are in the same order as the joint names in JointTrajectory.msg~%~%float64[] positions~%float64[] velocities~%float64[] accelerations~%float64[] effort~%duration time_from_start~%~%================================================================================~%MSG: trajectory_msgs/MultiDOFJointTrajectory~%# The header is used to specify the coordinate frame and the reference time for the trajectory durations~%Header header~%~%# A representation of a multi-dof joint trajectory (each point is a transformation)~%# Each point along the trajectory will include an array of positions/velocities/accelerations~%# that has the same length as the array of joint names, and has the same order of joints as ~%# the joint names array.~%~%string[] joint_names~%MultiDOFJointTrajectoryPoint[] points~%~%================================================================================~%MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint~%# Each multi-dof joint can specify a transform (up to 6 DOF)~%geometry_msgs/Transform[] transforms~%~%# There can be a velocity specified for the origin of the joint ~%geometry_msgs/Twist[] velocities~%~%# There can be an acceleration specified for the origin of the joint ~%geometry_msgs/Twist[] accelerations~%~%duration time_from_start~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'PlanTrajectory-response)))
  "Returns full string definition for message of type 'PlanTrajectory-response"
  (cl:format cl:nil "moveit_msgs/RobotTrajectory trajectory~%~%~%================================================================================~%MSG: moveit_msgs/RobotTrajectory~%trajectory_msgs/JointTrajectory joint_trajectory~%trajectory_msgs/MultiDOFJointTrajectory multi_dof_joint_trajectory~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectory~%Header header~%string[] joint_names~%JointTrajectoryPoint[] points~%~%================================================================================~%MSG: std_msgs/Header~%# Standard metadata for higher-level stamped data types.~%# This is generally used to communicate timestamped data ~%# in a particular coordinate frame.~%# ~%# sequence ID: consecutively increasing ID ~%uint32 seq~%#Two-integer timestamp that is expressed as:~%# * stamp.sec: seconds (stamp_secs) since epoch (in Python the variable is called 'secs')~%# * stamp.nsec: nanoseconds since stamp_secs (in Python the variable is called 'nsecs')~%# time-handling sugar is provided by the client library~%time stamp~%#Frame this data is associated with~%string frame_id~%~%================================================================================~%MSG: trajectory_msgs/JointTrajectoryPoint~%# Each trajectory point specifies either positions[, velocities[, accelerations]]~%# or positions[, effort] for the trajectory to be executed.~%# All specified values are in the same order as the joint names in JointTrajectory.msg~%~%float64[] positions~%float64[] velocities~%float64[] accelerations~%float64[] effort~%duration time_from_start~%~%================================================================================~%MSG: trajectory_msgs/MultiDOFJointTrajectory~%# The header is used to specify the coordinate frame and the reference time for the trajectory durations~%Header header~%~%# A representation of a multi-dof joint trajectory (each point is a transformation)~%# Each point along the trajectory will include an array of positions/velocities/accelerations~%# that has the same length as the array of joint names, and has the same order of joints as ~%# the joint names array.~%~%string[] joint_names~%MultiDOFJointTrajectoryPoint[] points~%~%================================================================================~%MSG: trajectory_msgs/MultiDOFJointTrajectoryPoint~%# Each multi-dof joint can specify a transform (up to 6 DOF)~%geometry_msgs/Transform[] transforms~%~%# There can be a velocity specified for the origin of the joint ~%geometry_msgs/Twist[] velocities~%~%# There can be an acceleration specified for the origin of the joint ~%geometry_msgs/Twist[] accelerations~%~%duration time_from_start~%~%================================================================================~%MSG: geometry_msgs/Transform~%# This represents the transform between two coordinate frames in free space.~%~%Vector3 translation~%Quaternion rotation~%~%================================================================================~%MSG: geometry_msgs/Vector3~%# This represents a vector in free space. ~%# It is only meant to represent a direction. Therefore, it does not~%# make sense to apply a translation to it (e.g., when applying a ~%# generic rigid transformation to a Vector3, tf2 will only apply the~%# rotation). If you want your data to be translatable too, use the~%# geometry_msgs/Point message instead.~%~%float64 x~%float64 y~%float64 z~%================================================================================~%MSG: geometry_msgs/Quaternion~%# This represents an orientation in free space in quaternion form.~%~%float64 x~%float64 y~%float64 z~%float64 w~%~%================================================================================~%MSG: geometry_msgs/Twist~%# This expresses velocity in free space broken into its linear and angular parts.~%Vector3  linear~%Vector3  angular~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <PlanTrajectory-response>))
  (cl:+ 0
     (roslisp-msg-protocol:serialization-length (cl:slot-value msg 'trajectory))
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <PlanTrajectory-response>))
  "Converts a ROS message object to a list"
  (cl:list 'PlanTrajectory-response
    (cl:cons ':trajectory (trajectory msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'PlanTrajectory)))
  'PlanTrajectory-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'PlanTrajectory)))
  'PlanTrajectory-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'PlanTrajectory)))
  "Returns string type for a service object of type '<PlanTrajectory>"
  "gopher_move_it_config/PlanTrajectory")