// Generated by gencpp from file gopher_move_it_config/PlanTrajectoryRequest.msg
// DO NOT EDIT!


#ifndef GOPHER_MOVE_IT_CONFIG_MESSAGE_PLANTRAJECTORYREQUEST_H
#define GOPHER_MOVE_IT_CONFIG_MESSAGE_PLANTRAJECTORYREQUEST_H


#include <string>
#include <vector>
#include <map>

#include <ros/types.h>
#include <ros/serialization.h>
#include <ros/builtin_message_traits.h>
#include <ros/message_operations.h>

#include <gopher_move_it_config/Joints.h>
#include <geometry_msgs/Pose.h>

namespace gopher_move_it_config
{
template <class ContainerAllocator>
struct PlanTrajectoryRequest_
{
  typedef PlanTrajectoryRequest_<ContainerAllocator> Type;

  PlanTrajectoryRequest_()
    : joints()
    , target()  {
    }
  PlanTrajectoryRequest_(const ContainerAllocator& _alloc)
    : joints(_alloc)
    , target(_alloc)  {
  (void)_alloc;
    }



   typedef  ::gopher_move_it_config::Joints_<ContainerAllocator>  _joints_type;
  _joints_type joints;

   typedef  ::geometry_msgs::Pose_<ContainerAllocator>  _target_type;
  _target_type target;





  typedef boost::shared_ptr< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> > Ptr;
  typedef boost::shared_ptr< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> const> ConstPtr;

}; // struct PlanTrajectoryRequest_

typedef ::gopher_move_it_config::PlanTrajectoryRequest_<std::allocator<void> > PlanTrajectoryRequest;

typedef boost::shared_ptr< ::gopher_move_it_config::PlanTrajectoryRequest > PlanTrajectoryRequestPtr;
typedef boost::shared_ptr< ::gopher_move_it_config::PlanTrajectoryRequest const> PlanTrajectoryRequestConstPtr;

// constants requiring out of line definition



template<typename ContainerAllocator>
std::ostream& operator<<(std::ostream& s, const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> & v)
{
ros::message_operations::Printer< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >::stream(s, "", v);
return s;
}


template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator==(const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator1> & lhs, const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator2> & rhs)
{
  return lhs.joints == rhs.joints &&
    lhs.target == rhs.target;
}

template<typename ContainerAllocator1, typename ContainerAllocator2>
bool operator!=(const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator1> & lhs, const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator2> & rhs)
{
  return !(lhs == rhs);
}


} // namespace gopher_move_it_config

namespace ros
{
namespace message_traits
{





template <class ContainerAllocator>
struct IsFixedSize< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct IsFixedSize< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> const>
  : FalseType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
  : TrueType
  { };

template <class ContainerAllocator>
struct IsMessage< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> const>
  : TrueType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
  : FalseType
  { };

template <class ContainerAllocator>
struct HasHeader< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> const>
  : FalseType
  { };


template<class ContainerAllocator>
struct MD5Sum< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "3bf313e1fc1f20a5ae89d4cd4412d92e";
  }

  static const char* value(const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator>&) { return value(); }
  static const uint64_t static_value1 = 0x3bf313e1fc1f20a5ULL;
  static const uint64_t static_value2 = 0xae89d4cd4412d92eULL;
};

template<class ContainerAllocator>
struct DataType< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "gopher_move_it_config/PlanTrajectoryRequest";
  }

  static const char* value(const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator>&) { return value(); }
};

template<class ContainerAllocator>
struct Definition< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
{
  static const char* value()
  {
    return "Joints joints\n"
"geometry_msgs/Pose target\n"
"\n"
"================================================================================\n"
"MSG: gopher_move_it_config/Joints\n"
"float64[] joints\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Pose\n"
"# A representation of pose in free space, composed of position and orientation. \n"
"Point position\n"
"Quaternion orientation\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Point\n"
"# This contains the position of a point in free space\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"\n"
"================================================================================\n"
"MSG: geometry_msgs/Quaternion\n"
"# This represents an orientation in free space in quaternion form.\n"
"\n"
"float64 x\n"
"float64 y\n"
"float64 z\n"
"float64 w\n"
;
  }

  static const char* value(const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator>&) { return value(); }
};

} // namespace message_traits
} // namespace ros

namespace ros
{
namespace serialization
{

  template<class ContainerAllocator> struct Serializer< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
  {
    template<typename Stream, typename T> inline static void allInOne(Stream& stream, T m)
    {
      stream.next(m.joints);
      stream.next(m.target);
    }

    ROS_DECLARE_ALLINONE_SERIALIZER
  }; // struct PlanTrajectoryRequest_

} // namespace serialization
} // namespace ros

namespace ros
{
namespace message_operations
{

template<class ContainerAllocator>
struct Printer< ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator> >
{
  template<typename Stream> static void stream(Stream& s, const std::string& indent, const ::gopher_move_it_config::PlanTrajectoryRequest_<ContainerAllocator>& v)
  {
    s << indent << "joints: ";
    s << std::endl;
    Printer< ::gopher_move_it_config::Joints_<ContainerAllocator> >::stream(s, indent + "  ", v.joints);
    s << indent << "target: ";
    s << std::endl;
    Printer< ::geometry_msgs::Pose_<ContainerAllocator> >::stream(s, indent + "  ", v.target);
  }
};

} // namespace message_operations
} // namespace ros

#endif // GOPHER_MOVE_IT_CONFIG_MESSAGE_PLANTRAJECTORYREQUEST_H
