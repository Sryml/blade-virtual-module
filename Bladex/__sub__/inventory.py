from __future__ import annotations
from .b_types import *


class B_PyInventory:
    def __init__(self) -> None:
        self.__HasBow: Bool
        self.__HasBowOnBack: Bool
        self.__HasShieldOnBack: Bool
        self.__HoldingBow: Bool
        self.__HoldingShield: Bool
        self.maxObjects: int
        self.maxQuivers: int
        self.maxShields: int
        self.maxWeapons: int
        self.__Name: str
        self.__nKeys: int
        self.__nKindObjects: int
        self.__nObjects: int
        self.__nQuivers: int
        self.__nShields: int
        self.__nSpecialKeys: int
        self.__nTablets: int
        self.__nWeapons: int
        self.__Owner: str

    @property
    def HasBow(self):
        """*read only*"""
        return self.__HasBow

    @property
    def HasBowOnBack(self):
        """*read only*"""
        return self.__HasBowOnBack

    @property
    def HasShieldOnBack(self):
        """*read only*"""
        return self.__HasShieldOnBack

    @property
    def HoldingBow(self):
        """*read only*"""
        return self.__HoldingBow

    @property
    def HoldingShield(self):
        """*read only*"""
        return self.__HoldingShield

    @property
    def Name(self):
        """*read only*"""
        return self.__Name

    @property
    def nKeys(self):
        """*read only*"""
        return self.__nKeys

    @property
    def nKindObjects(self):
        """*read only*"""
        return self.__nKindObjects

    @property
    def nObjects(self):
        """*read only*"""
        return self.__nObjects

    @property
    def nQuivers(self):
        """*read only*"""
        return self.__nQuivers

    @property
    def nShields(self):
        """*read only*"""
        return self.__nShields

    @property
    def nSpecialKeys(self):
        """*read only*"""
        return self.__nSpecialKeys

    @property
    def nTablets(self):
        """*read only*"""
        return self.__nTablets

    @property
    def nWeapons(self):
        """*read only*"""
        return self.__nWeapons

    @property
    def Owner(self):
        """*read only*"""
        return self.__Owner

    def AddBow(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddKey(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddMagicShield(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddObject(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddQuiver(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddShield(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddSpecialKey(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddTablet(self, obj_name: str, unknown: int = 0) -> int:
        """"""
        ...

    def AddWeapon(self, weapon_name: str, flag: Literal[0, 1, 2, 3] = 0) -> int:
        """
        :flag:
            W_FLAG_1H = 0  # One handed _whatever_ weapon\n
            W_FLAG_2W = 1  # Two handed sword\n
            W_FLAG_AXE = 2  # Two handed axw\n
            W_FLAG_SP = 3  # Two handed spear
        """
        ...

    def CarringObject(self, obj_name: str) -> int:
        """"""
        ...

    def CycleKeys(self) -> None:
        """"""
        ...

    def CycleObjects(self) -> None:
        """"""
        ...

    def CycleQuivers(self) -> None:
        """"""
        ...

    def CycleShields(self) -> None:
        """"""
        ...

    def CycleWeapons(self) -> None:
        """"""
        ...

    def GetActiveQuiver(self) -> str:
        """"""
        ...

    def GetActiveShield(self) -> str:
        """"""
        ...

    def GetActiveWeapon(self) -> str:
        """"""
        ...

    def GetBow(self) -> str:
        """"""
        ...

    def GetKey(self, obj: Union[int, str]) -> str:
        """"""
        ...

    def GetLeftBack(self) -> str:
        """"""
        ...

    def GetMagicShield(self) -> str:
        """"""
        ...

    def GetMaxNumberObjectsAt(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetNumberObjectsAt(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetObject(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetQuiver(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetRightBack(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSelectedKey(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSelectedObject(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSelectedQuiver(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSelectedShield(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSelectedWeapon(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetShield(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetSpecialKey(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetTablet(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def GetWeapon(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def IsKeySelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def IsObjectSelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def IsQuiverSelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def IsShieldSelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def IsWeaponSelected(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkBack(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkLeft(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkLeftBack(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkLeftHand(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkLeftHand2(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkRight(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkRightBack(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def LinkRightHand(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveBow(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveKey(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveMagicShield(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveObject(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveQuiver(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveShield(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveSpecialKey(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveTablet(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def RemoveWeapon(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...

    def SetCurrentQuiver(self, *args: Unknown, **kwargs: Unknown) -> Unknown:
        """"""
        ...
