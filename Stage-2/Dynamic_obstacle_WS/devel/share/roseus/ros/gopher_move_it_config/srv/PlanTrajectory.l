;; Auto-generated. Do not edit!


(when (boundp 'gopher_move_it_config::PlanTrajectory)
  (if (not (find-package "GOPHER_MOVE_IT_CONFIG"))
    (make-package "GOPHER_MOVE_IT_CONFIG"))
  (shadow 'PlanTrajectory (find-package "GOPHER_MOVE_IT_CONFIG")))
(unless (find-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORY")
  (make-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORY"))
(unless (find-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORYREQUEST")
  (make-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORYREQUEST"))
(unless (find-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORYRESPONSE")
  (make-package "GOPHER_MOVE_IT_CONFIG::PLANTRAJECTORYRESPONSE"))

(in-package "ROS")

(if (not (find-package "GEOMETRY_MSGS"))
  (ros::roseus-add-msgs "geometry_msgs"))


(if (not (find-package "MOVEIT_MSGS"))
  (ros::roseus-add-msgs "moveit_msgs"))


(defclass gopher_move_it_config::PlanTrajectoryRequest
  :super ros::object
  :slots (_joints _target ))

(defmethod gopher_move_it_config::PlanTrajectoryRequest
  (:init
   (&key
    ((:joints __joints) (instance gopher_move_it_config::Joints :init))
    ((:target __target) (instance geometry_msgs::Pose :init))
    )
   (send-super :init)
   (setq _joints __joints)
   (setq _target __target)
   self)
  (:joints
   (&rest __joints)
   (if (keywordp (car __joints))
       (send* _joints __joints)
     (progn
       (if __joints (setq _joints (car __joints)))
       _joints)))
  (:target
   (&rest __target)
   (if (keywordp (car __target))
       (send* _target __target)
     (progn
       (if __target (setq _target (car __target)))
       _target)))
  (:serialization-length
   ()
   (+
    ;; gopher_move_it_config/Joints _joints
    (send _joints :serialization-length)
    ;; geometry_msgs/Pose _target
    (send _target :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; gopher_move_it_config/Joints _joints
       (send _joints :serialize s)
     ;; geometry_msgs/Pose _target
       (send _target :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; gopher_move_it_config/Joints _joints
     (send _joints :deserialize buf ptr-) (incf ptr- (send _joints :serialization-length))
   ;; geometry_msgs/Pose _target
     (send _target :deserialize buf ptr-) (incf ptr- (send _target :serialization-length))
   ;;
   self)
  )

(defclass gopher_move_it_config::PlanTrajectoryResponse
  :super ros::object
  :slots (_trajectory ))

(defmethod gopher_move_it_config::PlanTrajectoryResponse
  (:init
   (&key
    ((:trajectory __trajectory) (instance moveit_msgs::RobotTrajectory :init))
    )
   (send-super :init)
   (setq _trajectory __trajectory)
   self)
  (:trajectory
   (&rest __trajectory)
   (if (keywordp (car __trajectory))
       (send* _trajectory __trajectory)
     (progn
       (if __trajectory (setq _trajectory (car __trajectory)))
       _trajectory)))
  (:serialization-length
   ()
   (+
    ;; moveit_msgs/RobotTrajectory _trajectory
    (send _trajectory :serialization-length)
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; moveit_msgs/RobotTrajectory _trajectory
       (send _trajectory :serialize s)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; moveit_msgs/RobotTrajectory _trajectory
     (send _trajectory :deserialize buf ptr-) (incf ptr- (send _trajectory :serialization-length))
   ;;
   self)
  )

(defclass gopher_move_it_config::PlanTrajectory
  :super ros::object
  :slots ())

(setf (get gopher_move_it_config::PlanTrajectory :md5sum-) "66d002794b60389592f498a78cfe1427")
(setf (get gopher_move_it_config::PlanTrajectory :datatype-) "gopher_move_it_config/PlanTrajectory")
(setf (get gopher_move_it_config::PlanTrajectory :request) gopher_move_it_config::PlanTrajectoryRequest)
(setf (get gopher_move_it_config::PlanTrajectory :response) gopher_move_it_config::PlanTrajectoryResponse)

(defmethod gopher_move_it_config::PlanTrajectoryRequest
  (:response () (instance gopher_move_it_config::PlanTrajectoryResponse :init)))

(setf (get gopher_move_it_config::PlanTrajectoryRequest :md5sum-) "66d002794b60389592f498a78cfe1427")
(setf (get gopher_move_it_config::PlanTrajectoryRequest :datatype-) "gopher_move_it_config/PlanTrajectoryRequest")
(setf (get gopher_move_it_config::PlanTrajectoryRequest :definition-)
      "Joints joints
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
---
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
")

(setf (get gopher_move_it_config::PlanTrajectoryResponse :md5sum-) "66d002794b60389592f498a78cfe1427")
(setf (get gopher_move_it_config::PlanTrajectoryResponse :datatype-) "gopher_move_it_config/PlanTrajectoryResponse")
(setf (get gopher_move_it_config::PlanTrajectoryResponse :definition-)
      "Joints joints
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
---
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
")



(provide :gopher_move_it_config/PlanTrajectory "66d002794b60389592f498a78cfe1427")


