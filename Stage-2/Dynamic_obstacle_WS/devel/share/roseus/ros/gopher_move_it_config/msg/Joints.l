;; Auto-generated. Do not edit!


(when (boundp 'gopher_move_it_config::Joints)
  (if (not (find-package "GOPHER_MOVE_IT_CONFIG"))
    (make-package "GOPHER_MOVE_IT_CONFIG"))
  (shadow 'Joints (find-package "GOPHER_MOVE_IT_CONFIG")))
(unless (find-package "GOPHER_MOVE_IT_CONFIG::JOINTS")
  (make-package "GOPHER_MOVE_IT_CONFIG::JOINTS"))

(in-package "ROS")
;;//! \htmlinclude Joints.msg.html


(defclass gopher_move_it_config::Joints
  :super ros::object
  :slots (_joints ))

(defmethod gopher_move_it_config::Joints
  (:init
   (&key
    ((:joints __joints) (make-array 0 :initial-element 0.0 :element-type :float))
    )
   (send-super :init)
   (setq _joints __joints)
   self)
  (:joints
   (&optional __joints)
   (if __joints (setq _joints __joints)) _joints)
  (:serialization-length
   ()
   (+
    ;; float64[] _joints
    (* 8    (length _joints)) 4
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64[] _joints
     (write-long (length _joints) s)
     (dotimes (i (length _joints))
       (sys::poke (elt _joints i) (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
       )
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64[] _joints
   (let (n)
     (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4)
     (setq _joints (instantiate float-vector n))
     (dotimes (i n)
     (setf (elt _joints i) (sys::peek buf ptr- :double)) (incf ptr- 8)
     ))
   ;;
   self)
  )

(setf (get gopher_move_it_config::Joints :md5sum-) "82c16c802eb7e05fa5331a00ebfb3b28")
(setf (get gopher_move_it_config::Joints :datatype-) "gopher_move_it_config/Joints")
(setf (get gopher_move_it_config::Joints :definition-)
      "float64[] joints

")



(provide :gopher_move_it_config/Joints "82c16c802eb7e05fa5331a00ebfb3b28")


