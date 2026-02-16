from .gestures import *
from .numerics import *
from .environment import environment
import math

class GestureTracker:
    def __init__(self, inventory):
        self.enter = None
        self.leave = None
        
        self._inventory = inventory
        
        self.aimPistol = Gesture(0.02, 0.03)
        self.aimRifleLeft = Gesture(-0.2, -0.1)
        self.aimRifleRight = Gesture(-0.2, -0.1)
        self.buttonA = Gesture(-0.8, -0.7)
        self.buttonB = Gesture(-0.8, -0.7)
        self.buttonX = Gesture(-0.8, -0.7)
        self.buttonY = Gesture(-0.8, -0.7)
        self.buttonLeftStick = Gesture(-0.8, -0.7)
        self.buttonLeftStickUp = Gesture(-0.2, -0.05)
        self.buttonLeftStickDown = Gesture(-0.2, -0.1)
        self.buttonLeftStickLeft = Gesture(-0.2, -0.1)
        self.buttonLeftStickRight = Gesture(-0.2, -0.1)
        self.buttonLeftStickInnerRing = Gesture(0.5, 0.5)
        self.buttonLeftStickOuterRing = Gesture(-0.9, -0.9)
        self.buttonRightStick = Gesture(-0.8, -0.7)
        self.buttonRightStickUp = Gesture(-0.2, -0.05)
        self.buttonRightStickDown = Gesture(-0.2, -0.1)
        self.buttonRightStickLeft = Gesture(-0.2, -0.1)
        self.buttonRightStickRight = Gesture(-0.2, -0.1)
        self.buttonRightStickInnerRing = Gesture(0.5, 0.5)
        self.buttonRightStickOuterRing = Gesture(-0.9, -0.9)
        self.duck = Gesture(-0.2, -0.1)
        self.gripLeft = Gesture(-0.6, -0.4)
        self.gripRight = Gesture(-0.6, -0.4)
        self.holsterInventoryLeft = LocationBasedGesture(0.05, 0.1, Vector(-0.3, -0.75, 0.1))
        self.holsterInventoryRight = LocationBasedGesture(0.05, 0.1, Vector(0.3, -0.75, 0.1))
        self.holsterWeaponLeft = LocationBasedGesture(0.05, 0.1, Vector(-0.3, -0.75, 0.1))
        self.holsterWeaponRight = LocationBasedGesture(0.02, 0.05, Vector(0.3, -0.75, 0.1))
        self.leanLeft = Gesture(-0.55, -0.45)
        self.leanRight = Gesture(-0.55, -0.45)
        self.lightLeft = LocationBasedGesture(0.04, 0.05, Vector(0,0,0))
        self.lightRight = LocationBasedGesture(0.04, 0.05, Vector(0,0,0))
        self.lowerAreaLeft = Gesture(-0.7, -0.6)
        self.lowerAreaRight = Gesture(-0.7, -0.6)
        self.meleeLeft = Gesture(-12.0, -10.0)
        self.meleeLeftAlt = Gesture(-3, -2.0)
        self.meleeLeftAltPull = Gesture(-3, -2.0)
        self.meleeLeftAltPush = Gesture(-3, -2.0)
        self.meleeRight = InventoryGesture(-8.0, -6.0, inventory)
        self.meleeRightAlt = InventoryGesture(-3, -2.0, inventory)
        self.meleeRightAltPull = InventoryGesture(-3, -2.0, inventory)
        self.meleeRightAltPush = InventoryGesture(-3, -2.0, inventory)
        self.shoulderInventoryLeft = LocationBasedGesture(0.01, 0.02, Vector(-0.25, 0, 0.1))
        self.shoulderInventoryRight = LocationBasedGesture(0.05, 0.1, Vector(0.3, 0, 0))
        self.shoulderWeaponLeft = LocationBasedGesture(0.05, 0.05, Vector(-0.3, 0, 0))
        self.shoulderWeaponRight = LocationBasedGesture(0.01, 0.02, Vector(0.25, 0, 0.1))
        self.triggerLeft = Gesture(-0.6, -0.4)
        self.triggerRight = InventoryGesture(-0.6, -0.4, inventory)
        self.weaponInventory = inventory
        self.upperAreaLeft = Gesture(-0.2, -0.1)
        self.upperAreaRight = Gesture(-0.2, -0.1)
        self.useLeft = Gesture(-0.9, -0.8)
        self.useRight = Gesture(-0.9, -0.8)
        self.useLeftUp = Gesture(-0.8, -0.7)
        self.useRightUp = Gesture(-0.8, -0.7)
        self.foreheadLeft = LocationBasedGesture(0.02, 0.04, Vector(0, 0.05, -0.15))
        self.foreheadRight = LocationBasedGesture(0.02, 0.04, Vector(0, 0.05, -0.15))

        self.swipeLeftHandLeft = Gesture(-0.8, -0.6)                            
        self.swipeLeftHandRight = Gesture(-0.8, -0.6)
        self.swipeLeftHandUp = Gesture(-0.8, -0.6)
        self.swipeLeftHandDown = Gesture(-0.8, -0.6)
        self.swipeRightHandLeft = Gesture(-0.8, -0.6)                           
        self.swipeRightHandRight = Gesture(-0.8, -0.6)
        self.swipeRightHandUp = Gesture(-0.8, -0.6)
        self.swipeRightHandDown = Gesture(-0.8, -0.6)

        self.circleSkyLeft = Gesture(-0.7, -0.5)
        self.circleSkyRight = Gesture(-0.7, -0.5)
        self.circleFloorLeft = Gesture(-0.7, -0.5)
        self.circleFloorRight = Gesture(-0.7, -0.5)

        self.shakeLeft = Gesture(-0.8, -0.6)
        self.shakeRight = Gesture(-0.8, -0.6)

        self.thrustLeft = Gesture(-12.0, -8.0)
        self.retractLeft = Gesture(-12.0, -8.0)
        self.thrustRight = Gesture(-12.0, -8.0)
        self.retractRight = Gesture(-12.0, -8.0)
        
        self.leftMeleeAltThreshold = -0.5
        self.rightMeleeAltThreshold = -0.5
        
        self.meleeLeft.CoolDown = 0.2
        self.meleeLeftAlt.CoolDown = 0.2
        self.meleeLeftAltPull.CoolDown = 0.2
        self.meleeLeftAltPush.CoolDown = 0.2
        self.meleeRight.CoolDown = 0.2
        self.meleeRightAlt.CoolDown = 0.2
        self.meleeRightAltPull.CoolDown = 0.2
        self.meleeRightAltPush.CoolDown = 0.2
        self.swipeLeftHandLeft.CoolDown = 0.5
        self.swipeLeftHandRight.CoolDown = 0.5
        self.swipeLeftHandUp.CoolDown = 0.5
        self.swipeLeftHandDown.CoolDown = 0.5
        self.swipeRightHandLeft.CoolDown = 0.5
        self.swipeRightHandRight.CoolDown = 0.5
        self.swipeRightHandUp.CoolDown = 0.5
        self.swipeRightHandDown.CoolDown = 0.5
        self.circleSkyLeft.CoolDown = 1.0
        self.circleSkyRight.CoolDown = 1.0
        self.circleFloorLeft.CoolDown = 1.0
        self.circleFloorRight.CoolDown = 1.0
        self.shakeLeft.CoolDown = 0.2
        self.shakeRight.CoolDown = 0.2
        self.thrustLeft.CoolDown = 0.5
        self.retractLeft.CoolDown = 0.5
        self.thrustRight.CoolDown = 0.5
        self.retractRight.CoolDown = 0.5
        
        GestureValidation_None = 0
        GestureValidation_Delay = 1
        GestureValidation_Trigger = 2
        GestureValidation_Grip = 3
    
        self.triggerLeft.validationMode = GestureValidation_Trigger
        self.triggerRight.validationMode = GestureValidation_Trigger
        self.gripLeft.validationMode = GestureValidation_Grip
        self.gripRight.validationMode = GestureValidation_Grip
                
        self.fireWeaponLeft = self.triggerLeft
        self.fireWeaponRight = self.triggerRight        
        self.grabLeft = self.gripLeft
        self.grabRight = self.gripRight
        
        self._locationBasedGesturesLeft = [
            self.holsterInventoryLeft,
            self.holsterInventoryRight,
            self.lightLeft,
            self.shoulderInventoryLeft,
            self.shoulderInventoryRight,
            self.foreheadLeft
        ]
        
        self._locationBasedGesturesRight = [
            self.holsterWeaponLeft,
            self.holsterWeaponRight,
            self.lightRight,
            self.shoulderWeaponLeft,
            self.shoulderWeaponRight,
            self.foreheadRight
        ]
        
        self._allGestures = [
            self.aimPistol,
            self.aimRifleLeft,
            self.aimRifleRight,
            self.buttonA,
            self.buttonB,
            self.buttonX,
            self.buttonY,
            self.buttonLeftStick,
            self.buttonLeftStickUp,
            self.buttonLeftStickDown,
            self.buttonLeftStickLeft,
            self.buttonLeftStickRight,
            self.buttonLeftStickInnerRing,
            self.buttonLeftStickOuterRing,
            self.buttonRightStick,
            self.buttonRightStickUp,
            self.buttonRightStickDown,
            self.buttonRightStickLeft,
            self.buttonRightStickRight,
            self.buttonRightStickInnerRing,
            self.buttonRightStickOuterRing,
            self.duck,
            self.gripLeft,
            self.gripRight,
            self.holsterInventoryLeft,
            self.holsterInventoryRight,
            self.holsterWeaponLeft,
            self.holsterWeaponRight,
            self.leanLeft,
            self.leanRight,
            self.lightLeft,
            self.lightRight,
            self.lowerAreaLeft,
            self.lowerAreaRight,
            self.meleeLeft,
            self.meleeLeftAlt,
            self.meleeLeftAltPull,
            self.meleeLeftAltPush,
            self.meleeRight,
            self.meleeRightAlt,
            self.meleeRightAltPull,
            self.meleeRightAltPush,
            self.shoulderInventoryLeft,
            self.shoulderInventoryRight,
            self.shoulderWeaponLeft,
            self.shoulderWeaponRight,
            self.triggerLeft,
            self.triggerRight,
            self.upperAreaLeft,
            self.upperAreaRight,
            self.useLeft,
            self.useRight,
            self.useLeftUp,
            self.useRightUp,
            self.swipeLeftHandLeft,
            self.swipeLeftHandRight,
            self.swipeLeftHandUp,
            self.swipeLeftHandDown,
            self.swipeRightHandLeft,
            self.swipeRightHandRight,
            self.swipeRightHandUp,
            self.swipeRightHandDown,
            self.foreheadLeft,
            self.foreheadRight,
            self.circleSkyLeft,
            self.circleSkyRight,
            self.circleFloorLeft,
            self.circleFloorRight,
            self.shakeLeft,
            self.shakeRight,
            self.thrustLeft,
            self.retractLeft,
            self.thrustRight,
            self.retractRight
        ]
    
    def addLocationBasedGesture(self, leftHand, lowerThreshold, upperThreshold, offset):
        gesture = LocationBasedGesture(lowerThreshold, upperThreshold, offset)
        if leftHand:
            self._locationBasedGesturesLeft.append(gesture)
        else:
            self._locationBasedGesturesRight.append(gesture)
        self._allGestures.append(gesture)
        return gesture
   
    def reset(self):
        for gesture in self._allGestures:
            gesture.reset()
                        
    def update(self, currentTime, deltaTime):        
        if environment.openVR.isMounted == False:
            return
        
        leftValidation = GestureValidation(environment.openVR.leftTrigger, environment.openVR.leftGrip)
        rightValidation = GestureValidation(environment.openVR.rightTrigger, environment.openVR.rightGrip)
        noneValidation = GestureValidation(1,1)
        
        item = self._inventory.get()
        
        h_fwd = environment.openVR.headPose.forward
        h_left = environment.openVR.headPose.left 
        
        mag_fwd = math.sqrt(h_fwd.x*h_fwd.x + h_fwd.z*h_fwd.z)
        if mag_fwd < 0.001: mag_fwd = 1
        fx = h_fwd.x / mag_fwd
        fz = h_fwd.z / mag_fwd
        
        mag_left = math.sqrt(h_left.x*h_left.x + h_left.z*h_left.z)
        if mag_left < 0.001: mag_left = 1
        lx = h_left.x / mag_left
        lz = h_left.z / mag_left
        
        rx = -lx
        rz = -lz

        swipe_speed_threshold = 0.35
        swipe_purity = 1.5
        shake_min = 0.8
        shake_max = 2.5
        shake_maintain = 0.8
        thrust_retract_min = 8.0
        thrust_retract_max = 12.0
        thrust_retract_purity = 1.5
        
        if self.lowerAreaLeft.enabled:
            self.lowerAreaLeft.update(currentTime, environment.openVR.leftTouchPose.position.y - environment.openVR.headPose.position.y, leftValidation)
        
        if self.lowerAreaRight.enabled:
            self.lowerAreaRight.update(currentTime, environment.openVR.rightTouchPose.position.y - environment.openVR.headPose.position.y, rightValidation)
        
        if self.upperAreaLeft.enabled:
            self.upperAreaLeft.update(currentTime, environment.openVR.headPose.position.y - environment.openVR.leftTouchPose.position.y, leftValidation)
        
        if self.upperAreaRight.enabled:
            self.upperAreaRight.update(currentTime, environment.openVR.headPose.position.y - environment.openVR.rightTouchPose.position.y, rightValidation)
        
        if self.aimPistol.enabled:
            dx = environment.openVR.leftTouchPose.position.x - environment.openVR.rightTouchPose.position.x
            dy = environment.openVR.leftTouchPose.position.y - environment.openVR.rightTouchPose.position.y
            dz = environment.openVR.leftTouchPose.position.z - environment.openVR.rightTouchPose.position.z
            d = dx*dx + dy*dy + dz*dz
            self.aimPistol.update(currentTime, d, leftValidation) 
                        
        if self.aimRifleRight.enabled:
            if self.aimPistol.inGesture or dotProduct(environment.openVR.leftTouchPose.forward, environment.openVR.headPose.forward) < 0.5:
                self.aimRifleRight.update(currentTime, 0, rightValidation)
            else:
                dx = environment.openVR.rightTouchPose.position.x - environment.openVR.headPose.position.x
                dz = environment.openVR.rightTouchPose.position.z - environment.openVR.headPose.position.z
                d = dx*dx + dz*dz
                self.aimRifleRight.update(currentTime, -d, rightValidation)
            
        if self.aimRifleLeft.enabled:
            if self.aimPistol.inGesture or self.aimRifleRight.inGesture or dotProduct(environment.openVR.leftTouchPose.forward, environment.openVR.headPose.forward) < 0.5:
                self.aimRifleLeft.update(currentTime, 0, leftValidation)
            else:
                dx = environment.openVR.leftTouchPose.position.x - environment.openVR.headPose.position.x
                dz = environment.openVR.leftTouchPose.position.z - environment.openVR.headPose.position.z
                d = dx*dx + dz*dz
                self.aimRifleLeft.update(currentTime, -d, leftValidation)
        
        if self.buttonA.enabled:
            self.buttonA.update(currentTime, -environment.openVR.a, rightValidation)
        if self.buttonB.enabled:
            self.buttonB.update(currentTime, -environment.openVR.b, rightValidation)
        if self.buttonRightStick.enabled:
            self.buttonRightStick.update(currentTime, -environment.openVR.rightStick, rightValidation)
            
        if self.buttonX.enabled:
            self.buttonX.update(currentTime, -environment.openVR.x, leftValidation)
        if self.buttonY.enabled:
            self.buttonY.update(currentTime, -environment.openVR.y, leftValidation)
        if self.buttonLeftStick.enabled:
            self.buttonLeftStick.update(currentTime, -environment.openVR.leftStick, leftValidation)
            
        if self.buttonLeftStickUp.enabled:
            self.buttonLeftStickUp.update(currentTime, -environment.openVR.leftStickAxes.y, leftValidation)
        if self.buttonLeftStickDown.enabled:
            self.buttonLeftStickDown.update(currentTime, environment.openVR.leftStickAxes.y, leftValidation)
        if self.buttonLeftStickLeft.enabled:
            self.buttonLeftStickLeft.update(currentTime, environment.openVR.leftStickAxes.x, leftValidation)
        if self.buttonLeftStickRight.enabled:
            self.buttonLeftStickRight.update(currentTime, -environment.openVR.leftStickAxes.x, leftValidation)
                
        leftStick = math.sqrt(environment.openVR.leftStickAxes.x*environment.openVR.leftStickAxes.x + environment.openVR.leftStickAxes.y*environment.openVR.leftStickAxes.y)
        if self.buttonLeftStickInnerRing.enabled:
            self.buttonLeftStickInnerRing.update(currentTime, leftStick, leftValidation)
        if self.buttonLeftStickOuterRing.enabled:
            self.buttonLeftStickOuterRing.update(currentTime, -leftStick, leftValidation)
         
        if self.buttonRightStickUp.enabled:
            self.buttonRightStickUp.update(currentTime, -environment.openVR.rightStickAxes.y, rightValidation)
        if self.buttonRightStickDown.enabled:
            self.buttonRightStickDown.update(currentTime, environment.openVR.rightStickAxes.y, rightValidation)        
        if self.buttonRightStickLeft.enabled:
            self.buttonRightStickLeft.update(currentTime, environment.openVR.rightStickAxes.x, rightValidation)            
        if self.buttonRightStickRight.enabled:
            self.buttonRightStickRight.update(currentTime, -environment.openVR.rightStickAxes.x, rightValidation)
        
        rightStick = math.sqrt(environment.openVR.rightStickAxes.x*environment.openVR.rightStickAxes.x + environment.openVR.rightStickAxes.y*environment.openVR.rightStickAxes.y)
        if self.buttonRightStickInnerRing.enabled:
            self.buttonRightStickInnerRing.update(currentTime, rightStick, rightValidation)
        if self.buttonRightStickOuterRing.enabled:
            self.buttonRightStickOuterRing.update(currentTime, -rightStick, rightValidation)
        
        if self.duck.enabled:
            self.duck.update(currentTime, environment.openVR.headPose.position.y - environment.headController.standingHeight, noneValidation)
        
        roll = getRoll(environment.openVR.headPose)
        if self.leanLeft.enabled:
            self.leanLeft.update(currentTime, roll - environment.rollCenter, noneValidation)
        
        if self.leanRight.enabled:
            self.leanRight.update(currentTime, environment.rollCenter - roll, noneValidation)

        l_pose, r_pose = environment.openVR.leftTouchPose, environment.openVR.rightTouchPose        
        dwx_l = (l_pose.position.x - environment.leftController.x) / deltaTime
        dy_l = (l_pose.position.y - environment.leftController.y) / deltaTime
        dwz_l = (l_pose.position.z - environment.leftController.z) / deltaTime
        dx_l = dwx_l * rx + dwz_l * rz
        dz_l = dwx_l * fx + dwz_l * fz
        d_melee_l = (dwx_l*dwx_l + dy_l*dy_l + dwz_l*dwz_l)
        speed_l = math.sqrt(d_melee_l)
        speed_xz_l = math.sqrt(dx_l*dx_l + dz_l*dz_l)
        is_l_horizontal = abs(l_pose.forward.y) < 0.5
        is_l_vertical = abs(l_pose.forward.y) > 0.9
        is_pure_z_l = abs(dz_l) > (abs(dx_l) + abs(dy_l)) * thrust_retract_purity
        leftMeleeAction = -1

        if self.useLeft.enabled:
            self.useLeft.update(currentTime, environment.openVR.leftTouchPose.left.y, leftValidation)            
        if self.useLeftUp.enabled:
            self.useLeftUp.update(currentTime, -environment.openVR.leftTouchPose.left.y, leftValidation)

        if self.circleSkyLeft.enabled:
            if d_melee_l > 2:
                self.circleSkyLeft.update(currentTime, 0, leftValidation)
            elif not self.circleSkyLeft.inGesture:
                if l_pose.forward.y < -0.9 and speed_xz_l > 1 and speed_xz_l > (abs(dy_l) * 1.5):
                    self.circleSkyLeft.update(currentTime, -1.0, leftValidation)
                else:
                    self.circleSkyLeft.update(currentTime, 0, leftValidation)
            else:
                self.circleSkyLeft.update(currentTime, -1.0 if speed_l > 0.1 else 0, leftValidation)

        if self.circleFloorLeft.enabled:
            if d_melee_l > 2:
                self.circleFloorLeft.update(currentTime, 0, leftValidation)
            elif not self.circleFloorLeft.inGesture:
                if l_pose.forward.y > 0.9 and speed_xz_l > 1 and speed_xz_l > (abs(dy_l) * 1.5):
                    self.circleFloorLeft.update(currentTime, -1.0, leftValidation)
                else:
                    self.circleFloorLeft.update(currentTime, 0, leftValidation)
            else:
                self.circleFloorLeft.update(currentTime, -1.0 if speed_l > 0.1 else 0, leftValidation)

        if leftMeleeAction == -1:
            swipe_l_up_input = 0
            swipe_l_down_input = 0
            swipe_l_left_input = 0
            swipe_l_right_input = 0
            if speed_l > swipe_speed_threshold and is_l_horizontal:
                if abs(dy_l) > (abs(dx_l) + abs(dz_l)) * swipe_purity:
                    if dy_l > 0: swipe_l_up_input = -speed_l
                    else: swipe_l_down_input = -speed_l
                elif abs(dx_l) > (abs(dy_l) + abs(dz_l)) * swipe_purity:
                    if dx_l > 0: swipe_l_left_input = -speed_l
                    else: swipe_l_right_input = -speed_l
            self.swipeLeftHandUp.update(currentTime, swipe_l_up_input, leftValidation)
            self.swipeLeftHandDown.update(currentTime, swipe_l_down_input, leftValidation)
            self.swipeLeftHandLeft.update(currentTime, swipe_l_left_input, leftValidation)
            self.swipeLeftHandRight.update(currentTime, swipe_l_right_input, leftValidation)
            if (self.swipeLeftHandUp.inGesture or self.swipeLeftHandDown.inGesture or 
                self.swipeLeftHandLeft.inGesture or self.swipeLeftHandRight.inGesture):
                leftMeleeAction = 5

        if leftMeleeAction == -1:
            thrust_l_input = 0
            if d_melee_l > thrust_retract_min and dz_l < 0 and is_pure_z_l:
                thrust_l_input = -d_melee_l
            self.thrustLeft.update(currentTime, thrust_l_input, leftValidation)
            if self.thrustLeft.inGesture:
                leftMeleeAction = 6

        if leftMeleeAction == -1:
            retract_l_input = 0
            if d_melee_l > thrust_retract_min and dz_l > 0 and is_pure_z_l:
                retract_l_input = -d_melee_l
            self.retractLeft.update(currentTime, retract_l_input, leftValidation)
            if self.retractLeft.inGesture:
                leftMeleeAction = 7

        if leftMeleeAction == -1:
            shake_l_input = 0
            if abs(dz_l) < 0.5:
                if not self.shakeLeft.inGesture:
                    if shake_min < speed_l < shake_max:
                        shake_l_input = -1.0
                else:
                    if speed_l > shake_maintain:
                        shake_l_input = -1.0
            self.shakeLeft.update(currentTime, shake_l_input, leftValidation)
            if self.shakeLeft.inGesture:
                leftMeleeAction = 4

        if leftMeleeAction == -1:
            melee_l_push_input = 0
            if l_pose.forward.y < self.leftMeleeAltThreshold:
                dot = dotProduct(l_pose.left, environment.openVR.headPose.forward)
                if self.meleeLeftAltPush.enabled and dot < -0.5:
                    melee_l_push_input = -d_melee_l
            self.meleeLeftAltPush.update(currentTime, melee_l_push_input, leftValidation)
            if self.meleeLeftAltPush.inGesture:
                leftMeleeAction = 2

        if leftMeleeAction == -1:
            melee_l_pull_input = 0
            if l_pose.forward.y < self.leftMeleeAltThreshold:
                dot = dotProduct(l_pose.left, environment.openVR.headPose.forward)
                if self.meleeLeftAltPull.enabled and dot > 0.5:
                    melee_l_pull_input = -d_melee_l
            self.meleeLeftAltPull.update(currentTime, melee_l_pull_input, leftValidation)
            if self.meleeLeftAltPull.inGesture:
                leftMeleeAction = 3

        if leftMeleeAction == -1:
            melee_l_alt_input = 0
            if l_pose.forward.y < self.leftMeleeAltThreshold:
                if self.meleeLeftAlt.enabled:
                    melee_l_alt_input = -d_melee_l
            self.meleeLeftAlt.update(currentTime, melee_l_alt_input, leftValidation)
            if self.meleeLeftAlt.inGesture:
                leftMeleeAction = 1

        if leftMeleeAction == -1 and self.meleeLeft.enabled:
            melee_l_input = 0
            if not (is_pure_z_l or (is_l_vertical and abs(dy_l) <= 1.5)):
                melee_l_input = -d_melee_l
            self.meleeLeft.update(currentTime, melee_l_input, leftValidation)
            if self.meleeLeft.inGesture:
                leftMeleeAction = 0

