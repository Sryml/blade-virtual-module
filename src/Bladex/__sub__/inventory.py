from __future__ import annotations

from .b_types import *


class B_PyInventory:
    def __init__(self, /) -> None:
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
    def HasBow(self, /):
        """*read only*"""
        return self.__HasBow

    @property
    def HasBowOnBack(self, /):
        """*read only*"""
        return self.__HasBowOnBack

    @property
    def HasShieldOnBack(self, /):
        """*read only*"""
        return self.__HasShieldOnBack

    @property
    def HoldingBow(self, /):
        """*read only*"""
        return self.__HoldingBow

    @property
    def HoldingShield(self, /):
        """*read only*"""
        return self.__HoldingShield

    @property
    def Name(self, /):
        """*read only*"""
        return self.__Name

    @property
    def nKeys(self, /):
        """*read only*"""
        return self.__nKeys

    @property
    def nKindObjects(self, /):
        """*read only*"""
        return self.__nKindObjects

    @property
    def nObjects(self, /):
        """*read only*"""
        return self.__nObjects

    @property
    def nQuivers(self, /):
        """*read only*"""
        return self.__nQuivers

    @property
    def nShields(self, /):
        """*read only*"""
        return self.__nShields

    @property
    def nSpecialKeys(self, /):
        """*read only*"""
        return self.__nSpecialKeys

    @property
    def nTablets(self, /):
        """*read only*"""
        return self.__nTablets

    @property
    def nWeapons(self, /):
        """*read only*"""
        return self.__nWeapons

    @property
    def Owner(self, /):
        """*read only*"""
        return self.__Owner

    def AddBow(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddKey(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddMagicShield(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddObject(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddQuiver(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddShield(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddSpecialKey(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddTablet(self, obj_name: str, unknown: int = 0, /) -> Bool:
        """"""
        ...

    def AddWeapon(self, weapon_name: str, flag: Literal[0, 1, 2, 3] = 0, /) -> Bool:
        """
        :flag:
            W_FLAG_1H = 0  # One handed _whatever_ weapon\n
            W_FLAG_2W = 1  # Two handed sword\n
            W_FLAG_AXE = 2  # Two handed axw\n
            W_FLAG_SP = 3  # Two handed spear
        """
        ...

    def CarringObject(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def CycleKeys(self, /) -> None:
        """"""
        ...

    def CycleObjects(self, /) -> None:
        """"""
        ...

    def CycleQuivers(self, /) -> None:
        """"""
        ...

    def CycleShields(self, /) -> None:
        """"""
        ...

    def CycleWeapons(self, /) -> None:
        """"""
        ...

    def GetActiveQuiver(self, /) -> str:
        """"""
        ...

    def GetActiveShield(self, /) -> str:
        """"""
        ...

    def GetActiveWeapon(self, /) -> str:
        """"""
        ...

    def GetBow(self, /) -> str:
        """"""
        ...

    def GetKey(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetLeftBack(self, /) -> str:
        """"""
        ...

    def GetMagicShield(self, /) -> str:
        """"""
        ...

    def GetMaxNumberObjectsAt(self, index: int, /) -> int:
        """"""
        ...

    def GetNumberObjectsAt(self, index: int, /) -> int:
        """"""
        ...

    def GetObject(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetQuiver(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetRightBack(self, /) -> str:
        """"""
        ...

    def GetSelectedKey(self, /) -> str:
        """"""
        ...

    def GetSelectedObject(self, /) -> str:
        """"""
        ...

    def GetSelectedQuiver(self, /) -> str:
        """"""
        ...

    def GetSelectedShield(self, /) -> str:
        """"""
        ...

    def GetSelectedWeapon(self, /) -> str:
        """"""
        ...

    def GetShield(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetSpecialKey(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetTablet(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def GetWeapon(self, obj: Union[int, str], /) -> str:
        """"""
        ...

    def IsKeySelected(self, index: int, /) -> Bool:
        """"""
        ...

    def IsObjectSelected(self, index: int, /) -> Bool:
        """"""
        ...

    def IsQuiverSelected(self, index: int, /) -> Bool:
        """"""
        ...

    def IsShieldSelected(self, index: int, /) -> Bool:
        """"""
        ...

    def IsWeaponSelected(self, index: int, /) -> Bool:
        """"""
        ...

    def LinkBack(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkLeft(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkLeftBack(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkLeftHand(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkLeftHand2(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkRight(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkRightBack(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def LinkRightHand(self, obj_name: str, /) -> Bool:
        """
        :obj_name: To unlink use "None"
        """
        ...

    def RemoveBow(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveKey(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveMagicShield(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveObject(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveQuiver(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveShield(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveSpecialKey(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveTablet(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def RemoveWeapon(self, obj_name: str, /) -> Bool:
        """"""
        ...

    def SetCurrentQuiver(self, obj_name: str, /) -> Bool:
        """"""
        ...
