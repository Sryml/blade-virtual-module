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
        self.CanUse: Bool
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
        self.Material: Unknown
        self.__Name: str
        self.Object: Unknown
        self.__Parent: str
        self.Person: Bool
        self.Physic: Bool
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

    @property
    def Kind(self):
        """*read only*"""
        return self.__Kind

    @property
    def Name(self):
        """Modifying this variable is not recommended."""
        return self.__Name

    @Name.setter
    def Name(self, value: str):
        self.__Name = value

    @property
    def Parent(self):
        """*read only*"""
        return self.__Parent

    @property
    def SubscribedLists(self):
        """*read only*"""
        return self.__SubscribedLists

    # Methods
    def Abs2RelPoint(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Abs2RelVector(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddAnimSound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddAnmEventFunc(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddCameraEvent(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddCameraNode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddEventSound(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddPathNode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def AddWatchAnim(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CameraClearPath(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CameraStartPath(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CanGoTo(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CanISee(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CanISeeFrom(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CatchOnFire(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Chase(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def CheckAnimCol(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ClearAnmEventFuncs(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ClearPath(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Cut(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def DelAnmEventFunc(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def DoAction(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def DoActionWI(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ExcludeHitFor(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def ExcludeHitInAnimationFor(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Face(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Fly(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Freeze(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetActionMode(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetChild(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetCombatants(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetDummyAxis(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetEnemyName(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetGroupMembers(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetInventory(
        self, *args: Unknown, **kwargs: Unknown
    ) -> inventory.B_PyInventory:
        ...

    def GetInventoryEntity(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetInventorySelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetNChildren(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetNodeIndex(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetParticleEntity(self, *args: Unknown, **kwargs: Unknown):
        return B_Entity_Particle()

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

    def Rel2AbsPoint(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def Rel2AbsVector(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
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


class B_Entity_Default(B_Entity):
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.CastShadows: Bool
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.FireParticleType: str
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
        self.nFires: int
        self.nLights: int

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
        self.FireParticleType: Optional[str] = None
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
        self.nFires: int
        self.nLights: int

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

        self.FireParticleType: Optional[str] = None
        self.Scale: float


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


class B_Entity_Particle_System_D(B_Entity):
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
        self.AimVector: Vector3
        self.Alpha: float
        self.Angle: Radian
        self.AnimFullName: str
        self.AnimName: str
        self.AnmEndedFunc: Optional[Callable[[str], Any]]
        self.__AnmPos: float
        self.AnmTranFunc: Optional[Callable[[str], Any]]
        self.__AstarState: Literal[0, 1, 2, 3]
        self.Attack: Bool
        self.AttackFunc: Optional[Callable[[str, str], Any]]
        self.BayRoute: Bool
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
        self.DefenceNeeded: Bool
        self.DelayNoSeenFunc: Optional[Callable[[str], Any]]
        self.Dist2Floor: float
        self.EnemyDeadFunc: Optional[Callable[[str], Any]]
        self.EnemyLastSeen: Vector3
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
        self.MeleeActive: Bool
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
        self.Seen: Unknown
        self.SelfIlum: float
        self.Sneak: Unknown
        self.TakeFunc: Unknown
        self.Texture: Unknown
        self.ThrowFunc: Unknown
        self.Tl: Unknown
        self.ToggleCombatFunc: Unknown
        self.Tr: Unknown
        self.Will1aaTo2aa: Unknown
        self.WillCrashInFloor: Unknown
        self.Wuea: Unknown

    @property
    def ActiveEnemy(self):
        """*read only*"""
        return self.__ActiveEnemy

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


class B_Entity_Physic(B_Entity):
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.AngularVelocity: Unknown
        self.CastShadows: Bool
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.Frozen: Bool
        self.Gravity: Unknown
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.OnStopFunc: Unknown
        self.Orientation: Quaternion
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.TestHit: Unknown
        self.Velocity: Unknown
        self.nFires: int
        self.nLights: int

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


class B_Entity_Pool(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Color: Unknown
        self.DeathTime: Unknown
        self.DeepColor: Unknown
        self.Scale: float


class B_Entity_Sliding_Area(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.A_D: Unknown
        self.Displacement: Unknown
        self.DisplacementLimit: Unknown
        self.IsStopped: Unknown
        self.OnStopFunc: Unknown
        self.Orientation: Quaternion
        self.SlidingSurface: Unknown
        self.V_D: Unknown


class B_Entity_Sound(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.BaseVolume: Unknown
        self.MaxDistance: Unknown
        self.MinDistance: Unknown
        self.Pitch: Unknown
        self.Playing: Unknown
        self.SendNotify: Unknown
        self.Volume: Unknown


class B_Entity_Spot(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.CastShadows: Bool
        self.Color: Unknown
        self.Flick: Unknown
        self.FlickPeriod: Unknown
        self.Intensity2: Unknown
        self.Scale: float
        self.Visible: Unknown


class B_Entity_Water(B_Entity):
    def __init__(self) -> None:
        super().__init__()

        self.Color: Unknown
        self.Reflection: Unknown
        self.Scale: float
        self.TouchFluidFunc: Unknown
        self.Transparency: Unknown


class B_Entity_Weapon(B_Entity):
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

    def __init__(self) -> None:
        super().__init__()

        self.Alpha: float
        self.AngularVelocity: Unknown
        self.CastShadows: Bool
        self.Cone: Unknown
        self.ExclusionGroup: Bool
        self.ExclusionMask: Union[int, Literal[1, 2, 4, 8, 32]]
        self.FireParticleType: Optional[str] = None
        self.FiresIntensity: List[int] = []
        self.Frozen: Bool
        self.Gravity: Unknown
        self.Height: Unknown
        self.__LightColor: Tuple
        self.__LightGlow: Tuple
        self.__LightIntensity: Tuple
        self.__LightPrecission: Tuple
        self.Lights: List[Tuple[float, float, RGBColor]]
        self.OnStopFunc: Unknown
        self.Orientation: Quaternion
        self.Radius: Unknown
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.Scale: float
        self.SelfIlum: float
        self.Solid: Bool
        self.TestHit: Unknown
        self.TrailColor: Unknown
        self.TrailLifeTime: Unknown
        self.Velocity: Unknown
        self.nFires: int
        self.nLights: int

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


# 18
class B_Entity_All(
    B_Entity_Actor,
    B_Entity_Aura,
    B_Entity_Camera,
    B_Entity_Default,
    B_Entity_ElectricBolt,
    B_Entity_Fire,
    B_Entity_Lava,
    B_Entity_Magic_Missile,
    B_Entity_Particle,
    B_Entity_Particle_System_D,
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
