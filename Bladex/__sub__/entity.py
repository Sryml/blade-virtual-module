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

    def GetInventory(self, *args: Unknown, **kwargs: Unknown) -> inventory.B_PyInventory:
        ...

    def GetInventoryEntity(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetInventorySelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetNChildren(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetNodeIndex(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        ...

    def GetParticleEntity(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
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
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Actor(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Aura(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Camera(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_ElectricBolt(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Fire(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Lava(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Magic_Missile(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Particle(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Particle_System_D(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Person(B_Entity):
    __RasterMode = Literal[
        "Full", "Read", "Write", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
    ]

    def __init__(self) -> None:
        super().__init__()

        self.__OnFloor: bool
        self.__AnmPos: float
        self.__InvRight: str
        self.__InvRightBack: str
        self.__InvLeft: str
        self.__InvLeftBack: str
        self.__ActiveEnemy: str
        self.__CharType: str
        self.__CharTypeExt: str
        self.__RasterModeZ: Literal["Full", "Read", "Write"]
        self.__RasterModeAlpha: Literal[
            "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha", None
        ]

        ####
        self.Alpha: float
        self.Scale: float
        self.Deaf: Bool
        self.Blind: Bool
        self.SelfIlum: float
        self.CastShadows: Bool
        self.InitPos: Vector3
        self.Life: Int
        self.Level: Int
        self.Orientation: Quaternion
        self.AnmEndedFunc: Optional[Callable[[str], Any]]
        self.RouteEndedFunc: Optional[Callable[[str], Any]]
        self.Person: Bool
        self.Physic: Bool
        self.Actor: Bool
        self.Arrow: Bool
        self.Weapon: Bool
        self.Static: Bool
        self.Frozen: Bool
        self.AimOffTarget: float
        self.ActionAreaMin: Int
        self.ActionAreaMax: Int
        self.GoToSneaking: Bool
        self.GoToJogging: Bool
        self.InvertedRoute: Bool
        self.AddBayPoint: Vector3
        self.HitShieldFunc: Optional[Callable]

    @property
    def AnmPos(self):
        """*read only*"""
        return self.__AnmPos

    @property
    def InvRight(self):
        """*read only*"""
        return self.__InvRight

    @property
    def InvRightBack(self):
        """*read only*"""
        return self.__InvRightBack

    @property
    def InvLeft(self):
        """*read only*"""
        return self.__InvLeft

    @property
    def InvLeftBack(self):
        """*read only*"""
        return self.__InvLeftBack

    @property
    def OnFloor(self):
        """*read only*"""
        return self.__OnFloor

    @property
    def ActiveEnemy(self):
        """*read only*"""
        return self.__ActiveEnemy

    @property
    def CharType(self):
        """*read only*"""
        return self.__CharType

    @property
    def CharTypeExt(self):
        """*read only*"""
        return self.__CharTypeExt

    @property
    def RasterModeZ(self):
        """*read only*\n
        Default:`"Full"`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeZ

    @property
    def RasterModeAlpha(self):
        """*read only*\n
        Default:`None`\n
        Use `RasterMode` to set this value.
        """
        return self.__RasterModeAlpha

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


class B_Entity_Physic(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Pool(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Sliding_Area(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Sound(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Spot(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Water(B_Entity):
    def __init__(self) -> None:
        super().__init__()


class B_Entity_Weapon(B_Entity):
    def __init__(self) -> None:
        super().__init__()


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
