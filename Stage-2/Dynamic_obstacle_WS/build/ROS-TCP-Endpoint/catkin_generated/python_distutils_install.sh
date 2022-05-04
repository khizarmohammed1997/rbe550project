#!/bin/sh

if [ -n "$DESTDIR" ] ; then
    case $DESTDIR in
        /*) # ok
            ;;
        *)
            /bin/echo "DESTDIR argument must be absolute... "
            /bin/echo "otherwise python's distutils will bork things."
            exit 1
    esac
fi

echo_and_run() { echo "+ $@" ; "$@" ; }

echo_and_run cd "/home/krishnasathwik09/Dynamic_obstacle_WS/src/ROS-TCP-Endpoint"

# ensure that Python install destination exists
echo_and_run mkdir -p "$DESTDIR/home/krishnasathwik09/Dynamic_obstacle_WS/install/lib/python2.7/dist-packages"

# Note that PYTHONPATH is pulled from the environment to support installing
# into one location when some dependencies were installed in another
# location, #123.
echo_and_run /usr/bin/env \
    PYTHONPATH="/home/krishnasathwik09/Dynamic_obstacle_WS/install/lib/python2.7/dist-packages:/home/krishnasathwik09/Dynamic_obstacle_WS/build/lib/python2.7/dist-packages:$PYTHONPATH" \
    CATKIN_BINARY_DIR="/home/krishnasathwik09/Dynamic_obstacle_WS/build" \
    "/usr/bin/python2" \
    "/home/krishnasathwik09/Dynamic_obstacle_WS/src/ROS-TCP-Endpoint/setup.py" \
    egg_info --egg-base /home/krishnasathwik09/Dynamic_obstacle_WS/build/ROS-TCP-Endpoint \
    build --build-base "/home/krishnasathwik09/Dynamic_obstacle_WS/build/ROS-TCP-Endpoint" \
    install \
    --root="${DESTDIR-/}" \
    --install-layout=deb --prefix="/home/krishnasathwik09/Dynamic_obstacle_WS/install" --install-scripts="/home/krishnasathwik09/Dynamic_obstacle_WS/install/bin"
