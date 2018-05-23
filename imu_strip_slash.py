#!/usr/bin/env python2
# license removed for brevity
import rospy
from sensor_msgs.msg import Imu


def main():
  rospy.init_node('imu_strip_slash')
  publisher = rospy.Publisher('/imu_data_fixed', Imu, queue_size=1)
  #remove_frames = rospy.get_param('~remove_frames', [])

  def callback(msg):
    print msg.header.frame_id
    if msg.header.frame_id[0] is '/':
        # remove '/'
        msg.header.frame_id = msg.header.frame_id[1:]
    publisher.publish(msg)

  rospy.Subscriber('/imu/data', Imu, callback)
  rospy.spin()


if __name__ == '__main__':
  main()
