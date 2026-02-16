# --- 1. 初始化模式 ---
FlyMode = Mode()

# --- 2. 自定义飞行俯仰控制动作 ---
class FlightPitchControl(Action):
    def __init__(self, mode):
        Action.__init__(self)
        self._mode = mode

    def update(self, *args):
        if self._mode.current == 1:
            # 0.26 弧度 ≈ 15度
            headY = environment.openVR.headPose.forward.y
            
            # --- 修正：反转升降逻辑 ---
            # 抬头 (> 15度) -> 触发 Ctrl (下降)
            if headY > 0.26: 
                keyboard.setKeyDown(Key.LeftControl) # 下降
                keyboard.setKeyUp(Key.Space)
            
            # 低头 (< -15度) -> 触发 Space (上升)
            elif headY < -0.26: 
                keyboard.setKeyDown(Key.Space)       # 上升
                keyboard.setKeyUp(Key.LeftControl)
            
            # 死区 -> 保持高度
            else: 
                keyboard.setKeyUp(Key.Space)
                keyboard.setKeyUp(Key.LeftControl)

    def leave(self, *args):
        keyboard.setKeyUp(Key.Space)
        keyboard.setKeyUp(Key.LeftControl)

# --- 3. 骑扫帚手势定义 ---
crotchLeft = gestureTracker.addLocationBasedGesture(True, 0.05, 0.05, Vector(0, -0.7, -0))
crotchLeft.enabled = True
crotchLeft.touchValidating = Touch_Validating_Left
crotchLeft.haptics.touchEnter = Touch_Enter_Left

crotchRight = gestureTracker.addLocationBasedGesture(False, 0.05, 0.05, Vector(0, -0.7, -0))
crotchRight.enabled = True
crotchRight.touchValidating = Touch_Validating_Right
crotchRight.haptics.touchEnter = Touch_Enter_Right

# --- 4. 绑定动作 ---
# 左手：切换模式 + 按Tab拿出扫帚 + 激活俯仰控制(传入FlyMode)
crotchLeft.gripAction = MultiAction([
    ModeSwitchWithReset(FlyMode, 1, 0),
    KeyPress(Key.Tab),      
    FlightPitchControl(FlyMode) 
])

# 巡航加速
crotchLeft.triggerAction = ModeBasedAction(FlyMode, {1:  MultiAction([KeyQuickPress(Key.D3), ResetAction()])})
crotchRight.gripAction = ModeBasedAction(FlyMode, {1: KeyPress(Key.W)})
crotchRight.triggerAction = ModeBasedAction(FlyMode, {1: MousePress(0)})

#手柄鼠标
RtriggerMode = Mode()
RgripMode = Mode()

gestureTracker.gripRight.enabled = True
gestureTracker.gripRight.action =  MultiAction([ModeSwitchWithReset(RgripMode, 1, 0), ModeSwitchWithReset(vrToMouse.mode, 3, 0)])
vrToMouse.mode.current = 0
vrToMouse.mouseSensitivityX = 1500
vrToMouse.mouseSensitivityY = 1500

#咒语组/荧光闪烁
gestureTracker.triggerRight.enabled  = True
gestureTracker.triggerRight.action = MultiAction([ModeSwitchWithReset(RtriggerMode, 1, 0), ModeBasedAction(RgripMode, {1: MousePress(0)}, KeyPress(Key.Period))])

# 左手左劃：大招组
gestureTracker.swipeLeftHandLeft.enabled = True
gestureTracker.swipeLeftHandLeft.triggerAction = ModeBasedAction(RtriggerMode, {1: KeyQuickPress(Key.D8)}, KeyQuickPress(Key.D1))
gestureTracker.swipeLeftHandLeft.haptics.touchEnter =  Touch_Melee_Left

# 左手左划：生活组
gestureTracker.swipeLeftHandRight.enabled = True
gestureTracker.swipeLeftHandRight.triggerAction = ModeBasedAction(RtriggerMode, {1: KeyQuickPress(Key.D6)})


