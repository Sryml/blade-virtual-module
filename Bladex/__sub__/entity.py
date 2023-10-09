from __future__ import annotations

# import Bladex
from . import inventory
from .b_types import *

import typing

# Entity.init_entity_properties


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
        self, x: float, y: float, z: float, node_name: Union[str, NULL] = NULL(0)
    ) -> Vector3:
        ...

    def Abs2RelVector(
        self, x: float, y: float, z: float, node_name: Union[str, NULL] = NULL(0)
    ) -> Vector3:
        ...

    def AddAnimSound(self, animation: str, sound: B_Entity_Sound, time: float) -> Bool:
        ...

    def AddAnmEventFunc(self, anm_event: str, func: Callable[[str, str], Any]) -> Bool:
        ...

    def AddCameraEvent(self, frame: int, func: Callable[[str, int], Any]) -> Bool:
        ...

    def AddCameraNode(
        self, node: int, time: float, x: float, y: float, z: float
    ) -> Bool:
        ...

    def AddEventSound(self, event_name: str, sound: B_Entity_Sound) -> Bool:
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

    def CanISee(self, ent: B_PyEntity) -> Bool:
        ...

    def CanISeeFrom(self, ent: B_PyEntity, x: float, y: float, z: float) -> Bool:
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
        interpolation_type: int,
        time: float,
        unknown: float = 0.0,
    ) -> int:
        ...

    def ExcludeHitFor(self, ent: B_PyEntity) -> Bool:
        ...

    def ExcludeHitInAnimationFor(self, ent: B_PyEntity) -> Bool:
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
        x_axis: float,
        y_axis: float,
        z_axis: float,
        unknown: int = 1,
    ) -> Tuple:
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

    def GetWoundedZone(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GoTo(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GoToPath(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GotAnmType(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GraspPos(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Impulse(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ImpulseC(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def InsideActionArea(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def InterruptCombat(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def IsValid(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LaunchAnimation(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LaunchAnimation2(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LaunchAnmType(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LaunchBayRoute(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LaunchWatch(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Link(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LinkAnchors(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LinkToNode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LookAt(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LookAtEntity(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def LookAtPerson(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def MessageEvent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Move(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def PlaySound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def PutToWorld(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def QuickFace(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RaiseEvent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Rel2AbsPoint(
        self, x: float, y: float, z: float, node_name: Union[str, NULL] = NULL(0)
    ) -> Vector3:
        ...

    def Rel2AbsVector(
        self, x: float, y: float, z: float, node_name: Union[str, NULL] = NULL(0)
    ) -> Vector3:
        ...

    def RemoveCameraEvent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromInvent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromInventLeft(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromInventLeft2(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromInventRight(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromList(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromWorld(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RemoveFromWorldWithChilds(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ResetChase(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ResetWounds(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Rotate(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RotateAbs(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def RotateRel(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SQDistance2(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetActiveEnemy(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetAnmFlags(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetAuraActive(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetAuraGradient(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetAuraParams(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetCameraEndTangentNode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetCameraStartTangentNode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetEnemy(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetMaxCamera(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetMesh(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetNextAttack(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetNodeEndTangent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetNodeStartTangent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetObjectSound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetOnFloor(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetOrientation(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetPersonView(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetPosition(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetSound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetTmpAnmFlags(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetTravellingView(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SetWoundedZone(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SeverLimb(self, limb: int):
        ...

    def SlideTo(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StartGrabbing(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StartLooking(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StartPath(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Stop(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StopGrabbing(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StopLooking(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def StopSound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SubscribeToList(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SwitchTo1H(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def SwitchToBow(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def TestPos(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def TestPosInOwnBox(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def TurnOff(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def TurnOn(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def UnFreeze(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Unlink(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def UnlinkChildren(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Use(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...


class B_Entity_(B_Entity):
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

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
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

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
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

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
        self.OnStepFunc: Optional[Callable[[Unknown], Any]]
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
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

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
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

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
    B_Entity_Spot,
    B_Entity_Water,
    B_Entity_Weapon,
):
    ...
