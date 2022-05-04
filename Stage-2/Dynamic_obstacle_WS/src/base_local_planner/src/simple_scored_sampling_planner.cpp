/*********************************************************************
 *
 * Software License Agreement (BSD License)
 *
 *  Copyright (c) 2008, Willow Garage, Inc.
 *  All rights reserved.
 *
 *  Redistribution and use in source and binary forms, with or without
 *  modification, are permitted provided that the following conditions
 *  are met:
 *
 *   * Redistributions of source code must retain the above copyright
 *     notice, this list of conditions and the following disclaimer.
 *   * Redistributions in binary form must reproduce the above
 *     copyright notice, this list of conditions and the following
 *     disclaimer in the documentation and/or other materials provided
 *     with the distribution.
 *   * Neither the name of Willow Garage, Inc. nor the names of its
 *     contributors may be used to endorse or promote products derived
 *     from this software without specific prior written permission.
 *
 *  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS
 *  "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT
 *  LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS
 *  FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
 *  COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT,
 *  INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
 *  BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
 *  LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
 *  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT
 *  LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN
 *  ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
 *  POSSIBILITY OF SUCH DAMAGE.
 *
 * Author: TKruse
 *********************************************************************/

#include <base_local_planner/simple_scored_sampling_planner.h>

#include <ros/console.h>
#include <iostream>
#include<cmath>
using namespace std;
namespace base_local_planner {
  
  SimpleScoredSamplingPlanner::SimpleScoredSamplingPlanner(std::vector<TrajectorySampleGenerator*> gen_list, std::vector<TrajectoryCostFunction*>& critics, int max_samples) {
    max_samples_ = max_samples;
    gen_list_ = gen_list;
    critics_ = critics;
  }

  double SimpleScoredSamplingPlanner::scoreTrajectory(Trajectory& traj, double best_traj_cost) {
    double traj_cost = 0;
    int gen_id = 0;
    for(std::vector<TrajectoryCostFunction*>::iterator score_function = critics_.begin(); score_function != critics_.end(); ++score_function) {
      TrajectoryCostFunction* score_function_p = *score_function;
      if (score_function_p->getScale() == 0) {
        continue;
      }
      double cost = score_function_p->scoreTrajectory(traj);
      if (cost < 0) {
        ROS_DEBUG("Velocity %.3lf, %.3lf, %.3lf discarded by cost function  %d with cost: %f", traj.xv_, traj.yv_, traj.thetav_, gen_id, cost);
        traj_cost = cost;
        break;
      }
      if (cost != 0) {
        cost *= score_function_p->getScale();
      }
      traj_cost += cost;
      if (best_traj_cost > 0) {
        // since we keep adding positives, once we are worse than the best, we will stay worse
        if (traj_cost > best_traj_cost) {
          break;
        }
      }
      gen_id ++;
    }


    return traj_cost;
  }

  void SimpleScoredSamplingPlanner::velocity_cone_data(double rbt_x,double rbt_y) {
    r_x = rbt_x;
    r_y = rbt_y;
    r_radius = 0.01;
  }

  void SimpleScoredSamplingPlanner::obstacle_data(double frieght_x,double frieght_y,double frieght_theta) {
    obs_x = frieght_x;
    obs_y = frieght_y;
    obs_radius = 0.2;
    // obstacle_Vx = 0.15 * cos(frieght_theta);
    // obstacle_Vy = 0.15 * sin(frieght_theta);
    obstacle_Vx = -0.15;
    obstacle_Vy = 0;
  }
  bool SimpleScoredSamplingPlanner::check_within_vo(double traj_vel_x,double traj_vel_y) {
    bool cone_flag;
    double relvx;
    double relvy;
    double rx;
    double ry;
    double r2;
    double rvel2;
    double dot_prod2;
    double cr2;
    // # compute the relative velocity
    relvx = traj_vel_x - obstacle_Vx;
    relvy = traj_vel_y - obstacle_Vy;
    // # compute the relative position
    rx = obs_x - r_x;
    ry = obs_y - r_y;
    // 
    r2 = pow(rx,2) + pow(ry,2);
    rvel2 = pow(relvx,2) + pow(relvy,2);
    dot_prod2 = pow((rx*relvx + ry*relvy),2);
    
    // # compute the configuration radius
    cr2 = pow((obs_radius + r_radius),2);
    
    //  compute the constraint condition 
    cone_flag = (r2 - dot_prod2 / rvel2) >= cr2;
    return cone_flag;
  }

