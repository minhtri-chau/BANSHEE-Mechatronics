import time
import motorctrl_v1 as motor
import Movement_Calc_v2 as calculation


BASE_ID = 1
BICEP_ID = 1
FOREARM_ID = 1
WRIST_ID = 1
CLAW_ID = 1

PORT_NUM = 'COM3'
BAUDRATE = 1000000

ALL_IDs = [BASE_ID, BICEP_ID, FOREARM_ID, WRIST_ID, CLAW_ID]
MOVE_IDs = [BASE_ID, BICEP_ID, FOREARM_ID, WRIST_ID]
COOR_1 = [5, -255, 40]                                      # In front of the chamber
COOR_2 = [5, -225, 40]                                      # Away from chamber      
COOR_REST = [275, 0, 205]  

def start_Arm():
    motor.portInitialization(PORT_NUM, ALL_IDs)
    print("DXL PORTS INITIALIZED \n")

def stop_Arm():
    motor.portTermination()
    print("DXL PORTS TERMINATED \n")

def battery_Pull():
    motor.dxlSetVelo([30,18,30,30,30], ALL_IDs)

    motor.motorRunWithInputs([90], [CLAW_ID])               # Open the claws

    angles = calculation.angle_Calc(COOR_1, 0)              # End effector positioned to the front of battery # Forearm always parallel to ground <-> 0 for Forearm Mode
    motor.simMotorRun(angles, MOVE_IDs)                     

    motor.motorRunWithInputs([180], [CLAW_ID])              # Close the claws

    angles = calculation.angle_Calc(COOR_2, 0)              # End effector pulled away from the chamber
    motor.simMotorRun(angles, MOVE_IDs)
    print("BATTERY PULLED\n")



                     
def battery_Push():
    motor.dxlSetVelo([30,18,30,30,30], ALL_IDs)

    motor.motorRunWithInputs([180], [CLAW_ID])              # Close the claws

    angles = calculation.angle_Calc(COOR_2, 0)              # End effector away from the chamber # Forearm always parallel to ground <-> 0 for Forearm Mode
    motor.simMotorRun(angles, MOVE_IDs)                     

    angles = calculation.angle_Calc(COOR_1, 0)              # End effector push battery into the chamber
    motor.simMotorRun(angles, MOVE_IDs)

    motor.motorRunWithInputs([90], [CLAW_ID])               # Open the claws
    print("BATTERY PUSHED\n")


def rest_Arm():
    motor.dxlSetVelo([30,18,30,30,30], ALL_IDs)

    angles = calculation.angle_Calc(COOR_REST, 0)
    motor.motorRunWithInputs(angles, MOVE_IDs)  
    print("ARM AT REST\n")



if __name__ == "__main__":
    start_Arm()
    time.sleep(2)
    battery_Pull()
    time.sleep(2)
    battery_Push()
    time.sleep(2)
    rest_Arm()
    stop_Arm()