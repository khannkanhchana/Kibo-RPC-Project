
import math


class IntBallPose:
    def __init__(self, x, y, z, qx, qy, qz, qw):
        self.x = x
        self.y = y
        self.z = z

        self.qx = qx
        self.qy = qy
        self.qz = qz
        self.qw = qw

    def __str__(self):
        roll, pitch, yaw = self.get_euler_angles()

        return (
            f"Position: X={self.x:.2f}, Y={self.y:.2f}, Z={self.z:.2f}\n"
            f"Orientation Quaternion: "
            f"qx={self.qx:.3f}, qy={self.qy:.3f}, "
            f"qz={self.qz:.3f}, qw={self.qw:.3f}\n"
            f"Orientation Euler: "
            f"Roll={roll:.2f}°, Pitch={pitch:.2f}°, Yaw={yaw:.2f}°"
        )

    def get_euler_angles(self):
        sinr_cosp = 2 * (self.qw * self.qx + self.qy * self.qz)
        cosr_cosp = 1 - 2 * (self.qx**2 + self.qy**2)
        roll = math.atan2(sinr_cosp, cosr_cosp)

        sinp = 2 * (self.qw * self.qy - self.qz * self.qx)
        pitch = math.asin(max(-1.0, min(1.0, sinp)))

        siny_cosp = 2 * (self.qw * self.qz + self.qx * self.qy)
        cosy_cosp = 1 - 2 * (self.qy**2 + self.qz**2)
        yaw = math.atan2(siny_cosp, cosy_cosp)

        return (
            math.degrees(roll),
            math.degrees(pitch),
            math.degrees(yaw)
        )

    def is_valid(self):
        return (
            9.50 <= self.x <= 11.50
            and -5.00 <= self.y <= -3.00
            and 4.20 <= self.z <= 5.80
        )


if __name__ == "__main__":

    poses = [
        IntBallPose(10.50, -4.00, 5.00, 0.0, 0.0, 0.0, 1.0),
        IntBallPose(9.80, -3.50, 4.50, 0.0, 0.0, 0.0, 1.0),
        IntBallPose(12.00, -4.00, 6.00, 0.0, 0.0, 0.0, 1.0)
    ]

    for index, pose in enumerate(poses, start=1):
        print(f"\n========== Test Pose {index} ==========")
        print(pose)

        if pose.is_valid():
            print("Boundary Check: VALID - Inside Kibo limits")
        else:
            print("Boundary Check: INVALID - Outside Kibo limits")
