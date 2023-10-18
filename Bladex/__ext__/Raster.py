# Module 'Raster'
from __future__ import annotations

import typing as __t

import Bladex.__sub__.b_types as __bt


def BmpHandle(bmp_name: str) -> int:
    """"""
    ...


def BmpName(bmp_handle: int) -> str:
    """"""
    ...


def ClassIdName() -> str:
    """"""
    ...


def Cls(r: int, g: int, b: int) -> None:
    """"""
    ...


def DrawBitmap(bmp_handle: int, w: int, h: int) -> None:
    """"""
    ...


@__t.overload
def DrawImage(w: int, h: int, color_channel: str, align: str, image_data: int) -> None:
    """"""
    ...


@__t.overload
def DrawImage(
    w: int,
    h: int,
    color_channel: __t.Literal["RGB", "BGR"],
    align: __t.Literal[
        "Cover",
        "Native",
        "Normal",
        "ScaledCentered",
        "ScaledCentered2",
        "Stretch",
        "UpsideDown",
    ],
    image_data: int,
) -> None:
    """"""
    ...


def DrawImage(*args: __t.Any, **kwargs: __t.Any) -> __t.Any:
    """"""
    ...


def FullScreen() -> __bt.Bool:
    """"""
    ...


def GetAlpha() -> float:
    """"""
    ...


def GetBrightness() -> float:
    """"""
    ...


def GetClipActive() -> __bt.Bool:
    """"""
    ...


def GetClipWindow() -> __t.Tuple[int, int, int, int]:
    """
    :return: (x, y, w, h)
    """
    ...


def GetContrast() -> float:
    """"""
    ...


def GetCurrentMode() -> __t.Tuple[int, int, int, int, int]:
    """
    :return: (depth, w, h, flags, frequency)
    """
    ...


def GetDomeColor() -> __bt.RGBColor:
    """"""
    ...


def GetGammaCorrection() -> float:
    """"""
    ...


def GetImage(
    x: int,
    y: int,
    w: int,
    h: int,
    color_channel: __t.Union[__t.Literal["RGB", "BGR"], __bt.str_],
    align: __t.Literal[
        "Cover",
        "Native",
        "Normal",
        "ScaledCentered",
        "ScaledCentered2",
        "Stretch",
        "UpsideDown",
    ],
    image_size: int,
    image_data: int,
) -> __bt.Bool:
    """"""
    ...


def GetPosition() -> __bt.Vector2:
    """"""
    ...


def GetRasterParameter(parameter: str) -> str:
    """"""
    ...


def GetSize() -> __t.Tuple[int, int]:
    """
    :return: (w, h)
    """
    ...


def GetTextAlpha() -> float:
    """"""
    ...


def GetTextBlur() -> __t.Tuple[int, int, int, int]:
    """
    :return: (blurLeft, blurTop, blurRight, blurBottom)
    """
    ...


def GetTextBlurAlpha() -> float:
    """"""
    ...


def GetTextMode() -> int:
    """"""
    ...


def GetTextScale() -> __t.Tuple[float, float]:
    """
    :return: (scale_x, scale_y)
    """
    ...


def GetTextShadow() -> __t.Tuple[int, int]:
    """
    :return: (x_shadow, y_shadow)
    """
    ...


def GetTextureInfo(index: int) -> __t.Tuple[int, int, int]:
    """
    :return: (w, h, depth)
    """
    ...


def GetVideoModeDscr(mode_index: int) -> __t.Tuple[int, int, int, int, int]:
    """
    :return: (depth, w, h, flags, frequency)
    """
    ...


def GetWindowSize() -> __t.Tuple[int, int]:
    """
    :return: (w, h)
    """
    ...


def Line(x1: int, y1: int, x2: int, y2: int) -> None:
    """"""
    ...


def LineTo(x: int, y: int) -> None:
    """"""
    ...


def Rectangle(x1: int, y1: int, x2: int, y2: int) -> None:
    """"""
    ...


def RemoveBackgroundImage() -> None:
    """"""
    ...


def SetAlpha(alpha: float) -> None:
    """"""
    ...


def SetBackgroundImage(
    w: int,
    h: int,
    color_channel: __t.Literal["RGB"],
    is_normal: __t.Literal["Normal"],
    align: __t.Literal[
        "Cover",
        "Stretch",
        "ScaledCentered",
        "VerticalStretch",
    ],
    image_data: int,
) -> None:
    """"""
    ...


def SetBrightness(v: float) -> None:
    """"""
    ...


def SetClipActive(active: int) -> None:
    """"""
    ...


def SetClipWindow(x: int, y: int, w: int, h: int) -> None:
    """"""
    ...


def SetContrast(v: float) -> None:
    """"""
    ...


def SetDomeColor(r: int, g: int, b: int) -> None:
    """"""
    ...


def SetFillColor(r: int, g: int, b: int) -> None:
    """"""
    ...


def SetFlags(flags: int) -> None:
    """"""
    ...


def SetFont(font_pointer: int) -> None:
    """"""
    ...


def SetGammaCorrection(v: float) -> None:
    """"""
    ...


def SetPenColor(r: int, g: int, b: int) -> None:
    """"""
    ...


def SetPosition(x: int, y: int) -> None:
    """"""
    ...


def SetRasterParameter(parameter: str, value: str) -> __bt.Bool:
    """"""
    ...


def SetTextAlpha(v: float) -> None:
    """"""
    ...


def SetTextBlur(blurLeft: int, blurTop: int, blurRight: int, blurBottom: int) -> None:
    """"""
    ...


def SetTextBlurAlpha(v: float) -> None:
    """"""
    ...


def SetTextBlurColor(r: int, g: int, b: int) -> None:
    """"""
    ...


def SetTextColor(r: int, g: int, b: int) -> None:
    """"""
    ...


def SetTextMode(mode: int) -> None:
    """SetTextMode(3)"""
    ...


def SetTextScale(scale_x: float, scale_y: float) -> None:
    """"""
    ...


def SetTextShadow(x_shadow: int, y_shadow: int) -> None:
    """"""
    ...


def SetVideoMode(mode: int) -> __bt.Bool:
    """"""
    ...


def SetVideoSettings(gamma: float, contrast: float, brightness: float) -> None:
    """"""
    ...


def SetWindowSize(w: int = -1, h: int = -1) -> __bt.Bool:
    """"""
    ...


def SolidRectangle(x1: int, y1: int, x2: int, y2: int) -> None:
    """"""
    ...


def SwapBuffers() -> None:
    """"""
    ...


def SysWrite(x: int, y: int, text: str, r: int, g: int, b: int) -> None:
    """"""
    ...


def UnifyRenderBuffers() -> None:
    """"""
    ...


def WriteText(text: str) -> __bt.Bool:
    """"""
    ...


def nTextures() -> int:
    """"""
    ...


def nVideoModes() -> int:
    """"""
    ...


#########
# reissue


def DrawResizeImage(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...


def GetScaledCenteredSizeFactor(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...


def GetUnscaledSize(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...


def ResetScale(*args: __bt.todo, **kwargs: __bt.todo) -> __bt.Bool:
    """*reissue only*"""
    ...
