
(cl:in-package :asdf)

(defsystem "gopher_move_it_config-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils :geometry_msgs-msg
               :gopher_move_it_config-msg
               :moveit_msgs-msg
)
  :components ((:file "_package")
    (:file "PlanTrajectory" :depends-on ("_package_PlanTrajectory"))
    (:file "_package_PlanTrajectory" :depends-on ("_package"))
  ))