# 左手上劃：戰鬥一組 (KeyPress 5) - 短震 1 下
gestureTracker.swipeLeftHandUp.enabled = True
gestureTracker.swipeLeftHandUp.triggerAction = ModeBasedAction(RtriggerMode, {1: KeyQuickPress(Key.D5)})
gestureTracker.swipeLeftHandUp.haptics.touchEnter =  Touch_Enter_Left


# 左手下劃：戰鬥二組 (KeyPress 7) - 短震 2 下
gestureTracker.swipeLeftHandDown.enabled = True
gestureTracker.swipeLeftHandDown.triggerAction = ModeBasedAction(RtriggerMode, {1: KeyQuickPress(Key.D7)})
gestureTracker.swipeLeftHandDown.haptics.touchEnter = Touch_DoublePulse_Left

#有求必应屋转动物品/缩放地图
LtriggerMode = Mode()
gestureTracker.triggerLeft.enabled = True
gestureTracker.triggerLeft.action = MultiAction([ModeSwitchWithReset(LtriggerMode, 1, 0), KeyPress(Key.Comma)])

gestureTracker.swipeRightHandLeft.enabled = True
gestureTracker.swipeRightHandLeft.action = ModeBasedAction(LtriggerMode, {1: KeyPress(Key.R)})

gestureTracker.swipeRightHandRight.enabled = True
gestureTracker.swipeRightHandRight.action = ModeBasedAction(LtriggerMode, {1: KeyPress(Key.T)})

#喝药
gestureTracker.lightRight.enabled = True
gestureTracker.lightRight.gripAction = KeyPress(Key.G)

#互动/收集
gestureTracker.shoulderInventoryLeft.enabled = True
gestureTracker.shoulderInventoryLeft.gripAction = KeyPress(Key.F)

#格挡
gestureTracker.foreheadLeft.enabled = True
gestureTracker.foreheadLeft.action =KeyPress(Key.Q)
gestureTracker.foreheadLeft.haptics.touchEnter =  Touch_Enter_Left

#闪避
gestureTracker.duck.enabled = True
gestureTracker.duck.action = KeyPress(Key.LeftControl)

gestureTracker.leanLeft.enabled = True
gestureTracker.leanLeft.action = KeyPress(Key.A)

gestureTracker.leanRight.enabled = True
gestureTracker.leanRight.action = KeyPress(Key.D)

#飞来术
gestureTracker.meleeLeftAltPull.enabled = True
gestureTracker.meleeLeftAltPull.triggerAction = KeyPress(Key.D4)

#统统飞走
gestureTracker.meleeLeftAltPush.enabled = True
gestureTracker.meleeLeftAltPush.triggerAction = KeyPress(Key.D2)

#荧光术、火焰术、冰霜术
gestureTracker.thrustRight.enabled = True
gestureTracker.thrustRight.triggerAction =KeyQuickPress(Key.D3)
gestureTracker.upperAreaRight.enabled = True
gestureTracker.upperAreaRight.triggerAction = KeyQuickPress(Key.D3)

#基础施法
gestureTracker.meleeRight.enabled = True
gestureTracker.meleeRight.action = MouseQuickPress(0)

#四分五裂、隐身术，左手横切数字1，整合在切换组里

#钻心咒Crucio
CrucioMode = Mode()

gestureTracker.shakeLeft.enabled = True
gestureTracker.shakeLeft.gripAction =  ModeSwitchWithReset(CrucioMode, 1, 0)

gestureTracker.shakeRight.enabled = True
gestureTracker.shakeRight.gripAction = ModeBasedAction(CrucioMode, {1: MultiAction([KeyQuickPress(Key.D8), KeyQuickPress(Key.D2)])})

