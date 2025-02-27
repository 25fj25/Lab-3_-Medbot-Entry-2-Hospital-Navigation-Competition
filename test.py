#region VEXcode Generated Robot Configuration
from vex import *
import urandom

# Brain should be defined by default
brain=Brain()

# Robot configuration code
left_drive_smart = Motor(Ports.PORT1, GearSetting.RATIO_18_1, False)
right_drive_smart = Motor(Ports.PORT10, GearSetting.RATIO_18_1, True)
drivetrain = DriveTrain(left_drive_smart, right_drive_smart, 319.19, 295, 40, MM, 1)


# wait for rotation sensor to fully initialize
wait(30, MSEC)


# Make random actually random
def initializeRandomSeed():
    wait(100, MSEC)
    random = brain.battery.voltage(MV) + brain.battery.current(CurrentUnits.AMP) * 100 + brain.timer.system_high_res()
    urandom.seed(int(random))
      
# Set random seed 
initializeRandomSeed()


def play_vexcode_sound(sound_name):
    # Helper to make playing sounds from the V5 in VEXcode easier and
    # keeps the code cleaner by making it clear what is happening.
    print("VEXPlaySound:" + sound_name)
    wait(5, MSEC)

# add a small delay to make sure we don't print in the middle of the REPL header
wait(200, MSEC)
# clear the console to make sure we don't have the REPL in the console
print("\033[2J")

#endregion VEXcode Generated Robot Configuration

# ----------------------------------------------------------------------------
#                                                                            
#    Project:                                        
#    Author:  
#    Created:
#    Configuration: V5 Speedbot or TrainingBot (Drivetrain 2-motor, No Gyro)     
#                                                                            
# ----------------------------------------------------------------------------

# Library imports
from vex import *

# Begin project code
'''/* The code syntax will be in pseudo-Java syntax, which means it will follow Java syntax as much as possible;
Such as using `//` for single line comments, `/*` and `*/` for multi-line comments, adding a `;` after every line, etc. */'''
#// Defines class `Main` to wrap around all methods
class Main: #{
    #// Defines a static method `main` to encompass all code to be ran at runtime.
    # public static void main(List<Object> args)
    @staticmethod
    def main(args: list) -> None: #{
        NINETY_DEGREES: int = 125#;
        drivetrain.set_drive_velocity(23, PERCENT)
        drivetrain.set_turn_velocity(55, PERCENT)
        drivetrain.drive_for(FORWARD, 710 , MM)#; 
        #// Drives forward for .71m from the start locaion to the center of the hallway; converted into mm by multiplying with 1000.
        wait(.5, SECONDS)#;
        drivetrain.turn_for(LEFT, 140, DEGREES)#; // Turns left 90º to drive down the hallway.
        drivetrain.drive_for(FORWARD, 1100, MM)#; // Drives down the hallway and stops in front of Pharmacy
        wait(.5, SECONDS)#; //TODO: Change the above code to not overrun. 
        drivetrain.turn_for(RIGHT, 100, DEGREES)#; // Turns right 90º to face the Pharmacy.
        drivetrain.drive_for(FORWARD, .45 * 1000, MM)#; // Drives into the Pharmacy.
        wait(5, SECONDS)#; // Waits 5 seconds to pick up the medication. 
        drivetrain.drive_for(REVERSE, 550, MM)#; // Reverses out of the Pharmacy. 
        # exit(129)
        wait(.5, SECONDS)#;
        drivetrain.turn_for(RIGHT, 115, DEGREES)#; // Drives up the hallway and stops in front of the Room 1. 
        drivetrain.drive_for(FORWARD, .45 * 1000, MM)#; // Enters Room 1. 
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // English
        drivetrain.drive_for(FORWARD, 475, MM)#; // Enters Room 1.
        wait(3, SECONDS)#; // Waits 3 seconds to deliver medicine. 
        drivetrain.drive_for(REVERSE, .55 * 1000, MM)#; // Reverses out of Room 1. 
        wait(.5, SECONDS)#;
        drivetrain.turn_for(RIGHT, 100, DEGREES)#; // Turns right to drive to the elevator. 
        drivetrain.drive_for(FORWARD, 55 * 10, MM)#; // Drives up the hallway and stops in from of the elevator. 
        wait(1, SECONDS)#;
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns left 90º to face the elevator. 
        drivetrain.drive_for(FORWARD, 63 * 10, MM)#; // Drives into the elevator. 
        wait(5, SECONDS)#; Waits 5 seconds for the elevator to reach Floor 2
        drivetrain.drive_for(REVERSE, 67.9 * 10, MM)#; // Exits the elevator
        wait(.5, SECONDS)#;
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns left 90º to face the hallway
        drivetrain.drive_for(FORWARD, 975, MM)#; // Drives down the entire hall
        wait(.5, SECONDS)#;
        drivetrain.turn_for(RIGHT, 100, DEGREES)#; // Drives up the hallway and stops in front of the Room 1.
        drivetrain.drive_for(FORWARD, 524, MM)#; // Enter Room 2
        wait(3, SECONDS)#; // Waits 3 seconds to place medication
        drivetrain.drive_for(REVERSE, 550, MM)#; // Reverses out of Room 2
        wait(.5, SECONDS)#;
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns left for 90º to face down the hallway
        drivetrain.drive_for(FORWARD, 500, MM)#; // Drives down the hallway to the door of Room 3
        wait(.5, SECONDS)#;
        drivetrain.turn_for(RIGHT, 100, DEGREES)#; // Turns to face the door
        drivetrain.drive_for(FORWARD, 500, MM)#; // Enters Room 3
        wait(3, SECONDS)#; // Waits 3 seconds to drop off the drugs
        drivetrain.drive_for(REVERSE, 525, MM)#; // Reverses out of Room 3
        wait(.5, SECONDS)#;
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns to drive back into the elevator
        drivetrain.drive_for(FORWARD, 500, MM)#; // Drives down the hallway
        wait(1, SECONDS)#;
        drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns to face the elevator
        drivetrain.drive_for(FORWARD, 700, MM)#; // Drives straight into the elevator and strikes the elevator doors
        wait(5, SECONDS)#; // Wait five secoinds for the slow af elevator to reach first floor
        drivetrain.drive_for(REVERSE, 1000, MM)#; // Runs out of the building screaming and never coming back again
    #}
#}

#// The below code executes the main method at the start of the runtime.
if __name__ == '__main__':
    Main.main([])
