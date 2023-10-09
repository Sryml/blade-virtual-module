# 09 2023 sryml
# Module 'Bladex'
from __future__ import annotations
from . import entity as __entity
from . import b_types as __bt

import typing as __t


def ActivateInput(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ActivateInput()
    Reactivate the input for the main player."""
    ...


def AddActionStepSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddActionStepSound(table,action,step_sound_table)"""
    ...


def AddAnimFlags(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddAnimFlags(string,wuea,mdf_y,solf,copy_rot,bng_mov,head_f)"""
    ...


def AddAnmEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmAddEvent(anm_name,event_name,event_frame)"""
    ...


def AddAnmLRelease(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddAnmLStep(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddAnmRRelease(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddAnmRStep(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddBipedAction(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddBoundFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddBoundFunc(string key,proc)
     Asigna el procedimiento pr al suceso key.
    AddBoundFunc(string key,string predproc)
     Asigna el procedimiento predefinifo predproc  al suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """
    ...


def AddCombustionDataFor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddCombustionDataFor(object_kind,upper_treshol,lower_treshold,flame_height,flame_size,speed,livetime)"""
    ...


def AddFloorCTolerance(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddFloorCTolerance(anm_name,float)"""
    ...


def AddGhostSector(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddGhostSector(string GhostName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""
    ...


def AddInputAction(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddInputAction(string action_name,int npi)
    Crea una acción nueva."""
    ...


def AddMaterialStepSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddMaterialStepSound(table,material,step_sound)"""
    ...


def AddMusicEventADPCM(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddMusicEventADPCM( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""
    ...


def AddMusicEventCD(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddMusicEventCD(lpszEventName, iTrack, dFIn, dFOut, fVolume, fPriority, bBackGround, iNext)"""
    ...


def AddMusicEventMP3(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddMusicEventMP3( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""
    ...


def AddMusicEventWAV(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddMusicEventWAV( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext, [opened])"""
    ...


def AddParticleGType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AddScheduledFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddScheduledFunc(double time,Func,Args)
    Llama a la funcion Func con los argumentos Args en el tiempo time"""
    ...


def AddStepSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddStepSound(name,sound)"""
    ...


def AddStopTests(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmStopTests(anm_name)"""
    ...


def AddTextureMaterial(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddTextureMaterial(texture,material)"""
    ...


def AddTranTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddTranTime (string biped_name,string next_anm , string prev_anm , double time )
    Al pasar de animacion prev_anm a next_anm la transicion dura t segs . 0 si no transicion .
    """
    ...


def AddTriggerSector(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddTriggerSector(string TriggerSectorName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""
    ...


def AddWatchAnim(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AddWatchAnim(string)
     Establece esa animacion como una de las incluidas en modo watch.
    NOTA : NO es ejecutada por defecto por ningun personaje , para eso hay otra funcion !.
    """
    ...


def AnmAddEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmAddEvent(anm_name,event_name,event_frame)
    Declara en la animacion de nombre anm_name un evento de nombre event_name en el frame event_frame
    """
    ...


def AnmClearEvents(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmClearEvents(anm_name)
    Borra en la animacion de nombre anm_name todos los eventos"""
    ...


def AnmDelEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmDelEvent(anm_name,event_name)
    Borra en la animacion de nombre anm_name el evento de nombre event_name"""
    ...


def AnmGetEventFrame(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """AnmGetEventFrame(anm_name,event_name)
    Devuelve en la animacion de nombre anm_name frame del evento de nombre event_name y si no existe devuelve -1
    """
    ...


def AnmTypeLSteps(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AnmTypeRSteps(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def AssocKey(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool AssocKey(string action,string input_device,string key[,int press])
    Asocia la acción action con la tecla key del dispositivo input_device"""
    ...


def BeginLoadGame(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """void BeginLoadGame()
    Indica a la engine que se va a cargar una partida grabada para que pueda ajustar parámetros.
    """
    ...


def Bind2(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Bind2(void)
    Associate a combination of 2 Actions keys to a new Action, time window settings."""
    ...


def BodInspector(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """BodInspector()"""
    ...


def CDCallBack(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int CDCallBack(func f)
    Establece la función CD."""
    ...


def CDLenght(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int CDLenght()
    Devuelve la duración del CD en milisegundos."""
    ...


def CDPause(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int CDPause()
    Detiene el CD."""
    ...


def CDPlayTrack(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """PlayCDTrack(int ntrack)
    Reproduce la pista ntrack del CD.
    Si ntrack==1 reproduce todo el CD."""
    ...


def CDPresent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int CDPresent()
    Indica si está el CD."""
    ...


def CDStop(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int CDStop()
    Detiene el CD."""
    ...


def CDTrackLenght(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CDTrackLenght(int ntrack)
    Devuelve la duración en milisegundos de la pista ntrack."""
    ...


def CDnTracks(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int nCDTracks()
    Devuelve el número de pistas del CD."""
    ...


def CheckAnims(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Gives a report of anims not assigned"""
    ...


def CheckPyErrors(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """returns whether a python error has occured."""
    ...


def CleanArea(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CleanArea(x,y,z,distance)
      Limpia una zona esferica con centro en 'x,y,z'
    y distancia 'distance' de sangre."""
    ...


def CloseDebugChannel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool CloseDebugChannel(string channel_name)
    Cierra el canal de depuración de nombre channel_name."""
    ...


def CloseLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CloseLevel([string statement])
    Cierra el nivel actual y ejecuta la instrucción statement."""
    ...


def CloseProfileSection(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool CloseProfileSection(int section)
    Tiene que estar activado el profiler interno.
    Cierra la sección i."""
    ...


def CreateBipedData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def CreateDFCAnimation(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateDFCAnmimation(str File1,str File2,str InternalName,int n_armonics)"""
    ...


# CreateEntity >>>

# __Type = __t.NewType("B_PyEntity", __entity.B_Entity_Aura)


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Aura"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Aura:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Camera"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Camera:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity ElectricBolt"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_ElectricBolt:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Fire", "Entity Dynamic Fire"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Fire:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Lava"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Lava:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Magic Missile"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Magic_Missile:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Particle"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Particle:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal[
        "Entity Particle System D1",
        "Entity Particle System D2",
        "Entity Particle System D3",
        "Entity Particle System Dobj",
        "Entity Particle System Dperson",
    ],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> B_Entity_Particle_System:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Pool"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Pool:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Sliding Area"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Sliding_Area:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Sound"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Sound:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Spot"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Spot:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Literal["Entity Water"],
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_Water:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Actor"],
    mesh_name: str = "",
) -> __entity.B_Entity_Actor:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Person"],
    mesh_name: str = "",
) -> __entity.B_Entity_Person:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Arrow", "Weapon"],
    mesh_name: str = "",
) -> __entity.B_Entity_Weapon:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["Physic"],
    mesh_name: str = "",
) -> __entity.B_Entity_Physic:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __entity.B_Entity_:
    ...


@__t.overload
def CreateEntity(
    name: str,
    kind: __t.Union[__bt.Builtin_Kind, __bt.BodList],
    x: float,
    y: float,
    z: float,
    parent_class: __t.Literal["", "Actor", "Arrow", "Person", "Physic", "Weapon"] = "",
    mesh_name: str = "",
):
    ...


def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    mesh_name: str = "",
) -> __t.Any:
    """CreateEntity(string name,string kind,double x,double y,double z)\n
    Crea una entidad nueva."""
    ...


# CreateEntity <<<


def CreateFCAnimation(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateFCAnmimation(str File,str InternalName,int n_armonics)"""
    ...


def CreateMaterial(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateMaterial(string name)
    Crea un nuevo material con nombre name."""
    ...


def CreateRoute(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateRoute()
    Crea una ruta vacía nueva."""
    ...


def CreateSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateSound(string filename,string soundname)
    Crea un sonido a partir del filename y con nombre name."""
    ...


def CreateSpark(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateSpark(string name,double x,double y,double z,)
    Crea un efecto de chispas."""
    ...


def CreateTimer(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """CreateTimer(string TimerName,double period)
    Crea un Timer de nombre TimerName con periodo period."""
    ...


def DeactivateInput(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """DeactivateInput()
    Disabled the input for the main player."""
    ...


def DeleteEntity(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """DeleteEntity(string name/object entity)
    Delete existing object.  Use with care.  Subscribe to Pin if unsure."""
    ...


def DeleteStringValue(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string DeleteStringValue(string variable)
    Elimina variable."""
    ...


def DisableProfiler(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool DisableProfiler(void)
    desactivar profiler interno."""
    ...


def DoneLoadGame(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """void DoneLoadGame()
    Indica a la engine que se ha cargado una partida grabada para que pueda ajustar parámetros.
    """
    ...


def DrawBOD(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """DrawBOD(string BODName,int x,int y,int ancho,int alto)
    Dibuja el BOD de nombre BODName en el rectángulo x,y,ancho,alto."""
    ...


def DumpMemoryLeaks(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool DumpMemoryLeaks(string filename)
    Dumps cuurent memory allocations to filename."""
    ...


def EnableProfiler(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool EnableProfiler(void)
    activar profiler interno."""
    ...


def ExeMusicEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ """
    ...


def ExportWorld(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ExportWorld ()
    Export the world to owner Max format."""
    ...


def GenerateEntityName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GenerateEntityName()
    Generates a new and unique entity name."""
    ...


def GetAecGap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool GetAecGap()
    Devuelve tiempo de auto encaramientpo....."""
    ...


def GetAfterFrameFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame de nombre name."""
    ...


def GetAfterFrameFuncName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetAfterFrameFuncName(int idx)
    Devuelve el nombre de la función AfterFrame del sistema de índice idx."""
    ...


def GetAnimationDuration(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetAnimationDuration (string sampled animation name )
    Resturns the duration in seconds of the full animation disregarding interpolation.
    """
    ...


def GetAnmRaces(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """list GetAnmRaces(void)
    Devuelve una lista con los nombres de las razas cargadas en memoria."""
    ...


def GetAppMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetAppMode()
    Obtiene el modo de la aplicación (Game, Menu,...)."""
    ...


def GetAutoEngageCombat(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool GetAutoEngageCombat()
    Devuelve true si se encara automaticanmente si se puede."""
    ...


def GetBloodLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetBloodLevel()
    Obtiene el nivel de sangre."""
    ...


def GetCharType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetCharType(Barbarian,Bar)
    Crea un CharType , o raza de personaje."""
    ...


def GetCombos(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetCombos(blah blah BLAH!)"""
    ...


def GetCommandLine(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetCommandLine()
    Obtiene la línea de órdenes que se ha pasado a la aplicación."""
    ...


def GetCurrentMap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetCurrentMap()
    Devuelve el mapa actual."""
    ...


def GetDrawObjectShadows(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool GetDrawObjectShadows()
    Devuelve si se dibujan las sombras de los objetos/personajes."""
    ...


def GetEAXOverride(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """float GetEAXOverride()"""
    ...


def GetEnemiesVisibleFrom(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetEnemiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


def GetEntitiesAt(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetEntitiesAt(double x,double y,double z,double radius)
    Obtiene las entidades que están en un radio radius de la posición (x,y,z)"""
    ...


def GetEntitiesVisibleFrom(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


@__t.overload
def GetEntity(arg: __t.Literal["Player1"]) -> __entity.B_Entity_Person:
    ...


@__t.overload
def GetEntity(arg: __t.Literal["Camera"]) -> __entity.B_Entity_Camera:
    ...


@__t.overload
def GetEntity(
    arg: __t.Union[str, int, __t.Literal["Camera", "Player1"]]
) -> __entity.B_PyEntity:
    ...


def GetEntity(arg: __t.Union[str, int]) -> __t.Any:
    """GetEntity(int n)
     Crea una entidad de Python que referencia a la entidad Blade de índice n.
    GetEntity(string name)
     Crea una entidad de Python que referencia a la entidad Blade de nombre name."""
    ...


def GetGhostSectorSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetGhostSectorSound(string gsname)
    Devuelve el sonido ambiente perteneciente al sector fantasma de nombre gsname."""
    ...


def GetInputMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetInputMode(string device)
    Obtiene el modo del dispositivo device."""
    ...


def GetLastPlayerCType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetLastPlayerCType()"""
    ...


def GetMaterial(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetMaterial(int n)
     Crea un objeto Python que referencia al material Blade de índice n.
    GetMaterial(string name)
     Crea un objeto Python que referencia al material Blade de nombre name."""
    ...


def GetMenuTgapFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetMenuTgapFunc()
    Devuelve ....."""
    ...


def GetModelPos(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetModelPos(string Person)
    Devuelve la posicion del modelo 3D del Person especificado"""
    ...


def GetMouseState(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetMouseState()
    retorna invert,xsens,ysens"""
    ...


def GetMusicEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetMusicEvent(lpszEventName)"""
    ...


def GetMusicEventPriority(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ """
    ...


def GetMusicVolume(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """float GetMusicVolume()
    Obtiene el volumen de la musica."""
    ...


def GetMutilationLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetMutilationLevel()
    Obtiene el nivel de mutilaciones."""
    ...


def GetNewExclusionGroupId(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetNewExclusionGroupId()(void)
    Devuelve un nuevo y unico identificador para los grupos de exclusion."""
    ...


def GetObjectEntitiesVisibleFrom(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """tuple GetObjectEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""
    ...


def GetPTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetPTime()
    real timer"""
    ...


def GetParticleGType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Preguntar a Angel"""
    ...


def GetParticleGVal(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Preguntar a Angel"""
    ...


def GetProgramId(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetProgramId()
    Devuelve identificador de la aplicación.
    (HWND en Windows)"""
    ...


def GetRootWidget(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetRootWidget(widget w)
    Establece el Widget raiz."""
    ...


def GetSSQuality(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Undoc(0-2)"""
    ...


def GetSaveInfo(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetSaveInfo(void)
    Obtiene información de estado."""
    ...


def GetScheduledFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """(func,arg,name,time) GetScheduledFunc(int index)
    Devuelve una tupla con la función, los argumentos, el nombre y cuando se ejecuta."""
    ...


def GetScreenRect(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def GetScreenXY(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def GetSector(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetSector(int n)
     Crea un sector de Python que referencia al sector Blade de índice n.
    GetSector(double x,double y,double z)
     Crea un sector de Python que referencia al sector Blade que contiene al punto (x,y,z).
    """
    ...


def GetSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetSound(name)"""
    ...


def GetSoundFileName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetSoundFileName(int idx)
    Devuelve el archivo del sonido idx."""
    ...


def GetSoundName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetSoundName(int idx)
    Devuelve el nombre del sonido idx."""
    ...


def GetSoundVolume(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """float GetSoundVolume()
    Obtiene el volumen del sistema de sonido."""
    ...


def GetSpeakerConfig(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Undoc(0-3)"""
    ...


def GetStringValue(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetStringValue(string variable)
    Devuelve el valor de variable, None si no esta definida."""
    ...


def GetTextWH(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def GetTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """float GetTime(void)
    Devuelve el tiempo del juego en segundos."""
    ...


def GetTimeActionHeld(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""
    ...


def GetTimeSpeed(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """float GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""
    ...


def GetTimerInfo(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """(name,period) GetTimerInfo(int iTimer)
    Devuelve información sobre el timer de índice iTimer."""
    ...


def GetTrailType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTrailType(esteraCorta)
    Crea un TrailType , o tipo de estelas."""
    ...


def GetTriggerSectorData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTriggerSectorFunc(string TriggerSectorName)
    Devuelve el objeto Python asociado al campo Data del triggersector TriggerSectorName.
    """
    ...


def GetTriggerSectorFloorHeight(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """GetTriggerSectorFloorHeight(string TriggerSectorName)
    Devuelve la altura del suelo asociada al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Devuelve la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """
    ...


def GetTriggerSectorGroup(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTriggerSectorGroup(string TriggerSectorName)
    Devuelve el grupo asociado al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetTriggerSectorName(int idx)
    Devuelve el triggersector de índice idx, None si no existe."""
    ...


def GetTriggerSectorPoints(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTriggerSectorPoints(string TriggerSectorName)
    Devuelve los puntos asociados al trigersector TriggerSectorName."""
    ...


def GetTriggerSectorRoofHeight(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """GetTriggerSectorRoofHeight(string TriggerSectorName)
    Devuelve la altura del techo asociada al trigersector TriggerSectorName."""
    ...


def GetWeaponCombos(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """tuple GetWeaponCombos(blah blah BLAH!)"""
    ...


def GetWindowId(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetWindowId()
    Devuelve identificador de la ventana de la aplicación.
    (HWND en Windows)"""
    ...


def GetWorldFileName(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """string GetWorldFileName()
    Obtiene el nombre del archivo del que se ha cargado el mundo actual."""
    ...


def GetnAfterFrameFuncs(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetnAfterFrameFuncs()
    Devuelve el nº de funciones AfterFrame en el sistema."""
    ...


def GetnParticleGType(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetnParticleGType(void)
    Devuelve el nº de tipos de partículas."""
    ...


def GetnScheduledFuncs(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetnScheduledFuncs(void)
    Devuelve el nº de funciones diferidas."""
    ...


def GetnTimers(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int GetnTimers(void)
    Devuelve el número de timers del sistema."""
    ...


def GiveAnims(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GiveAnims(race_name). Da las anims de la raza en cuestion"""
    ...


def GoToTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetClockTime(float time)
    Establece el tiempo del juego en segundos...."""
    ...


def HeapCheckAllAllocations(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """HeapCheckAllAllocations(integer)
    Sets the Heap Checking to be performed on every allocation.  Functions only in debug.
    """
    ...


def HeapCheckDelayFree(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """HeapCheckDelayFree(integer)
    Simulates low memory conditions by delaying freeing until program termination.  Functions only in debug.
    """
    ...


def HeapCheckLeaks(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """HeapCheckSystemMemory(integer)
    Enables leak checking on program termination.  Functions only in debug."""
    ...


def HeapCheckSetMark(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """HeapCheckSetMark()
    Sets a memory checkpoint.  Reterns current bytes allocated. Only working in DEBUG"""
    ...


def HeapCheckSystemMemory(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """HeapCheckSystemMemory(integer)
    Includes memory used in runtime libraries for checking.  Functions only in debug."""
    ...


def Input(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Input(string texto)
    Crea una ventana de introducción de datos."""
    ...


def InsideActionArea(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """InsideActionArea(int AA,double x,double y,double z)
    ....blah blah !"""
    ...


def KillMusic(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """KillMusic ()
    Guess...;) .n"""
    ...


def LoadAnmRaceData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool LoadAnmRaceData(string filename,string race)
    Carga las animaciones de la raza en el archivo filename."""
    ...


def LoadAnmSoundData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool LoadAnmSoundData(string filename,string race)
    Carga la información de sonido de las animaciones de la raza en el archivo filename.
    """
    ...


def LoadCombustionData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool LoadCombustionData(string filename)
    Carga los datos de los combustion data del archivo filename."""
    ...


def LoadEntitiesData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool LoadEntitiesData(string filename)
    Carga los datos de las entidades del archivo filename."""
    ...


def LoadLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """LoadLevel(string dir_name)
    Lee de disco el nivel en el directorio dir_name."""
    ...


def LoadMusicState(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """loadMusicState(filename)"""
    ...


def LoadParticleSystemsData(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """bool LoadParticleSystemsData(string filename)
    Carga los datos de los sistemas de partículas del archivo filename."""
    ...


def LoadSampledAnimation(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """LoadSampledAnm(str File,str InternalName,int Type)"""
    ...


def LoadSoundDataBase(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """loadSoundDataBase(filename)"""
    ...


def LoadWorld(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """LoadWorld(string filename)
    Lee de disco el mapa (.bw) de nombre filename."""
    ...


def OpenDebugChannel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool OpenDebugChannel(string channel_name)
    Abre el canal de depuración de nombre channel_name."""
    ...


def OpenProfileSection(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool OpenProfileSection(int section[,string comment])
    Tiene que estar activado el profiler interno.
    Abre la sección i."""
    ...


def PauseSoundSystem(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """PauseSoundSystem ()
    Guess...;) .n"""
    ...


def PauseSoundSystemButMusic(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """PauseSoundSystemButMusic ()
    Idem than pauseSoundSystem BUt with muzic ."""
    ...


def PerformHeapCheck(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """PerformHeapCheck()
    Performs an integrity check on the heap now.  Integrity assertion only working in DEBUG
    """
    ...


def PlaySound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """PlaySound(int i,double x,double y,double z)
    Reproduce el sonido i en la posición (x,y,z)."""
    ...


def Quit(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool Quit()
    Termina el programa."""
    ...


def ReadAlphaBitMap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ReadAlphaBitMap(string file_name,string internal_name)
    Lee de disco una textura alpha."""
    ...


def ReadBitMap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ReadBitMap(string file_name,string internal_name)
    Lee de disco una textura."""
    ...


def ReadLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ReadLevel(string filename)
    Lee de disco el nivel (.lvl) filename."""
    ...


def ReassignCombustionData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool ReassignCombustionData(void)
    Reasigna los datos de los combustion data del archivo filename."""
    ...


def RemoveAfterFrameFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame del sistema de nombre name."""
    ...


def RemoveBipedAction(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def RemoveBoundFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """RemoveBoundFunc(string key,proc)
     Quita el procedimiento pr del suceso key.
    RemoveBoundFunc(string key,string predproc)
     Quita el procedimiento predefinifo predproc  del suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """
    ...


def RemoveInputAction(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """RemoveInputAction(string action_name)
    Quita una acción existente."""
    ...


def RemoveScheduledFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """RemoveScheduledFunc(atring FuncName)
    Removes a previously named sceduled function.  Removes first func found with this name.
    """
    ...


def RemoveTriggerSectorFunc(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """RemoveTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Desvincula la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """
    ...


def RestartTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """RestartTime(void)
    Reinicia el tiempo del juego."""
    ...


def ResumeSoundSystem(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ResumeSoundSystem ()
    Guess...;) .n"""
    ...


def SaveAnmRaceData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SaveAnmRaceData(string filename,string race)
    Guarda las animaciones de la raza race en el archivo filename."""
    ...


def SaveAnmSoundData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SaveAnmSoundData(string filename,string race)
    Guarda información de sonido de las animaciones de la raza race en el archivo filename.
    """
    ...


def SaveCombustionData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SaveCombustionData(string filename)
    Guarda los datos de los combustion  data en el archivo filename."""
    ...


def SaveEntitiesData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SaveEntitiesData(string filename)
    Guarda los datos de las entidades en el archivo filename."""
    ...


def SaveMusicState(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """saveMusicState(filename)"""
    ...


def SaveParticleSystemsData(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """bool SaveParticleSystemsData(string filename)
    Guarda los datos de los sistemas de partículas en el archivo filename."""
    ...


def SaveProfileData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SaveProfileData(string filename)
    Tiene que estar activado el profiler interno.
    Guarda información de los tiempos de las secciones activas en el archivo filename.
    """
    ...


def SaveSSConfig(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Undoc"""
    ...


def SaveScreenShot(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SaveScreenShot(filename,width,height)
    Acaso necesita descripcion?"""
    ...


def SaveSoundDataBase(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """saveSoundDataBase(filename)"""
    ...


def SaveStats(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Save statistics"""
    ...


def SetActionCameraMovement(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """SetActionCameraMovement(char* action_name,double angle,double start_pos,double end_pos)
    Interpolates the camera in the given action , the given angle in the given gap"""
    ...


def SetActionEventTable(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def SetAecGap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetAutoEngageCombat(double aec_gap)
    Establece tiempo auto encaramiento."""
    ...


def SetAfterFrameFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetAfterFrameFunc(name,function)
    Sets a function referenced with name that is going to be called at the end of each frame.
    """
    ...


def SetAnimationFactor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetAnimationFactor(string mov , float new_speed_factor )
    Cambia la velocidad del movimiento dado ."""
    ...


def SetAppMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetAppMode(string mode)
    Establece el modo de la aplicación (Game, Menu,...)."""
    ...


def SetAutoEngageCombat(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetAutoEngageCombat(bool auto)
    Establece si se encara automaticamente los enemigos."""
    ...


def SetAutoGenTexture(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetAutoGenTexture (string TexturName , integer TextEfecct )
    A la texture con dicho nombre se le aplica el efecto dado ."""
    ...


def SetBloodLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetBloodLevel(int level)
    Establece el nivel de sangre."""
    ...


def SetCallCheck(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetCallCheck(int check)
     Activa/desactiva la comprobación de errores de Python en las llamadas que hace Blade.
    Devuelve el estado anterior"""
    ...


def SetCombos(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetCombos(tuple combos)"""
    ...


def SetCurrentMap(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetCurrentMap(string dir_map)
    Establece el directorio de mapa actual."""
    ...


def SetDefaultMass(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetDefaultMass(string entity_kind,double mass)
    Establece la masa mass predefinida para las nuevas entidades de tipo kind."""
    ...


def SetDefaultMaterial(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetDefaultMaterial(string entity_kind,double material)
    Establece el material predefinido para las nuevas entidades de tipo kind."""
    ...


def SetDrawObjectShadows(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetDrawObjectShadows(bool draw)
    Establece si se deben dibujar las sombras de los objetos/personajes."""
    ...


def SetEAX(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetEAX(integer eax_flag)
    Establece la distorsion eax indicada."""
    ...


def SetEAXOverride(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetEAXOverride(0/1)"""
    ...


def SetEventTableFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def SetEventTableFuncC(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def SetGhostSectorGroupSound(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """SetGhostSectorGroupSound(string GroupName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double Scale)
    Establece el sonido del archivo filename al grupo de sectores fantasma GhostName."""
    ...


def SetGhostSectorSound(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetGhostSectorSound(string GhostName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double vMaxDist,double Scale)
    Establece el sonido del archivo filename al sector fantasma GhostName."""
    ...


def SetInputMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetInputMode(string device,string mode)
    Establece el modo del dispositivo device."""
    ...


def SetListenerPosition(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetListenerPosition(int modo[,double x,double y,double z])
    Cambia posicion o modo del oyente.
    mode : 0 - Punto en el mapa
           1 - Personaje
           2 - Cámara"""
    ...


def SetMenuTgapFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetMenuTgapFunc(function)
    Sets a function blah blah blah..."""
    ...


def SetMouseState(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetMouseState(invert,xsens,ysens)"""
    ...


def SetMusicVolume(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetMusicVolume (float factor)
    Guess...;) .n"""
    ...


def SetMutilationLevel(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetMutilationLevel(int level)
    Establece el nivel de mutilaciones."""
    ...


def SetParticleGVal(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def SetRootWidget(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetRootWidget(widget w)
    Establece el Widget raiz."""
    ...


def SetRunString(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """void SetRunString(string variable)
    Ejecuta la cadena de caracteres variable."""
    ...


def SetSS2dChannels(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSS2dChannels (int num_ch)
    Tells the sound system the number of 2d channels ."""
    ...


def SetSS3dChannels(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSS3dChannels (int num_ch)
    Tells the sound system the number of 3d channels ."""
    ...


def SetSSFilter(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSSFilter (bool)
    Tells the sound system to filter the output or not ."""
    ...


def SetSSFrecuency(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSSFrecuency (int frec)
    Tells the sound system the base frecuency to use ."""
    ...


def SetSSQuality(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Undoc(0-2)"""
    ...


def SetSaveInfo(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int SetSaveInfo(tuple info)
    Establece información de estado."""
    ...


def SetSolidMask(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def SetSoundVolume(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSoundVolume(double Volume)
    Establece el volumen del sistema de sonido."""
    ...


def SetSpeakerConfig(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Undoc(0-3)"""
    ...


def SetStringValue(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetStringValue(string variable,string value)
    Guarda la cadena de caracteres value cobn el nombre variable."""
    ...


def SetSun(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetSun(int exists,double x,double y,double z)
    Establece la posicion del sol mediante la direccion de la luz exterior. exists indica si se dibuja (1) o no (0)
    """
    ...


def SetTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool SetTime(float time)
    Establece el tiempo del juego en segundos."""
    ...


def SetTimeSpeed(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""
    ...


def SetTriggerSectorData(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetTriggerSectorData(string TriggerSectorName,Data)
    Asigna el objeto Python Data al campo Data del triggersector TriggerSectorName."""
    ...


def SetTriggerSectorFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetTriggerSectorFunc(string TriggerSectorName,string FuncType,Func)
    Asigna la funcion Func al evento FuncType del triggersector TriggerSectorName."""
    ...


def SetTurnSpeed(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SetTurnSpeed(string name_raza,float new_speed )
    Cambia la velocidad de giro de una raza . En radianes."""
    ...


def ShowActionAreas(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def ShowSounds(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ShowSounds(int sh)
    Establece si se debe mostrar un objeto para indicar donde estan los sonido ambiente.
    """
    ...


def ShutDownSoundChannels(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """ShutDownSoundChannels ()
    Guess...;) .n"""
    ...


def SoundSystemActive(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """SoundSystemActive ()
    Tells if the sound system if active or not ."""
    ...


def StartProfile(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """bool StartProfile(void)
    Tiene que estar activado el profiler interno.
    Reinicia sesión."""
    ...


def StopTime(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """StopTime(void)
    Detiene el tiempo del juego."""
    ...


def TakeSnapShot(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """Takes a snapshot"""
    ...


def UnBindAll(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """UnBindAll()
    Borra la configuración de teclado."""
    ...


def WriteText(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """"""
    ...


def YSSInfo(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """YSSInfo()"""
    ...


def nEntities(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int nEntities(void)
    Devuelve el nº de entidades en el mapa."""
    ...


def nMaterials(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """nMaterials(void)
    Devuelve el nº de materiales."""
    ...


def nSectors(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int nEntities(void)
    Devuelve el nº de sectors en el mapa."""
    ...


def nSounds(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int nSounds(void)
    Devuelve el nº de sonidos en el mapa."""
    ...


def nTriggerSectors(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """int nTriggerSectors(void)
    Desvincula el número de triggersectors en el mapa."""
    ...


#########
# reissue


def ApplyVideoSettings(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool ApplyVideoSettings()
    Apply changed video settings"""
    ...


def FakeInputAction(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    FakeInput(string action_name)"""
    ...


def GetActiveControllerType(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """*reissue only*
    GetActiveControllerType()"""
    ...


def GetActiveMonitor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int GetActiveMonitor()
    Get active monitor"""
    ...


def GetAntialiasing(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetAntialiasing()
     Get antialiasing"""
    ...


def GetAspectRatio(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int GetAspectRatio()
    Get aspect ratio"""
    ...


def GetFieldOfView(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetFieldOfView()
     Get field of view"""
    ...


def GetHideUI(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetHideUI()
     Get Hide UI"""
    ...


def GetLastUsedController(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    GetLastUsedController()"""
    ...


def GetLimitFps(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*"""
    ...


def GetNumMonitor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int GetNumMonitor()
    Get number of available monitor"""
    ...


def GetPlayIntro(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetPlayIntro()
    Devuelve true si se encara automaticanmente si se puede."""
    ...


def GetResolution(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    string GetResolution()
    Get window resolution"""
    ...


def GetReworkedCamera(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetReworkedCamera()
    Use a new non stuttering camera"""
    ...


def GetScreenMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int GetScreenMode()
    Get if window is in fullscreen mode"""
    ...


def GetSubtitlesEnable(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetSubtitlesEnable()
     Get usability of subtitles"""
    ...


def GetSupportedResolution(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetSupportedResolution()
    Get all supported window resolution"""
    ...


def GetUIScaleFactor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int GetUIScaleFactor()
     Get UI Scale Factor"""
    ...


def GetUpperCaseRussian(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    GetUpperCaseRussian(string word)"""
    ...


def GetVerticalSync(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetVerticalSync()
    get vertical sync"""
    ...


def GetVibration(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool GetVibration()
    get vibration"""
    ...


def IsRunningOnHandheldDevice(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """*reissue only*
    IsRunningOnHandheldDevice()
    Returns true if running on a handheld device."""
    ...


def IsUseMsgActive(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool IsUseMsgActive()
    Is Use active this frame"""
    ...


def PlayHaptic(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    PlayHaptic(hapticValue)"""
    ...


def SetActiveMonitor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int SetActiveMonitor(int active_monitor)
    Set active monitor"""
    ...


def SetAntialiasing(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetAntialiasing(bool antialiasing)
     Set antialiasing"""
    ...


def SetAspectRatio(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int SetAspectRatio(char* aspect_ratio)
    set aspect ratio"""
    ...


def SetFieldOfView(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetFieldOfView(float field_of_view)
     Set field of view"""
    ...


def SetGamepadChangeFunc(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetGamepadChangeFunc(controllerType,function)"""
    ...


def SetGamepadDisconnectFunc(
    *args: __bt.Unknown, **kwargs: __bt.Unknown
) -> __bt.Unknown:
    """*reissue only*
    SetGamepadDisconnectFunc(isDisconnect,function)"""
    ...


def SetHideUI(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetHideUI(float field_of_view)
     Hide UI"""
    ...


def SetLimitFps(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*"""
    ...


def SetMessageWidget(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetMessageWidget(widget w)
     Establece el Widget raiz."""
    ...


def SetPlayIntro(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool SetPlayIntro(bool auto)
    Establece si se encara automaticamente los enemigos."""
    ...


def SetResolution(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool SetResolution(int width, int height)
    Set screen resolution"""
    ...


def SetReworkedCamera(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool SetReworkedCamera(bool reworked)
    Set reworked camera"""
    ...


def SetScreenMode(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool SetScreenMode(bool windowed)
    Set screen mode"""
    ...


def SetSubtitlesEnable(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetSubtitlesEnable(bool subtitles_enable)
     Set usability of subtitles"""
    ...


def SetUIScaleFactor(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    SetUIScaleFactor(int v)
     Set UI Scale Factor"""
    ...


def SetVerticalSync(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    int SetVerticalSync()
    Set vertical sync"""
    ...


def SetVibration(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool SetVibration(bool reworked)
    Set vibration"""
    ...


def ShowCriticalWarning(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    ShowCriticalWarning(string title,string msg)"""
    ...


def TriggerEvent(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    TriggerEvent(string event_name)
    Pass the index of the achievement to be activated."""
    ...


def TriggerEventInner(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    TriggerEventInner()
    Tries to unlock complete game as (id=50..53)."""
    ...


def TurnAround(*args: __bt.Unknown, **kwargs: __bt.Unknown) -> __bt.Unknown:
    """*reissue only*
    bool TurnAround()
    Turn around"""
    ...
