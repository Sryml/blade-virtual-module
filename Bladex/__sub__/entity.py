from __future__ import annotations

import typing

# import Bladex
from . import b_object, inventory
from .b_types import *

# Entity.init_entity_properties

__RasterMode = Literal[
    "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
]


class B_Entity:
    def __init__(self) -> None:
        self.Actor: Bool
        self.AngVel: float
        self.Arrow: Bool
        self.AttackList: Optional[list]
        self.__CanUse: Bool
        self.ContinuousDamage: int
        self.DamageFunc: Optional[Callable]
        self.Data: Any = None
        self.FrameFunc: Optional[Callable] = None
        self.GlowSizeDist: int
        self.GlowTestZ: Bool
        self.HearFunc: Optional[Callable]
        self.HitFunc: Optional[Callable]
        self.HitShieldFunc: Optional[Callable]
        self.__InAttack: Bool
        self.__InDestructorAttack: Bool
        self.__InWorld: Bool
        self.InflictHitFunc: Optional[Callable]
        self.Intensity: float
        self.InternalState: Unknown
        self.__Kind: str
        self.Mass: float
        self.__Material: Unknown
        self.__Name: str
        self.__Object: Unknown
        self.__Parent: str
        self.Person: Bool
        self.__Physic: Bool
        self.Position: Vector3
        self.Precission: float
        self.Reflects: int
        self.SeeFunc: Optional[Callable]
        self.SendSectorMsgs: Bool
        self.SendTriggerSectorMsgs: Bool
        self.SizeFactor: float
        self.Static: Bool
        self.StaticWeaponMode: int
        self.StickFunc: Optional[Callable]
        self.__SubscribedLists: List[str]
        self.TimerFunc: Optional[Callable]
        self.TrailMode: int
        self.UseFunc: Optional[Callable]
        self.Weapon: Bool
        self.WeaponMode: int

    # @property
    # def AngVel(self):
    #     """*read only*"""
    #     return self.__AngVel

    @property
    def CanUse(self):
        """*read only*"""
        return self.__CanUse

    @property
    def InAttack(self):
        """*read only*"""
        return self.__InAttack

    @property
    def InDestructorAttack(self):
        """*read only*"""
        return self.__InDestructorAttack

    @property
    def InWorld(self):
        """*read only*"""
        return self.__InWorld

    # @property
    # def Intensity(self):
    #     """*read only*"""
    #     return self.__Intensity

    # @property
    # def InternalState(self):
    #     """*read only*"""
    #     return self.__InternalState

    @property
    def Kind(self):
        """*read only*"""
        return self.__Kind

    @property
    def Material(self):
        """*read only*"""
        return self.__Material

    @property
    def Name(self):
        """Modifying this variable is not recommended."""
        return self.__Name

    @Name.setter
    def Name(self, value: str):
        self.__Name = value

    @property
    def Object(self):
        """*read only*"""
        return self.__Object

    @property
    def Parent(self):
        """*read only*"""
        return self.__Parent

    @property
    def Physic(self):
        """*read only*"""
        return self.__Physic

    # @property
    # def Precission(self):
    #     """*read only*"""
    #     return self.__Precission

    # @property
    # def SizeFactor(self):
    #     """*read only*"""
    #     return self.__SizeFactor

    @property
    def SubscribedLists(self):
        """*read only*"""
        return self.__SubscribedLists

    # Methods
    def Abs2RelPoint(
        self,
        x: float,
        y: float,
        z: float,
        node_name: Union[NodeType, str_, NULL] = NULL(0),
    ) -> Vector3:
        ...

    @overload
    def Abs2RelVector(self, entity: B_PyEntity) -> Vector3:
        ...

    @overload
    def Abs2RelVector(
        self,
        x: float,
        y: float,
        z: float,
        node_name: Union[NodeType, str_, NULL] = NULL(0),
    ) -> Vector3:
        ...

    def Abs2RelVector(self, *args: Any, **kwargs: Any) -> Vector3:
        ...

    def AddAnimSound(
        self, animation: str, sound: b_object.B_PySound, time: float
    ) -> Bool:
        ...

    def AddAnmEventFunc(self, anm_event: str, func: Callable[[str, str], Any]) -> Bool:
        ...

    def AddCameraEvent(self, frame: int, func: Callable[[str, int], Any]) -> Bool:
        ...

    def AddCameraNode(
        self, node: int, time: float, x: float, y: float, z: float
    ) -> Bool:
        ...

    def AddEventSound(self, event_name: str, sound: b_object.B_PySound) -> Bool:
        ...

    def AddPathNode(self, time: float, x: float, y: float, z: float) -> Bool:
        ...

    def AddWatchAnim(self, anm_name: str) -> Bool:
        ...

    def CameraClearPath(self, node: int) -> Bool:
        ...

    def CameraStartPath(self, node: int) -> Bool:
        ...

    def CanGoTo(self, x: float, y: float, z: float) -> Bool:
        ...

    def CanISee(self, entity: B_PyEntity) -> Bool:
        ...

    def CanISeeFrom(self, entity: B_PyEntity, x: float, y: float, z: float) -> Bool:
        ...

    def CatchOnFire(self, x: float, y: float, z: float) -> Bool:
        ...

    def Chase(self, enemy: B_PyEntity, action_area: Int) -> Bool:
        ...

    def CheckAnimCol(self, anm_name: str, obj: B_PyEntity, unknown: int) -> int:
        ...

    def ClearAnmEventFuncs(self) -> Bool:
        ...

    def ClearPath(self) -> Bool:
        ...

    def Cut(self) -> Bool:
        ...

    def DelAnmEventFunc(self, anm_event: str) -> Bool:
        ...

    def DoAction(self, action_name: str) -> int:
        ...

    def DoActionWI(
        self,
        action_name: str,
        interpolation_type: Literal[0, 1, 2, 3, 4, 5],
        tran_time: float,
        start_timeline: float = 0.0,
    ) -> int:
        """
        InterpWithOff = 0\n
        InterpWithOutOff = 1\n
        InertialIntrp = 2\n
        FixedRFootIntep = 3\n
        FixedLFootIntep = 4\n
        FixedFootAutoInterp = 5
        """
        ...

    def ExcludeHitFor(self, entity: B_PyEntity) -> Bool:
        ...

    def ExcludeHitInAnimationFor(self, entity: B_PyEntity) -> Bool:
        ...

    def Face(self, angle: float) -> Bool:
        ...

    def Fly(self, velocity_x: float, velocity_y: float, velocity_z: float) -> Bool:
        ...

    def Freeze(self) -> Bool:
        ...

    def GetActionMode(self) -> int:
        ...

    def GetChild(self, index: int) -> str:
        ...

    def GetCombatants(self) -> List:
        ...

    def GetDummyAxis(
        self,
        anchor_name: str,
        axis_x: float,
        axis_y: float,
        axis_z: float,
        ref: Bool = 1,
    ) -> Vector3:
        """
        :ref:
            1 - World coordinate\n
            0 - Entity's own coordinate
        """
        ...

    def GetEnemyName(self) -> str:
        ...

    def GetGroupMembers(self) -> Union[List, Literal[0]]:
        ...

    def GetInventory(self) -> inventory.B_PyInventory:
        ...

    def GetInventoryEntity(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetInventorySelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetNChildren(self) -> int:
        ...

    def GetNodeIndex(self, node_name: str) -> int:
        ...

    def GetParticleEntity(self) -> B_Entity_Particle:
        ...

    def GetWoundedZone(self, zone: int) -> Bool:
        ...

    def GoTo(self, x: float, y: float, z: float) -> Bool:
        ...

    def GoToPath(self, i_unknown: int, f_unknown: float) -> Bool:
        ...

    def GotAnmType(self, anm_name: str) -> Bool:
        ...

    def GraspPos(self, anchor_name: str) -> Vector3:
        ...

    def Impulse(self, x: float, y: float, z: float) -> Bool:
        ...

    def ImpulseC(
        self, x: float, y: float, z: float, dx: float, dy: float, dz: float
    ) -> int:
        ...

    def InsideActionArea(self, action_area: int) -> Bool:
        ...

    def InterruptCombat(self) -> Bool:
        ...

    def IsValid(self) -> Bool:
        ...

    def LaunchAnimation(self, anm_name: str) -> Bool:
        ...

    def LaunchAnimation2(self, anm_name1: str, anm_name2: str) -> Bool:
        ...

    def LaunchAnmType(self, anm_type: str, index: int = 0) -> Bool:
        ...

    def LaunchBayRoute(self) -> Bool:
        ...

    def LaunchWatch(self) -> Bool:
        ...

    def Link(self, child: B_PyEntity) -> Bool:
        ...

    def LinkAnchors(
        self, entity_anchor: str, child: B_PyEntity, child_anchor: str
    ) -> Bool:
        ...

    def LinkToNode(self, child: B_PyEntity, node: int) -> Bool:
        ...

    @overload
    def LookAt(self, obj_name: str) -> Bool:
        ...

    @overload
    def LookAt(self, x: float, y: float, z: float) -> Bool:
        ...

    def LookAt(self, *args: Any, **kwargs: Any) -> Bool:
        ...

    def LookAtEntity(self, ent_name: str) -> Bool:
        ...

    def LookAtPerson(self, person_name: str) -> Bool:
        ...

    @overload
    def MessageEvent(
        self,
        message_type: Literal[0x7, 0x8, 0xD, 0xE, 0xF],
        unknown1: Literal[0],
        unknown2: Literal[0],
    ) -> int:
        ...

    @overload
    def MessageEvent(self, message_type: int, unknown1: int, unknown2: int) -> int:
        ...

    def MessageEvent(self, message_type: int, unknown1: int, unknown2: int) -> int:
        """
        :message_type:
            MESSAGE_START_WEAPON = 7\n
            MESSAGE_STOP_WEAPON = 8\n
            MESSAGE_SETSTATICWEPONMODE = 13\n
            MESSAGE_START_TRAIL = 14\n
            MESSAGE_STOP_TRAIL = 15
        """
        ...

    def Move(self, x: float, y: float, z: float, unknown: int = 1) -> Bool:
        ...

    def PlaySound(self, cycles: int = -1) -> Bool:
        ...

    def PutToWorld(self) -> Bool:
        ...

    def QuickFace(self, angle: float) -> Bool:
        ...

    @overload
    def RaiseEvent(self, event_name: Literal["Interrupt"]) -> int:
        ...

    @overload
    def RaiseEvent(self, event_name: str) -> int:
        ...

    def RaiseEvent(self, event_name: str) -> int:
        ...

    def Rel2AbsPoint(
        self,
        x: float,
        y: float,
        z: float,
        node_name: Union[NodeType, str_, NULL] = NULL(0),
    ) -> Vector3:
        ...

    @overload
    def Rel2AbsVector(self, entity: B_PyEntity) -> Vector3:
        ...

    @overload
    def Rel2AbsVector(
        self,
        x: float,
        y: float,
        z: float,
        node_name: Union[NodeType, str_, NULL] = NULL(0),
    ) -> Vector3:
        ...

    def Rel2AbsVector(self, *args: Any, **kwargs: Any) -> Vector3:
        ...

    def RemoveCameraEvent(self, frame: int) -> Bool:
        ...

    def RemoveFromInvent(self, obj_name: str) -> Bool:
        ...

    def RemoveFromInventLeft(self) -> Bool:
        ...

    def RemoveFromInventLeft2(self) -> Bool:
        ...

    def RemoveFromInventRight(self) -> Bool:
        ...

    def RemoveFromList(self, timer_name: str) -> Bool:
        ...

    def RemoveFromWorld(self) -> Literal[1]:
        ...

    def RemoveFromWorldWithChilds(self) -> Literal[1]:
        ...

    def ResetChase(self) -> Bool:
        ...

    def ResetWounds(self) -> Bool:
        ...

    def Rotate(
        self,
        axis_x: float,
        axis_y: float,
        axis_z: float,
        angle: float,
        unknown: int = 1,
    ) -> Bool:
        ...

    def RotateAbs(
        self,
        x: float,
        y: float,
        z: float,
        axis_x: float,
        axis_y: float,
        axis_z: float,
        angle: float,
        unknown: int = 1,
    ) -> Bool:
        ...

    def RotateRel(
        self,
        x: float,
        y: float,
        z: float,
        axis_x: float,
        axis_y: float,
        axis_z: float,
        angle: float,
        unknown: int = 1,
    ) -> Bool:
        ...

    def SQDistance2(self, entity: B_PyEntity) -> float:
        ...

    def SetActiveEnemy(self, entity: B_PyEntity) -> Bool:
        ...

    def SetAnmFlags(
        self,
        anm_name: str,
        wuea: Literal[0, 1, 2],
        mod_y: Bool,
        solf: Bool,
        copy_rot: Bool,
        bng_mov: Literal[0, 1, 2, 3, 4, 5],
        headf: Literal[0, 1, 2, 3],
    ) -> Bool:
        """
        :bng_mov:
            BM_IDC = 0\n
            BM_NONE = 1\n
            BM_XYZ = 2\n
            BM_XZ = 3\n
            BM_2ANM = 4\n
            BM_SCRIPT = 5
        :headf:
            HEADF_ENG = 0\n
            HEADF_ANM = 1\n
            HEADF_ANM2SEE = 2\n
            HEADF_ANM2ENG = 3
        """
        ...

    def SetAuraActive(self, is_active: int) -> Bool:
        ...

    def SetAuraGradient(
        self,
        gap: int,
        r1: float,
        g1: float,
        b1: float,
        alpha1: float,
        starting_point: float,
        r2: float,
        g2: float,
        b2: float,
        alpha2: float,
        ending_point: float,
    ) -> Bool:
        ...

    def SetAuraParams(
        self,
        size: float,
        alpha: float,
        color_intensity: float,
        hide_front_faces: int,
        hide_back_faces: int,
        alpha_mode: int,
    ) -> Bool:
        ...

    def SetCameraEndTangentNode(
        self, node: int, node_index: int, tang_x: float, tang_y: float, tang_z: float
    ) -> Bool:
        ...

    def SetCameraStartTangentNode(
        self, node: int, node_index: int, tang_x: float, tang_y: float, tang_z: float
    ) -> Bool:
        ...

    def SetEnemy(self, enemy: B_PyEntity) -> Bool:
        ...

    def SetMaxCamera(self, cam_file_name: str, start: int, end: int) -> Bool:
        ...

    def SetMesh(self, mesh_name: str) -> Bool:
        ...

    def SetNextAttack(self, attack: str) -> int:
        ...

    def SetNodeEndTangent(
        self, unknown1: int, unknown2: float, unknown3: float, unknown4: float
    ) -> Bool:
        ...

    def SetNodeStartTangent(
        self, unknown1: int, unknown2: float, unknown3: float, unknown4: float
    ) -> Bool:
        ...

    def SetObjectSound(self, sound_name: str) -> Bool:
        ...

    def SetOnFloor(self) -> int:
        ...

    def SetOrientation(
        self, w: float, x: float, y: float, z: float, unknown: int = 1
    ) -> Bool:
        ...

    def SetPersonView(self, person_name: str) -> Bool:
        ...

    def SetPosition(self, x: float, y: float, z: float, unknown: int = 1) -> Bool:
        ...

    def SetSound(self, file_name: str) -> Bool:
        ...

    def SetTmpAnmFlags(
        self,
        wuea: Literal[0, 1, 2],
        mod_y: Bool,
        solf: Bool,
        copy_rot: Bool,
        bng_mov: Literal[0, 1, 2, 3, 4, 5],
        headf: Literal[0, 1, 2, 3],
        unknown: Bool = 1,
    ) -> Bool:
        """
        :bng_mov:
            BM_IDC = 0\n
            BM_NONE = 1\n
            BM_XYZ = 2\n
            BM_XZ = 3\n
            BM_2ANM = 4\n
            BM_SCRIPT = 5
        :headf:
            HEADF_ENG = 0\n
            HEADF_ANM = 1\n
            HEADF_ANM2SEE = 2\n
            HEADF_ANM2ENG = 3
        """
        ...

    def SetTravellingView(self, s_type: int, t_type: int) -> Bool:
        ...

    def SetWoundedZone(self, zone: int, is_active: int) -> Bool:
        ...

    def SeverLimb(self, limb: int) -> B_Entity_Weapon:
        ...

    def SlideTo(
        self, final_displacement: float, initial_velocity: float, acceleration: float
    ) -> Bool:
        ...

    def StartGrabbing(self) -> Bool:
        ...

    def StartLooking(self, x: float, y: float, z: float) -> Bool:
        ...

    def StartPath(self, node: int) -> Bool:
        ...

    def Stop(self) -> Bool:
        ...

    def StopGrabbing(self) -> Bool:
        ...

    def StopLooking(self) -> Bool:
        ...

    def StopSound(self) -> Bool:
        ...

    @overload
    def SubscribeToList(
        self, name: Literal["Pin", "Listeners", "Timer60", "Timer30", "Timer15"]
    ) -> Bool:
        ...

    @overload
    def SubscribeToList(self, name: str) -> Bool:
        ...

    def SubscribeToList(self, name: str) -> Bool:
        ...

    def SwitchTo1H(self) -> Bool:
        ...

    def SwitchToBow(self) -> Bool:
        ...

    def TestPos(
        self, x: float, y: float, z: float, action_area: int, max_fall: float
    ) -> int:
        ...

    def TestPosInOwnBox(
        self, x: float, y: float, z: float, box_size: float = 1.0
    ) -> int:
        ...

    def TurnOff(self) -> Bool:
        ...

    def TurnOn(self) -> Bool:
        ...

    def UnFreeze(self) -> Bool:
        ...

    def Unlink(self, child: B_PyEntity) -> Bool:
        ...

    def UnlinkChildren(self) -> Bool:
        ...

    def Use(self) -> Bool:
        ...


class B_Entity_(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.CastShadows: Bool
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.__FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.Orientation: Quaternion
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.__nFires: int
        self.__nLights: int

    @property
    def FireParticleType(self):
        """*read only*"""
        return self.__FireParticleType

    @property
    def LightColor(self):
        """*read only*"""
        return self.__LightColor

    @property
    def LightGlow(self):
        """*read only*"""
        return self.__LightGlow

    @property
    def LightIntensity(self):
        """*read only*"""
        return self.__LightIntensity

    @property
    def LightPrecission(self):
        """*read only*"""
        return self.__LightPrecission

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def nFires(self):
        """*read only*"""
        return self.__nFires

    @property
    def nLights(self):
        """*read only*"""
        return self.__nLights


class B_Entity_Actor(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.Animation: str
        self.CastShadows: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.__FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.Frame: int
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.OnAnimationEndFunc: Optional[Callable[[str], Any]]
        self.OnPathNodeFunc: Optional[Callable[[str, int], Any]]
        self.Orientation: Quaternion
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.__nFires: int
        self.__nLights: int

    @property
    def FireParticleType(self):
        """*read only*"""
        return self.__FireParticleType

    @property
    def LightColor(self):
        """*read only*"""
        return self.__LightColor

    @property
    def LightGlow(self):
        """*read only*"""
        return self.__LightGlow

    @property
    def LightIntensity(self):
        """*read only*"""
        return self.__LightIntensity

    @property
    def LightPrecission(self):
        """*read only*"""
        return self.__LightPrecission

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def nFires(self):
        """*read only*"""
        return self.__nFires

    @property
    def nLights(self):
        """*read only*"""
        return self.__nLights


class B_Entity_Aura(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Scale: float


class B_Entity_Camera(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.ChangeNodeFunc: Union[Callable[[str, int, int], Any], Literal[""]]
        self.Dist: float
        self.ESource: str
        self.ETarget: str
        self.EarthQuake: Bool
        self.EarthQuakeFactor: float
        self.PViewType: Literal[0, 1, 2, 3]
        self.Returns: Unknown
        self.SType: Literal[0, 1, 2]
        self.Scale: float
        self.TAng: Vector3
        self.TPos: Vector3
        self.TType: Literal[0, 1, 2, 3]


class B_Entity_ElectricBolt(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Active: Bool
        self.CoreGlowColor: RGBColor
        self.Damage: Bool
        self.ETarget: str
        self.FixedTarget: Bool
        self.InnerGlowColor: RGBColor
        self.MaxAmplitude: float
        self.MinSectorLength: float
        self.OuterGlowColor: RGBColor
        self.Scale: float
        self.SimpleSections: Bool
        self.Target: Vector3


class B_Entity_Fire(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.__FireParticleType: Optional[str] = None
        self.Scale: float

    @property
    def FireParticleType(self):
        """*read only*"""
        return self.__FireParticleType


class B_Entity_Lava(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Scale: float
        self.SelfLight: Bool
        self.TextureName: str
        self.TouchFluidFunc: Optional[Callable[[str, str, float], Any]]
        self.Zoom: float


class B_Entity_Magic_Missile(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.CastShadows: Bool
        self.Color: RGBColor
        self.Damage: Bool
        self.DamageRadius: float
        self.ETarget: str
        self.Flick: Bool
        self.Intensity2: Unknown
        self.OnHitFunc: Optional[Callable[[str, str], Any]]
        self.Scale: float
        self.Velocity: Vector3
        self.Visible: Bool


class B_Entity_Particle(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.DeathTime: float
        self.Friction: float
        self.Friction2: float
        self.Gravity: Vector3
        self.ObjCTest: Bool
        self.PartialLevel: Unknown
        self.Scale: float
        self.Velocity: Vector3


class B_Entity_Particle_System(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.D: Vector3
        self.D1: Vector3
        self.D2: Vector3
        self.DeathTime: float
        self.FollowFactor: float
        self.Friction: float
        self.Friction2: float
        self.NormalVelocity: Int
        self.ObjectName: str
        self.PPS: int
        self.ParticleType: Union[str_, ParticleType]
        self.PersonName: str
        self.PersonNodeName: Union[str_, NodeType]
        self.RandomVelocity: Int
        self.RandomVelocity_V: Int
        self.Scale: float
        self.Time2Live: int
        self.Time2Live_V: int
        self.Velocity: Vector3
        self.YGravity: Int


class B_Entity_Person(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Accuracy: float
        self.ActionAreaMax: Int
        self.ActionAreaMin: Int
        self.__ActiveEnemy: str
        self.AddBayPoint: Vector3
        self.Aim: Bool
        self.AimOffTarget: Radian
        self.__AimVector: Vector3
        self.Alpha: float
        self.Angle: Radian
        self.__AnimFullName: str
        self.__AnimName: str
        self.AnmEndedFunc: Optional[Callable[[str], Any]]
        self.__AnmPos: float
        self.AnmTranFunc: Optional[Callable[[str], Any]]
        self.__AstarState: Literal[0, 1, 2, 3]
        self.Attack: Bool
        self.AttackFunc: Optional[Callable[[str, str], Any]]
        self.__BayRoute: Bool
        self.BigFallFunc: Optional[Callable[[str, float], Any]]
        self.Blind: Bool
        self.Block: Bool
        self.BlockingPropensity: float
        self.CastShadows: Bool
        self.CharSeeingEnemyFunc: Optional[Callable[[str, str], Any]]
        self.__CharType: str
        self.__CharTypeExt: str
        self.CombatDistFlag: Bool
        self.CombatGroup: str
        self.ContinuousBlock: Bool
        self.__CurrentAreas: Unknown
        self.Deaf: Bool
        self.__DefenceNeeded: Bool
        self.DelayNoSeenFunc: Optional[Callable[[str], Any]]
        self.__Dist2Floor: float
        self.EnemyDeadFunc: Optional[Callable[[str], Any]]
        self.__EnemyLastSeen: Vector3
        self.EnemyNoAllowedAreaFunc: Optional[Callable[[str], Any]]
        self.Energy: float
        self.EnterCloseFunc: Optional[Callable[[str], Any]]
        self.EnterLargeFunc: Optional[Callable[[str], Any]]
        self.EnterPrimaryAAFunc: Optional[Callable[[str], Any]]
        self.EnterSecondaryAAFunc: Optional[Callable[[str], Any]]
        self.Frozen: Bool
        self.GoToJogging: Bool
        self.GoToSneaking: Bool
        self.Gob: Bool
        self.Gof: Bool
        self.Heard: Bool
        self.ImDeadFunc: Optional[Callable[[str], Any]]
        self.ImHurtFunc: Optional[Callable[[str], Any]]
        self.__InCombat: Bool
        self.InitPos: Vector3
        self.__InvLeft: str
        self.__InvLeft2: str
        self.__InvLeftBack: str
        self.__InvRight: str
        self.__InvRightBack: str
        self.InvertedRoute: Bool
        self.LastAttackTime: float
        self.__LastSound: str
        self.__LastSoundPosition: Vector3
        self.LastTimeSeen: float
        self.Level: Int
        self.Life: Int
        self.__MeleeActive: Bool
        self.MeshName: str
        self.MutilateFunc: Optional[
            Callable[[str, str, float, float, float, float, float, float, int], Any]
        ]
        self.__MutilationsMask: int
        self.NewComboFunc: Optional[Callable[[str, str], Any]]
        self.NoAllowedAreaFunc: Optional[Callable[[str], Any]]
        self.__OnFloor: bool
        self.OnHitFunc: Optional[Callable[[str, str], Any]]
        self.OnStepFunc: Optional[Callable[[str], Any]]
        self.Orientation: Quaternion
        self.PartialLevel: Int
        self.__PrevAnimName: str
        self.RAttackMax: Int
        self.RAttackMin: Int
        self.__RangeActive: Bool
        self.RangeDefenceCapable: Bool
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Returns: Unknown
        self.RouteEndedFunc: Optional[Callable[[str], Any]]
        self.__RouteType: int
        self.Run: Bool
        self.Scale: float
        self.Seen: Bool
        self.SelfIlum: float
        self.Sneak: Bool
        self.TakeFunc: Optional[Callable[[str], Any]]
        self.Texture: Unknown
        self.ThrowFunc: Optional[Callable[[str], Any]]
        self.Tl: Bool
        self.ToggleCombatFunc: Optional[Callable[[str], Any]]
        self.Tr: Bool
        self.__Will1aaTo2aa: Bool
        self.__WillCrashInFloor: Bool
        self.Wuea: Literal[0, 1, 2]

    @property
    def ActiveEnemy(self):
        """*read only*"""
        return self.__ActiveEnemy

    @property
    def AimVector(self):
        """*read only*"""
        return self.__AimVector

    @property
    def AnimFullName(self):
        """*read only*"""
        return self.__AnimFullName

    @property
    def AnimName(self):
        """*read only*"""
        return self.__AnimName

    @property
    def AnmPos(self):
        """*read only*"""
        return self.__AnmPos

    @property
    def AstarState(self):
        """*read only*\n
        non-player attribute"""
        return self.__AstarState

    @property
    def BayRoute(self):
        """*read only*"""
        return self.__BayRoute

    @property
    def CharType(self):
        """*read only*"""
        return self.__CharType

    @property
    def CharTypeExt(self):
        """*read only*"""
        return self.__CharTypeExt

    @property
    def CurrentAreas(self):
        """*read only*"""
        return self.__CurrentAreas

    @property
    def DefenceNeeded(self):
        """*read only*"""
        return self.__DefenceNeeded

    @property
    def Dist2Floor(self):
        """*read only*"""
        return self.__Dist2Floor

    @property
    def EnemyLastSeen(self):
        """*read only*"""
        return self.__EnemyLastSeen

    @property
    def InCombat(self):
        """*read only*"""
        return self.__InCombat

    @property
    def InvLeft(self):
        """*read only*"""
        return self.__InvLeft

    @property
    def InvLeft2(self):
        """*read only*"""
        return self.__InvLeft2

    @property
    def InvLeftBack(self):
        """*read only*"""
        return self.__InvLeftBack

    @property
    def InvRight(self):
        """*read only*"""
        return self.__InvRight

    @property
    def InvRightBack(self):
        """*read only*"""
        return self.__InvRightBack

    @property
    def LastSound(self):
        """*read only*"""
        return self.__LastSound

    @property
    def LastSoundPosition(self):
        """*read only*"""
        return self.__LastSoundPosition

    @property
    def MeleeActive(self):
        """*read only*"""
        return self.__MeleeActive

    @property
    def MutilationsMask(self):
        """*read only*"""
        return self.__MutilationsMask

    @property
    def OnFloor(self):
        """*read only*"""
        return self.__OnFloor

    @property
    def PrevAnimName(self):
        """*read only*"""
        return self.__PrevAnimName

    @property
    def RangeActive(self):
        """*read only*"""
        return self.__RangeActive

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def RouteType(self):
        """*read only*\n
        non-player attribute"""
        return self.__RouteType

    @property
    def Will1aaTo2aa(self):
        """*read only*"""
        return self.__Will1aaTo2aa

    @property
    def WillCrashInFloor(self):
        """*read only*"""
        return self.__WillCrashInFloor


class B_Entity_Physic(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.AngularVelocity: Vector3
        self.CastShadows: Bool
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.__FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.Frozen: Bool
        self.Gravity: Vector3
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.OnStopFunc: Optional[Callable[[str], Any]]
        self.Orientation: Quaternion
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.__TestHit: Bool
        self.Velocity: Vector3
        self.__nFires: int
        self.__nLights: int

    @property
    def FireParticleType(self):
        """*read only*"""
        return self.__FireParticleType

    @property
    def LightColor(self):
        """*read only*"""
        return self.__LightColor

    @property
    def LightGlow(self):
        """*read only*"""
        return self.__LightGlow

    @property
    def LightIntensity(self):
        """*read only*"""
        return self.__LightIntensity

    @property
    def LightPrecission(self):
        """*read only*"""
        return self.__LightPrecission

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def TestHit(self):
        """*read only*"""
        return self.__TestHit

    @property
    def nFires(self):
        """*read only*"""
        return self.__nFires

    @property
    def nLights(self):
        """*read only*"""
        return self.__nLights


class B_Entity_Pool(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Color: RGBColor
        self.DeathTime: float
        self.DeepColor: RGBColor
        self.Scale: float


class B_Entity_Sliding_Area(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.A_D: float
        self.Displacement: float
        self.DisplacementLimit: float
        self.__IsStopped: Bool
        self.OnStopFunc: Optional[Callable[[str], Any]]
        self.Orientation: Quaternion
        self.SlidingSurface: Vector3
        self.V_D: float

    @property
    def IsStopped(self):
        """*read only*"""
        return self.__IsStopped


class B_Entity_Sound(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.BaseVolume: float
        self.MaxDistance: float
        self.MinDistance: float
        self.Pitch: float
        self.__Playing: Bool
        self.SendNotify: Bool
        self.Volume: float

    @property
    def Playing(self):
        """*read only*"""
        return self.__Playing


class B_Entity_Spark(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ


class B_Entity_Spot(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.CastShadows: Bool
        self.Color: RGBColor
        self.Flick: Bool
        self.__FlickPeriod: float
        self.Intensity2: float
        self.Scale: float
        self.Visible: Bool

    @property
    def FlickPeriod(self):
        """B_ENTITYEXT_SPOT_FLICKPERIOD -> Not implemented"""
        return self.__FlickPeriod


class B_Entity_Water(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Color: RGBColor
        self.Reflection: float
        self.Scale: float
        self.TouchFluidFunc: Optional[Callable[[str, str, float], Any]]
        self.Transparency: float


class B_Entity_Weapon(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.AngularVelocity: Vector3
        self.CastShadows: Bool
        self.Cone: float
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.__FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.Frozen: Bool
        self.Gravity: Vector3
        self.Height: float
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.OnStopFunc: Optional[Callable[[str], Any]]
        self.Orientation: Quaternion
        self.Radius: float
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.__TestHit: Bool
        self.TrailColor: RGBNormalized
        self.TrailLifeTime: float
        self.Velocity: Vector3
        self.__nFires: int
        self.__nLights: int

    @property
    def FireParticleType(self):
        """*read only*"""
        return self.__FireParticleType

    @property
    def LightColor(self):
        """*read only*"""
        return self.__LightColor

    @property
    def LightGlow(self):
        """*read only*"""
        return self.__LightGlow

    @property
    def LightIntensity(self):
        """*read only*"""
        return self.__LightIntensity

    @property
    def LightPrecission(self):
        """*read only*"""
        return self.__LightPrecission

    @property
    def RasterMode(self):
        """*write only*\n
        Use `RasterModeZ`/`RasterModeAlpha` to get.\n
        Default:`Full`, `BlendingAlpha`
        """
        return AttributeError

    @RasterMode.setter
    def RasterMode(
        self,
        value: __RasterMode,
    ):
        ...

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def TestHit(self):
        """*read only*"""
        return self.__TestHit

    @property
    def nFires(self):
        """*read only*"""
        return self.__nFires

    @property
    def nLights(self):
        """*read only*"""
        return self.__nLights


# 18
class B_PyEntity(
    B_Entity_Actor,
    B_Entity_Aura,
    B_Entity_Camera,
    B_Entity_,
    B_Entity_ElectricBolt,
    B_Entity_Fire,
    B_Entity_Lava,
    B_Entity_Magic_Missile,
    B_Entity_Particle,
    B_Entity_Particle_System,
    B_Entity_Person,
    B_Entity_Physic,
    B_Entity_Pool,
    B_Entity_Sliding_Area,
    B_Entity_Sound,
    B_Entity_Spark,
    B_Entity_Spot,
    B_Entity_Water,
    B_Entity_Weapon,
):
    ...
