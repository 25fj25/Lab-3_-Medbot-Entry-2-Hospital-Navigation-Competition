
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

drivetrain.set_drive_velocity(23, PERCENT)
drivetrain.drive_for(FORWARD, 775, MM)#; #// Drives forward for 750 mm from the start locaion to the center of the hallway
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 115, DEGREES)#; // Turns left 90º to drive down the hallway.
drivetrain.drive_for(FORWARD, 1000, MM)#; // Drives down the hallway and stops in front of Pharmacy
wait(.5, SECONDS)#; //TODO: Change the above code to not overrun. 
drivetrain.turn_for(RIGHT, 95, DEGREES)#; // Turns right 90º to face the Pharmacy.
drivetrain.drive_for(FORWARD, 540, MM)#; // Drives into the Pharmacy.
wait(5, SECONDS)#; // Waits 5 seconds to pick up the medication. 
drivetrain.drive_for(REVERSE, 525, MM)#; // Reverses out of the Pharmacy. 
# exit(129)
wait(.5, SECONDS)#;
drivetrain.turn_for(RIGHT, 95, DEGREES)#; // Drives up the hallway and stops in front of the Room 1. 
drivetrain.drive_for(FORWARD, 495 , MM)#; // 
wait(.5, SECONDS)
drivetrain.turn_for(LEFT, 110, DEGREES)#; // What the fuck
drivetrain.drive_for(FORWARD,500, MM)#; // Enters Room 1.
wait(3, SECONDS)#; // Waits 3 seconds to deliver medicine.                                                                                                              
drivetrain.drive_for(REVERSE, 485 , MM)#; // Reverses out of Room 1. 
wait(.5, SECONDS)#;
drivetrain.turn_for(RIGHT, 95, DEGREES)#; // Turns right to drive to the elevator. 
drivetrain.drive_for(FORWARD, 575 , MM)#; // Drives up the hallway and stops in from of the elevator. 
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns left 90º to face the elevator. 
drivetrain.drive_for(FORWARD, 500 , MM)#; // Drives into the elevator. 
wait(5, SECONDS)#; Waits 5 seconds for the elevator to reach Floor 2
drivetrain.drive_for(REVERSE, 650, MM)#; // Exits the elevator
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 110, DEGREES)#; // Turns left 90º to face the hallway
drivetrain.drive_for(FORWARD, 945, MM)#; // Drives down the entire hall
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 110, DEGREES)#; // Drives up the hallway and stops in front of the Room 1.
drivetrain.drive_for(FORWARD, 400, MM)
wait(3, SECONDS)
drivetrain.drive_for(REVERSE, 550, MM)#; // Reverses out of Room 2
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 110, DEGREES)#; // Turns left for 90º to face down the hallway
drivetrain.drive_for(FORWARD, 775, MM)#; // Drives down the hallway to the door of Room 3
wait(.5, SECONDS)#;
drivetrain.turn_for(RIGHT, 100, DEGREES)#; // Turns to face the door
drivetrain.drive_for(FORWARD, 400, MM)#; // Enters Room 3
wait(3, SECONDS)#; // Waits 3 seconds to drop off the drugs
drivetrain.drive_for(REVERSE, 475, MM)#; // Reverses out of Room 3
wait(.5, SECONDS)#;
drivetrain.turn_for(LEFT, 100, DEGREES)#; // Turns to drive back into the elevator
drivetrain.drive_for(FORWARD, 450, MM)#; // Drives down the hallway
wait(1, SECONDS)#;
drivetrain.turn_for(LEFT, 95, DEGREES)#; // Turns to face the elevator
drivetrain.drive_for(FORWARD, 775, MM)#; // Drives straight into the elevator and strikes the elevator doors
wait(5, SECONDS)#; // Wait five secoinds for the slow af elevator to reach first floor
drivetrain.drive_for(REVERSE, 1150, MM)#; // Runs out of the building screaming and never coming back again



    #}
#}

#// The below code executes the main method at the start of the runtime.
if __name__ == '__main__':
    Main.main([])