# 魂魄出窍 Imperio
ImperioMode = Mode()
gestureTracker.useRight.enabled = True
gestureTracker.useRight.action = ModeSwitchWithReset(ImperioMode, 1, 0)
gestureTracker.useRight.haptics.touchEnter = Touch_Enter_Right

gestureTracker.retractRight.enabled = True
gestureTracker.retractRight.gripAction = ModeBasedAction(ImperioMode, {1: MultiAction([KeyQuickPress(Key.D8),KeyQuickPress(Key.D4)])})

# 3. 阿瓦达索命 Avada Kedavra
AvadaMode = Mode() 
gestureTracker.retractLeft.enabled = True
gestureTracker.retractLeft.gripAction = ModeSwitchWithReset(AvadaMode, 1, 0)

gestureTracker.thrustRight.enabled = True
gestureTracker.thrustRight.gripAction = ModeBasedAction(AvadaMode,  {1: MultiAction([KeyQuickPress(Key.D8),KeyQuickPress(Key.D1)])})


#古代魔法
AncientMode = Mode() 
gestureTracker.lowerAreaLeft.enabled = True
gestureTracker.lowerAreaLeft.action = ModeSwitchWithReset(AncientMode, 1, 0)
gestureTracker.meleeLeft.enabled = True
gestureTracker.meleeLeft.gripAction =  ModeBasedAction(AncientMode,  {1: KeyPress(Key.X)})

#古代魔法投掷
gestureTracker.meleeLeftAltPull.enabled = True
gestureTracker.meleeLeftAltPull.gripAction = KeyPress(Key.Z)

#原形立现
gestureTracker.circleSkyRight.enabled = True
gestureTracker.circleSkyRight.triggerAction = KeyPress(Key.R)

#指路
gestureTracker.circleFloorRight.enabled = True
gestureTracker.circleFloorRight.triggerAction = KeyPress(Key.V)

#菜单
gestureTracker.buttonRightStick.enabled = True
gestureTracker.buttonRightStick.action = KeyPress(Key.P)

#背包物品
gestureTracker.shoulderWeaponRight.enabled = True
gestureTracker.shoulderWeaponRight.gripAction = KeyPress(Key.Tab)

#野兽管理
gestureTracker.useRightUp.enabled = True
gestureTracker.useRightUp.gripAction = KeyPress(Key.H)
gestureTracker.useRightUp.haptics.touchEnter = Touch_Enter_Right

#重置高度
gestureTracker.aimPistol.enabled = True
gestureTracker.aimPistol.action = ResetAction()

#bhaptics
#gestureTracker = gestureSets.defaultGestureSet
gestureTracker.triggerRight.haptics.enter = None
gestureTracker.triggerRight.haptics.hold = None
gestureTracker.meleeLeft.validationMode = 3
gestureTracker.meleeLeft.haptics.enter =  "SoulTrapCaptured_1"
gestureTracker.retractLeft.haptics.enter =  "HealthPenUse_1"
gestureTracker.thrustRight.haptics.enter =  "Laser"
gestureTracker.meleeRight.haptics.enter =  "MinigunVest_R"
gestureTracker.shakeRight.haptics.enter = "GrabbedByBarnacle_1"
gestureTracker.swipeLeftHandLeft.validationMode = 2
gestureTracker.swipeLeftHandLeft.haptics.enter = "RecoilMeleeVest_L"
gestureTracker.shoulderInventoryLeft.validationMode = 3
gestureTracker.shoulderInventoryLeft.haptics.enter  = "BackpackStoreClipLeft_1"
gestureTracker.retractRight.validationMode = 3
gestureTracker.retractRight.haptics.enter =  "Healing_1"
gestureTracker.shoulderWeaponRight.haptics.enter  = "BackpackRetrieveClipRight_1"
gestureTracker.lightRight.haptics.enter  = "PotionDrinking_1"

gestureTracker.circleSkyRight.haptics.enter =  "HeartBeat_1"
gestureTracker.circleFloorRight.haptics.enter =  "SwimVest20_1"