#Right hand

        dwx_r = (r_pose.position.x - environment.rightController.x) / deltaTime
        dy_r = (r_pose.position.y - environment.rightController.y) / deltaTime
        dwz_r = (r_pose.position.z - environment.rightController.z) / deltaTime
        dx_r = dwx_r * rx + dwz_r * rz
        dz_r = dwx_r * fx + dwz_r * fz
        d_melee_r = (dwx_r*dwx_r + dy_r*dy_r + dwz_r*dwz_r)
        speed_r = math.sqrt(d_melee_r)
        speed_xz_r = math.sqrt(dx_r*dx_r + dz_r*dz_r)
        is_r_horizontal = abs(r_pose.forward.y) < 0.5
        is_r_vertical =abs(r_pose.forward.y) > 0.7
        is_pure_z_r = abs(dz_r) > (abs(dx_r) + abs(dy_r)) * thrust_retract_purity
        rightMeleeAction = -1

        if self.useRight.enabled:
            self.useRight.update(currentTime, -environment.openVR.rightTouchPose.left.y, rightValidation)
        if self.useRightUp.enabled:
            self.useRightUp.update(currentTime, environment.openVR.rightTouchPose.left.y, rightValidation)

        if self.circleSkyRight.enabled:
            if d_melee_r > 2:
                self.circleSkyRight.update(currentTime, 0, rightValidation)
            elif not self.circleSkyRight.inGesture:
                if r_pose.forward.y < -0.9 and speed_xz_r > 1 and speed_xz_r > (abs(dy_r) * 1.5):
                    self.circleSkyRight.update(currentTime, -1.0, rightValidation)
                else:
                    self.circleSkyRight.update(currentTime, 0, rightValidation)
            else:
                self.circleSkyRight.update(currentTime, -1.0 if speed_r > 0.1 else 0, rightValidation)

        if self.circleFloorRight.enabled:
            if d_melee_r > 2:
                self.circleFloorRight.update(currentTime, 0, rightValidation)
            elif not self.circleFloorRight.inGesture:
                if r_pose.forward.y > 0.9 and speed_xz_r > 1 and speed_xz_r > (abs(dy_r) * 1.5):
                    self.circleFloorRight.update(currentTime, -1.0, rightValidation)
                else:
                    self.circleFloorRight.update(currentTime, 0, rightValidation)
            else:
                self.circleFloorRight.update(currentTime, -1.0 if speed_r > 0.1 else 0, rightValidation)

        if rightMeleeAction == -1:
            swipe_r_up_input = 0
            swipe_r_down_input = 0
            swipe_r_left_input = 0
            swipe_r_right_input = 0
            if speed_r > swipe_speed_threshold and is_r_horizontal:
                if abs(dy_r) > (abs(dx_r) + abs(dz_r)) * swipe_purity:
                    if dy_r > 0: swipe_r_up_input = -speed_r
                    else: swipe_r_down_input = -speed_r
                elif abs(dx_r) > (abs(dy_r) + abs(dz_r)) * swipe_purity:
                    if dx_r > 0: swipe_r_left_input = -speed_r
                    else: swipe_r_right_input = -speed_r
            self.swipeRightHandUp.update(currentTime, swipe_r_up_input, rightValidation)
            self.swipeRightHandDown.update(currentTime, swipe_r_down_input, rightValidation)
            self.swipeRightHandLeft.update(currentTime, swipe_r_left_input, rightValidation)
            self.swipeRightHandRight.update(currentTime, swipe_r_right_input, rightValidation)
            if (self.swipeRightHandUp.inGesture or self.swipeRightHandDown.inGesture or 
                self.swipeRightHandLeft.inGesture or self.swipeRightHandRight.inGesture):
                rightMeleeAction = 5

        if rightMeleeAction == -1:
            thrust_r_input = 0
            if d_melee_r > thrust_retract_min and dz_r < 0 and is_pure_z_r:
                thrust_r_input = -d_melee_r
            self.thrustRight.update(currentTime, thrust_r_input, rightValidation)
            if self.thrustRight.inGesture:
                rightMeleeAction = 6

        if rightMeleeAction == -1:
            retract_r_input = 0
            if d_melee_r > thrust_retract_min and dz_r > 0 and is_pure_z_r:
                retract_r_input = -d_melee_r
            self.retractRight.update(currentTime, retract_r_input, rightValidation)
            if self.retractRight.inGesture:
                rightMeleeAction = 7

        if rightMeleeAction == -1:
            shake_r_input = 0
            if abs(dz_r) < 0.5:
                if not self.shakeRight.inGesture:
                    if shake_min < speed_r < shake_max:
                        shake_r_input = -1.0
                else:
                    if speed_r > shake_maintain:
                        shake_r_input = -1.0
            self.shakeRight.update(currentTime, shake_r_input, rightValidation)
            if self.shakeRight.inGesture:
                rightMeleeAction = 4

        if rightMeleeAction == -1:
            melee_r_push_input = 0
            if r_pose.forward.y < self.rightMeleeAltThreshold:
                dot = dotProduct(r_pose.left, environment.openVR.headPose.forward)
                if self.meleeRightAltPush.enabled and dot < -0.5:
                    melee_r_push_input = -d_melee_r
            self.meleeRightAltPush.update(currentTime, melee_r_push_input, rightValidation)
            if self.meleeRightAltPush.inGesture:
                rightMeleeAction = 2

        if rightMeleeAction == -1:
            melee_r_pull_input = 0
            if r_pose.forward.y < self.rightMeleeAltThreshold:
                dot = dotProduct(r_pose.left, environment.openVR.headPose.forward)
                if self.meleeRightAltPull.enabled and dot > 0.5:
                    melee_r_pull_input = -d_melee_r
            self.meleeRightAltPull.update(currentTime, melee_r_pull_input, rightValidation)
            if self.meleeRightAltPull.inGesture:
                rightMeleeAction = 3

        if rightMeleeAction == -1:
            melee_r_alt_input = 0
            if r_pose.forward.y < self.rightMeleeAltThreshold:
                if self.meleeRightAlt.enabled:
                    melee_r_alt_input = -d_melee_r
            self.meleeRightAlt.update(currentTime, melee_r_alt_input, rightValidation)
            if self.meleeRightAlt.inGesture:
                rightMeleeAction = 1

        if rightMeleeAction == -1 and (item == None or item.trackMeleeRight) and self.meleeRight.enabled:
            melee_r_input = 0
            if not (is_pure_z_r or (is_r_vertical and abs(dy_r) <= 1.5)):
                melee_r_input = -d_melee_r
            self.meleeRight.update(currentTime, melee_r_input, rightValidation)
            if self.meleeRight.inGesture:
                rightMeleeAction = 0

        for gesture in self._locationBasedGesturesLeft:
            if gesture.enabled:
                gY = environment.openVR.headPose.position.y + gesture.offset.y
                gX = environment.openVR.headPose.position.x + environment.openVR.headPose.left.x * gesture.offset.x + environment.openVR.headPose.forward.x * gesture.offset.z
                gZ = environment.openVR.headPose.position.z + environment.openVR.headPose.left.z * gesture.offset.x + environment.openVR.headPose.forward.z * gesture.offset.z
                dx = l_pose.position.x - gX
                dy = l_pose.position.y - gY
                dz = l_pose.position.z - gZ
                d = dx*dx + dy*dy + dz*dz
                gesture.update(currentTime, d, leftValidation)        
           
        for gesture in self._locationBasedGesturesRight:
            if gesture.enabled:
                gY = environment.openVR.headPose.position.y + gesture.offset.y
                gX = environment.openVR.headPose.position.x + environment.openVR.headPose.left.x * gesture.offset.x + environment.openVR.headPose.forward.x * gesture.offset.z
                gZ = environment.openVR.headPose.position.z + environment.openVR.headPose.left.z * gesture.offset.x + environment.openVR.headPose.forward.z * gesture.offset.z
                dx = r_pose.position.x - gX
                dy = r_pose.position.y - gY
                dz = r_pose.position.z - gZ
                d = dx*dx + dy*dy + dz*dz
                gesture.update(currentTime, d, rightValidation)                 
        
        if self.triggerLeft.enabled:
            self.triggerLeft.update(currentTime, -environment.openVR.leftTrigger, leftValidation)
        if self.triggerRight.enabled:
            if item == None or item.trackFireWeapon:
                self.triggerRight.update(currentTime, -environment.openVR.rightTrigger, rightValidation)
            else:
                self.triggerRight.update(currentTime, 0, rightValidation)
        if self.gripLeft.enabled:
            self.gripLeft.update(currentTime, -environment.openVR.leftGrip, leftValidation)
        if self.gripRight.enabled:
            self.gripRight.update(currentTime, -environment.openVR.rightGrip, rightValidation)