from __future__ import annotations

from .b_types import *


class B_PyChar:
    def __init__(self, /) -> None:
        self.AddRouteAnim: str
        self.DieFall: float
        self.DistStop: float
        self.DistStop2: float
        self.DistStopMaxFactor: float
        self.Fov: float
        self.HeadControlled: int
        self.HearMinVolume: float
        self.HighArmour: str
        self.IntName: str
        self.Jcost: float
        self.LowArmour: str
        self.MaxCombatDist: float
        self.MaxFall: float
        self.MaxGrab: float
        self.MaxSeeDist: float
        self.MaxStair: float
        self.MaxTake1: float
        self.MaxTake2: float
        self.MaxTake3: float
        self.MaxTake4: float
        self.MaxTake5: float
        self.MedArmour: str
        self.MedGrab: float
        self.Min2Grab: float
        self.MinTake: float
        self.MovBkwdSpeedInStrafe: float
        self.MovFrwdSpeedInStrafe: float
        self.NaturalWeapons: int
        self.NoArmour: str
        self.Reach: float
        self.TurnSpeed: float

    def AddAttack(self, attack_name: str, anm_name: str, /) -> Bool:
        ...

    def AddEnergyLevel(self, anm_name: str, level: int, /) -> Bool:
        ...

    def AddLevels(
        self, anm_name: str, allow_attack_lv: int, allow_destructor_lv: int, /
    ) -> Bool:
        ...

    @overload
    def AllowAttack(
        self,
        attack_name: str,
        keys: Literal["R", "L", "F", "B", "A", "D"],
        previous: str,
        previous_negative: str,
        window_name: str,
        weapon_kind: Literal["1H", "2W", "AXE", "SP"] = "1H",
        /,
    ) -> Bool:
        ...

    @overload
    def AllowAttack(
        self,
        attack_name: str,
        keys: str,
        previous: str,
        previous_negative: str,
        window_name: str,
        weapon_kind: str = "1H",
        /,
    ) -> Bool:
        ...

    def AllowAttack(
        self,
        attack_name: str,
        keys: str,
        previous: str,
        previous_negative: str,
        window_name: str,
        weapon_kind: str = "1H",
        /,
    ) -> Bool:
        """
        :keys Modifiers:
            R+L - Simultaneous press\n
            !F - Should not be pressed\n
            &F - Should be already pressed
        """
        ...

    @overload
    def AssignTrail(
        self,
        attack_name: str,
        unknown: Literal[""],
        trail_name: Literal[
            "EstelaAmarilla1", "EstelaAzul1", "EstelaGris1", "EstelaRoja1"
        ],
        /,
    ) -> Bool:
        ...

    @overload
    def AssignTrail(self, attack_name: str, unknown: str, trail_name: str, /) -> Bool:
        ...

    def AssignTrail(self, attack_name: str, unknown: str, trail_name: str, /) -> Bool:
        ...

    def AttackTypeFlag(self, attack_name: str, flag: int, /) -> Bool:
        ...

    def AttackWindow(
        self, anm_name: str, window_start: float, window_end: float, window_name: str, /
    ) -> Bool:
        ...

    def ChangeAnimation(self, old_anm_name: str, new_anm_name: str, /) -> Bool:
        ...

    def LoadAllAnimations(self, /) -> Bool:
        ...

    def MetaAttack(self, meta_attack_name: str, attack_name: str, /) -> Bool:
        ...

    def SetAnmDefaultPrefix(self, prefix: str, /) -> Bool:
        ...

    def SetCDSphere(self, index: int, height: float, radius: float, /) -> Bool:
        ...

    def SetNCDSpheres(self, number: int, /) -> Bool:
        ...