  bool SimpleScoredSamplingPlanner::findBestTrajectory(Trajectory& traj, std::vector<Trajectory>* all_explored) {
    Trajectory loop_traj;
    Trajectory best_traj;
    double loop_traj_cost, best_traj_cost = -1;
    bool gen_success;
    bool velocity_cone_flag;
    int count, count_valid;
    for (std::vector<TrajectoryCostFunction*>::iterator loop_critic = critics_.begin(); loop_critic != critics_.end(); ++loop_critic) {
      TrajectoryCostFunction* loop_critic_p = *loop_critic;
      if (loop_critic_p->prepare() == false) {
        ROS_WARN("A scoring function failed to prepare");
        return false;
      }
    }

     /*build velocity cone */
    // flag =
    // velocity_cone_data();
    // velocity_cone_flag = check_within_vo();
    // ROS_INFO("Robot Position %f",r_y);
    //  ROS_INFO("DWA frieght position %f",obs_y);
    for (std::vector<TrajectorySampleGenerator*>::iterator loop_gen = gen_list_.begin(); loop_gen != gen_list_.end(); ++loop_gen) {
      count = 0;
      count_valid = 0;
      TrajectorySampleGenerator* gen_ = *loop_gen;
      bool velocity_cone_flag;
      while (gen_->hasMoreTrajectories()) {
        gen_success = gen_->nextTrajectory(loop_traj);
        if (gen_success == false) {
          // TODO use this for debugging
          continue;
        }
        loop_traj_cost = scoreTrajectory(loop_traj, best_traj_cost);

        if (all_explored != NULL) {
          loop_traj.cost_ = loop_traj_cost;
          all_explored->push_back(loop_traj);
        }
        //Sathwik : if trajectory lies in velocity cone add cost to it //////////////////////////////////////////
        // ROS_INFO("Trajectory cost before %f",loop_traj.cost_);
        velocity_cone_flag = check_within_vo(loop_traj.xv_,loop_traj.yv_);
        velocity_cone_flag = 0;
        if (velocity_cone_flag == 1){
          loop_traj.cost_ = loop_traj.cost_ + 0.5;
          velocity_cone_flag = 0;
          // ROS_INFO("inside cone before %f",loop_traj.xv_);
        }
        // ROS_INFO("outside cone before %f",loop_traj.cost_);
        // ROS_INFO("Trajectory cost after %f",loop_traj.cost_);
        // ROS_INFO("loop trajectory %d ",loop_traj_cost);
        if (loop_traj_cost >= 0) {
          count_valid++;
          if (best_traj_cost < 0 || loop_traj_cost < best_traj_cost) {
            best_traj_cost = loop_traj_cost;
            best_traj = loop_traj;
          }
        }
        count++;
        if (max_samples_ > 0 && count >= max_samples_) {
          break;
        }        
      }
      // ROS_INFO("Best trajectory cost %f",best_traj_cost);
      if (best_traj_cost >= 0) {
        traj.xv_ = best_traj.xv_;
        traj.yv_ = best_traj.yv_;
        traj.thetav_ = best_traj.thetav_;
        traj.cost_ = best_traj_cost;
        traj.resetPoints();
        double px, py, pth;
        for (unsigned int i = 0; i < best_traj.getPointsSize(); i++) {
          best_traj.getPoint(i, px, py, pth);
          traj.addPoint(px, py, pth);
        }
      }
      ROS_DEBUG("Evaluated %d trajectories, found %d valid", count, count_valid);
      if (best_traj_cost >= 0) {
        // do not try fallback generators
        break;
      }
    }
    return best_traj_cost >= 0;
  }


  
}// namespace
