import Bladex
from b_types import *

import typing


class B_PyEntity:
    def __init__(self):
        self.__Name: str
        self.__Kind: str
        self.__OnFloor: bool
        self.__AnmPos: float
        self.__InvRight: str
        self.__InvRightBack: str
        self.__InvLeft: str
        self.__InvLeftBack: str
        self.__ActiveEnemy: str
        self.__CharType: str
        self.__CharTypeExt: str
        self.__RasterModeAlpha: Optional[str]

        ####
        self.Alpha: float
        self.Scale: float
        self.Deaf: Bool
        self.Blind: Bool
        self.SelfIlum: float
        self.CastShadows: Bool
        self.RasterMode: Literal[
            "Read", "Write", "Full", "BlendingAlpha", "AdditiveAlpha", "MultiplyAlpha"
        ]
        self.Data: Any
        self.InitPos: Vector3
        self.Life: Int
        self.Level: Int
        self.Orientation: Quaternion
        self.Position: Vector3
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
        return self.__AnmPos

    @property
    def InvRight(self):
        return self.__InvRight

    @property
    def InvRightBack(self):
        return self.__InvRightBack

    @property
    def InvLeft(self):
        return self.__InvLeft

    @property
    def InvLeftBack(self):
        return self.__InvLeftBack

    @property
    def Name(self):
        return self.__Name

    @property
    def Kind(self):
        return self.__Kind

    @property
    def OnFloor(self):
        return self.__OnFloor

    @property
    def ActiveEnemy(self):
        return self.__ActiveEnemy

    @property
    def CharType(self):
        return self.__CharType

    @property
    def CharTypeExt(self):
        return self.__CharTypeExt

    @property
    def RasterModeAlpha(self):
        return self.__RasterModeAlpha

    ####
    def Abs2RelPoint(self):
        ...

    def Abs2RelVector(self):
        ...

    def AddAnimSound(self):
        ...

    def AddAnmEventFunc(self):
        ...

    def AddCameraEvent(self):
        ...

    def AddCameraNode(self):
        ...

    def AddEventSound(self):
        ...

    def AddPathNode(self):
        ...

    def AddWatchAnim(self):
        ...

    def CameraClearPath(self):
        ...

    def CameraStartPath(self):
        ...

    def CanGoTo(self):
        ...

    def CanISee(self):
        ...

    def CanISeeFrom(self):
        ...

    def CatchOnFire(self):
        ...

    def Chase(self):
        ...

    def CheckAnimCol(self):
        ...

    def ClearAnmEventFuncs(self):
        ...

    def ClearPath(self):
        ...

    def Cut(self):
        ...

    def DelAnmEventFunc(self):
        ...

    def DoAction(self):
        ...

    def DoActionWI(self):
        ...

    def ExcludeHitFor(self):
        ...

    def ExcludeHitInAnimationFor(self):
        ...

    def Face(self):
        ...

    def Fly(self):
        ...

    def Freeze(self):
        ...

    def GetActionMode(self):
        ...

    def GetChild(self):
        ...

    def GetCombatants(self):
        ...

    def GetDummyAxis(self):
        ...

    def GetEnemyName(self):
        ...

    def GetGroupMembers(self):
        ...

    def GetInventory(self):
        ...

    def GetInventoryEntity(self):
        ...

    def GetInventorySelected(self):
        ...

    def GetNChildren(self):
        ...

    def GetNodeIndex(self):
        ...

    def GetParticleEntity(self):
        ...

    def GetWoundedZone(self):
        ...

    def GoTo(self):
        ...

    def GoToPath(self):
        ...

    def GotAnmType(self):
        ...

    def GraspPos(self):
        ...

    def Impulse(self):
        ...

    def ImpulseC(self):
        ...

    def InsideActionArea(self):
        ...

    def InterruptCombat(self):
        ...

    def IsValid(self):
        ...

    def LaunchAnimation(self):
        ...

    def LaunchAnimation2(self):
        ...

    def LaunchAnmType(self):
        ...

    def LaunchBayRoute(self):
        ...

    def LaunchWatch(self):
        ...

    def Link(self):
        ...

    def LinkAnchors(self):
        ...

    def LinkToNode(self):
        ...

    def LookAt(self):
        ...

    def LookAtEntity(self):
        ...

    def LookAtPerson(self):
        ...

    def MessageEvent(self):
        ...

    def Move(self):
        ...

    def PlaySound(self):
        ...

    def PutToWorld(self):
        ...

    def QuickFace(self):
        ...

    def RaiseEvent(self):
        ...

    def Rel2AbsPoint(self):
        ...

    def Rel2AbsVector(self):
        ...

    def RemoveCameraEvent(self):
        ...

    def RemoveFromInvent(self):
        ...

    def RemoveFromInventLeft(self):
        ...

    def RemoveFromInventLeft2(self):
        ...

    def RemoveFromInventRight(self):
        ...

    def RemoveFromList(self):
        ...

    def RemoveFromWorld(self):
        ...

    def RemoveFromWorldWithChilds(self):
        ...

    def ResetChase(self):
        ...

    def ResetWounds(self):
        ...

    def Rotate(self):
        ...

    def RotateAbs(self):
        ...

    def RotateRel(self):
        ...

    def SQDistance2(self):
        ...

    def SetActiveEnemy(self):
        ...

    def SetAnmFlags(self):
        ...

    def SetAuraActive(self):
        ...

    def SetAuraGradient(self):
        ...

    def SetAuraParams(self):
        ...

    def SetCameraEndTangentNode(self):
        ...

    def SetCameraStartTangentNode(self):
        ...

    def SetEnemy(self):
        ...

    def SetMaxCamera(self):
        ...

    def SetMesh(self):
        ...

    def SetNextAttack(self):
        ...

    def SetNodeEndTangent(self):
        ...

    def SetNodeStartTangent(self):
        ...

    def SetObjectSound(self):
        ...

    def SetOnFloor(self):
        ...

    def SetOrientation(self):
        ...

    def SetPersonView(self):
        ...

    def SetPosition(self):
        ...

    def SetSound(self):
        ...

    def SetTmpAnmFlags(self):
        ...

    def SetTravellingView(self):
        ...

    def SetWoundedZone(self):
        ...

    def SeverLimb(self, limb: int):
        ...

    def SlideTo(self):
        ...

    def StartGrabbing(self):
        ...

    def StartLooking(self):
        ...

    def StartPath(self):
        ...

    def Stop(self):
        ...

    def StopGrabbing(self):
        ...

    def StopLooking(self):
        ...

    def StopSound(self):
        ...

    def SubscribeToList(self):
        ...

    def SwitchTo1H(self):
        ...

    def SwitchToBow(self):
        ...

    def TestPos(self):
        ...

    def TestPosInOwnBox(self):
        ...

    def TurnOff(self):
        ...

    def TurnOn(self):
        ...

    def UnFreeze(self):
        ...

    def Unlink(self):
        ...

    def UnlinkChildren(self):
        ...

    def Use(self):
        ...
