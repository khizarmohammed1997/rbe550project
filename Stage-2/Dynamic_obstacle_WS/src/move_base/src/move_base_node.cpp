/*
 * Copyright (c) 2013, Willow Garage, Inc.
 * All rights reserved.
 *
 * Redistribution and use in source and binary forms, with or without
 * modification, are permitted provided that the following conditions are met:
 *
 *     * Redistributions of source code must retain the above copyright
 *       notice, this list of conditions and the following disclaimer.
 *     * Redistributions in binary form must reproduce the above copyright
 *       notice, this list of conditions and the following disclaimer in the
 *       documentation and/or other materials provided with the distribution.
 *     * Neither the name of the Willow Garage, Inc. nor the names of its
 *       contributors may be used to endorse or promote products derived from
 *       this software without specific prior written permission.
 *
 * THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
 * AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
 * IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
 * ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
 * LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
 * CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
 * SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
 * INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
 * CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
 * ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 * POSSIBILITY OF SUCH DAMAGE.
 */

#include <move_base/move_base.h>
#include <tf2_ros/transform_listener.h>
#include <base_local_planner/simple_scored_sampling_planner.h>
#include <tf/tf.h>
double frieght_x;
double frieght_y;
double frieght_theta;
base_local_planner::SimpleScoredSamplingPlanner planner = base_local_planner::SimpleScoredSamplingPlanner();

void freight_pose_Callback(geometry_msgs::PoseStamped data){
   frieght_x = data.pose.position.x;
   frieght_y = data.pose.position.y;
  //  frieght_theta = data.pose.orientation.z;
   tf::Quaternion q(
        data.pose.orientation.x,
        data.pose.orientation.y,
        data.pose.orientation.z,
        data.pose.orientation.w);
    tf::Matrix3x3 m(q);
    double roll, pitch, yaw;
    m.getRPY(roll, pitch, yaw);
    frieght_theta = yaw;
  planner.obstacle_data(frieght_x,frieght_y,frieght_theta);
  // ROS_INFO("frieght position %f",frieght_theta);
  }



int main(int argc, char** argv){
  ros::init(argc, argv, "move_base_node");
  tf2_ros::Buffer buffer(ros::Duration(10));
  tf2_ros::TransformListener tf(buffer);
  // extern double frieght_x;
  // extern double frieght_y;
  move_base::MoveBase move_base( buffer );

  ros::NodeHandle n_subs;
      // ros::Subscriber frieght_sub = n_subs.subscribe("model_pose", 1000, AjithPlannerROS::freight_pose_Callback);
  ros::Subscriber frieght_sub = n_subs.subscribe("/model_pose", 1000, freight_pose_Callback);
  // ROS_INFO("frieght position");
  //ros::MultiThreadedSpinner s;

  ros::spin();

  return(0);
}
