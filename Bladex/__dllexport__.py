# 09 2023 sryml
import __sub__.entity as __entity

import typing as __t


def ActivateInput():
    """ActivateInput()
    Reactivate the input for the main player."""


def AddActionStepSound():
    """AddActionStepSound(table,action,step_sound_table)"""


def AddAnimFlags():
    """AddAnimFlags(string,wuea,mdf_y,solf,copy_rot,bng_mov,head_f)"""


def AddAnmEvent():
    """AnmAddEvent(anm_name,event_name,event_frame)"""


def AddAnmLRelease():
    """"""


def AddAnmLStep():
    """"""


def AddAnmRRelease():
    """"""


def AddAnmRStep():
    """"""


def AddBipedAction():
    """"""


def AddBoundFunc():
    """AddBoundFunc(string key,proc)
     Asigna el procedimiento pr al suceso key.
    AddBoundFunc(string key,string predproc)
     Asigna el procedimiento predefinifo predproc  al suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """


def AddCombustionDataFor():
    """AddCombustionDataFor(object_kind,upper_treshol,lower_treshold,flame_height,flame_size,speed,livetime)"""


def AddFloorCTolerance():
    """AddFloorCTolerance(anm_name,float)"""


def AddGhostSector():
    """AddGhostSector(string GhostName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""


def AddInputAction():
    """AddInputAction(string action_name,int npi)
    Crea una acción nueva."""


def AddMaterialStepSound():
    """AddMaterialStepSound(table,material,step_sound)"""


def AddMusicEventADPCM():
    """AddMusicEventADPCM( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""


def AddMusicEventCD():
    """AddMusicEventCD(lpszEventName, iTrack, dFIn, dFOut, fVolume, fPriority, bBackGround, iNext)"""


def AddMusicEventMP3():
    """AddMusicEventMP3( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext )"""


def AddMusicEventWAV():
    """AddMusicEventWAV( lpszEventName, lpszFile, dFIn, fVolume, dFOut, fPriority, bBackGround, iNext, [opened])"""


def AddParticleGType():
    """"""


def AddScheduledFunc():
    """AddScheduledFunc(double time,Func,Args)
    Llama a la funcion Func con los argumentos Args en el tiempo time"""


def AddStepSound():
    """AddStepSound(name,sound)"""


def AddStopTests():
    """AnmStopTests(anm_name)"""


def AddTextureMaterial():
    """AddTextureMaterial(texture,material)"""


def AddTranTime():
    """AddTranTime (string biped_name,string next_anm , string prev_anm , double time )
    Al pasar de animacion prev_anm a next_anm la transicion dura t segs . 0 si no transicion .
    """


def AddTriggerSector():
    """AddTriggerSector(string TriggerSectorName,string GroupName,float FloorHeight,float RoofHeight,List points)
    Crea."""


def AddWatchAnim():
    """AddWatchAnim(string)
     Establece esa animacion como una de las incluidas en modo watch.
    NOTA : NO es ejecutada por defecto por ningun personaje , para eso hay otra funcion !.
    """


def AnmAddEvent():
    """AnmAddEvent(anm_name,event_name,event_frame)
    Declara en la animacion de nombre anm_name un evento de nombre event_name en el frame event_frame
    """


def AnmClearEvents():
    """AnmClearEvents(anm_name)
    Borra en la animacion de nombre anm_name todos los eventos"""


def AnmDelEvent():
    """AnmDelEvent(anm_name,event_name)
    Borra en la animacion de nombre anm_name el evento de nombre event_name"""


def AnmGetEventFrame():
    """AnmGetEventFrame(anm_name,event_name)
    Devuelve en la animacion de nombre anm_name frame del evento de nombre event_name y si no existe devuelve -1
    """


def AnmTypeLSteps():
    """"""


def AnmTypeRSteps():
    """"""


def AssocKey():
    """bool AssocKey(string action,string input_device,string key[,int press])
    Asocia la acción action con la tecla key del dispositivo input_device"""


def BeginLoadGame():
    """void BeginLoadGame()
    Indica a la engine que se va a cargar una partida grabada para que pueda ajustar parámetros.
    """


def Bind2():
    """Bind2(void)
    Associate a combination of 2 Actions keys to a new Action, time window settings."""


def BodInspector():
    """BodInspector()"""


def CDCallBack():
    """int CDCallBack(func f)
    Establece la función CD."""


def CDLenght():
    """int CDLenght()
    Devuelve la duración del CD en milisegundos."""


def CDPause():
    """int CDPause()
    Detiene el CD."""


def CDPlayTrack():
    """PlayCDTrack(int ntrack)
    Reproduce la pista ntrack del CD.
    Si ntrack==1 reproduce todo el CD."""


def CDPresent():
    """int CDPresent()
    Indica si está el CD."""


def CDStop():
    """int CDStop()
    Detiene el CD."""


def CDTrackLenght():
    """CDTrackLenght(int ntrack)
    Devuelve la duración en milisegundos de la pista ntrack."""


def CDnTracks():
    """int nCDTracks()
    Devuelve el número de pistas del CD."""


def CheckAnims():
    """Gives a report of anims not assigned"""


def CheckPyErrors():
    """returns whether a python error has occured."""


def CleanArea():
    """CleanArea(x,y,z,distance)
      Limpia una zona esferica con centro en 'x,y,z'
    y distancia 'distance' de sangre."""


def CloseDebugChannel():
    """bool CloseDebugChannel(string channel_name)
    Cierra el canal de depuración de nombre channel_name."""


def CloseLevel():
    """CloseLevel([string statement])
    Cierra el nivel actual y ejecuta la instrucción statement."""


def CloseProfileSection():
    """bool CloseProfileSection(int section)
    Tiene que estar activado el profiler interno.
    Cierra la sección i."""


def CreateBipedData():
    """"""


def CreateDFCAnimation():
    """CreateDFCAnmimation(str File1,str File2,str InternalName,int n_armonics)"""


def CreateEntity(
    name: str,
    kind: str,
    x: float,
    y: float,
    z: float,
    parent_class: str = "",
    unknown: str = "",
) -> __entity.B_PyEntity:
    """CreateEntity(string name,string kind,double x,double y,double z)
    Crea una entidad nueva."""
    return __entity.B_PyEntity()


def CreateFCAnimation():
    """CreateFCAnmimation(str File,str InternalName,int n_armonics)"""


def CreateMaterial():
    """CreateMaterial(string name)
    Crea un nuevo material con nombre name."""


def CreateRoute():
    """CreateRoute()
    Crea una ruta vacía nueva."""


def CreateSound():
    """CreateSound(string filename,string soundname)
    Crea un sonido a partir del filename y con nombre name."""


def CreateSpark():
    """CreateSpark(string name,double x,double y,double z,)
    Crea un efecto de chispas."""


def CreateTimer():
    """CreateTimer(string TimerName,double period)
    Crea un Timer de nombre TimerName con periodo period."""


def DeactivateInput():
    """DeactivateInput()
    Disabled the input for the main player."""


def DeleteEntity():
    """DeleteEntity(string name/object entity)
    Delete existing object.  Use with care.  Subscribe to Pin if unsure."""


def DeleteStringValue():
    """string DeleteStringValue(string variable)
    Elimina variable."""


def DisableProfiler():
    """bool DisableProfiler(void)
    desactivar profiler interno."""


def DoneLoadGame():
    """void DoneLoadGame()
    Indica a la engine que se ha cargado una partida grabada para que pueda ajustar parámetros.
    """


def DrawBOD():
    """DrawBOD(string BODName,int x,int y,int ancho,int alto)
    Dibuja el BOD de nombre BODName en el rectángulo x,y,ancho,alto."""


def DumpMemoryLeaks():
    """bool DumpMemoryLeaks(string filename)
    Dumps cuurent memory allocations to filename."""


def EnableProfiler():
    """bool EnableProfiler(void)
    activar profiler interno."""


def ExeMusicEvent():
    """ """


def ExportWorld():
    """ExportWorld ()
    Export the world to owner Max format."""


def GenerateEntityName():
    """string GenerateEntityName()
    Generates a new and unique entity name."""


def GetAecGap():
    """bool GetAecGap()
    Devuelve tiempo de auto encaramientpo....."""


def GetAfterFrameFunc():
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame de nombre name."""


def GetAfterFrameFuncName():
    """string GetAfterFrameFuncName(int idx)
    Devuelve el nombre de la función AfterFrame del sistema de índice idx."""


def GetAnimationDuration():
    """GetAnimationDuration (string sampled animation name )
    Resturns the duration in seconds of the full animation disregarding interpolation.
    """


def GetAnmRaces():
    """list GetAnmRaces(void)
    Devuelve una lista con los nombres de las razas cargadas en memoria."""


def GetAppMode():
    """string GetAppMode()
    Obtiene el modo de la aplicación (Game, Menu,...)."""


def GetAutoEngageCombat():
    """bool GetAutoEngageCombat()
    Devuelve true si se encara automaticanmente si se puede."""


def GetBloodLevel():
    """int GetBloodLevel()
    Obtiene el nivel de sangre."""


def GetCharType():
    """GetCharType(Barbarian,Bar)
    Crea un CharType , o raza de personaje."""


def GetCombos():
    """tuple GetCombos(blah blah BLAH!)"""


def GetCommandLine():
    """string GetCommandLine()
    Obtiene la línea de órdenes que se ha pasado a la aplicación."""


def GetCurrentMap():
    """string GetCurrentMap()
    Devuelve el mapa actual."""


def GetDrawObjectShadows():
    """bool GetDrawObjectShadows()
    Devuelve si se dibujan las sombras de los objetos/personajes."""


def GetEAXOverride():
    """float GetEAXOverride()"""


def GetEnemiesVisibleFrom():
    """tuple GetEnemiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""


def GetEntitiesAt():
    """tuple GetEntitiesAt(double x,double y,double z,double radius)
    Obtiene las entidades que están en un radio radius de la posición (x,y,z)"""


def GetEntitiesVisibleFrom():
    """tuple GetEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""


def GetEntity(arg: __t.Union[str, int]) -> __entity.B_PyEntity:
    """GetEntity(int n)
     Crea una entidad de Python que referencia a la entidad Blade de índice n.
    GetEntity(string name)
     Crea una entidad de Python que referencia a la entidad Blade de nombre name."""
    return __entity.B_PyEntity()


def GetGhostSectorSound():
    """GetGhostSectorSound(string gsname)
    Devuelve el sonido ambiente perteneciente al sector fantasma de nombre gsname."""


def GetInputMode():
    """string GetInputMode(string device)
    Obtiene el modo del dispositivo device."""


def GetLastPlayerCType():
    """string GetLastPlayerCType()"""


def GetMaterial():
    """GetMaterial(int n)
     Crea un objeto Python que referencia al material Blade de índice n.
    GetMaterial(string name)
     Crea un objeto Python que referencia al material Blade de nombre name."""


def GetMenuTgapFunc():
    """GetMenuTgapFunc()
    Devuelve ....."""


def GetModelPos():
    """GetModelPos(string Person)
    Devuelve la posicion del modelo 3D del Person especificado"""


def GetMouseState():
    """GetMouseState()
    retorna invert,xsens,ysens"""


def GetMusicEvent():
    """GetMusicEvent(lpszEventName)"""


def GetMusicEventPriority():
    """ """


def GetMusicVolume():
    """float GetMusicVolume()
    Obtiene el volumen de la musica."""


def GetMutilationLevel():
    """int GetMutilationLevel()
    Obtiene el nivel de mutilaciones."""


def GetNewExclusionGroupId():
    """int GetNewExclusionGroupId()(void)
    Devuelve un nuevo y unico identificador para los grupos de exclusion."""


def GetObjectEntitiesVisibleFrom():
    """tuple GetObjectEntitiesVisibleFrom(tuple center,double radius,tuple direction,double angle)"""


def GetPTime():
    """GetPTime()
    real timer"""


def GetParticleGType():
    """Preguntar a Angel"""


def GetParticleGVal():
    """Preguntar a Angel"""


def GetProgramId():
    """int GetProgramId()
    Devuelve identificador de la aplicación.
    (HWND en Windows)"""


def GetRootWidget():
    """SetRootWidget(widget w)
    Establece el Widget raiz."""


def GetSSQuality():
    """Undoc(0-2)"""


def GetSaveInfo():
    """tuple GetSaveInfo(void)
    Obtiene información de estado."""


def GetScheduledFunc():
    """(func,arg,name,time) GetScheduledFunc(int index)
    Devuelve una tupla con la función, los argumentos, el nombre y cuando se ejecuta."""


def GetScreenRect():
    """"""


def GetScreenXY():
    """"""


def GetSector():
    """GetSector(int n)
     Crea un sector de Python que referencia al sector Blade de índice n.
    GetSector(double x,double y,double z)
     Crea un sector de Python que referencia al sector Blade que contiene al punto (x,y,z).
    """


def GetSound():
    """GetSound(name)"""


def GetSoundFileName():
    """string GetSoundFileName(int idx)
    Devuelve el archivo del sonido idx."""


def GetSoundName():
    """string GetSoundName(int idx)
    Devuelve el nombre del sonido idx."""


def GetSoundVolume():
    """float GetSoundVolume()
    Obtiene el volumen del sistema de sonido."""


def GetSpeakerConfig():
    """Undoc(0-3)"""


def GetStringValue():
    """string GetStringValue(string variable)
    Devuelve el valor de variable, None si no esta definida."""


def GetTextWH():
    """"""


def GetTime():
    """float GetTime(void)
    Devuelve el tiempo del juego en segundos."""


def GetTimeActionHeld():
    """Return the amount of milliseconds a key has been hald down, or zero if it is currently considered released"""


def GetTimeSpeed():
    """float GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""


def GetTimerInfo():
    """(name,period) GetTimerInfo(int iTimer)
    Devuelve información sobre el timer de índice iTimer."""


def GetTrailType():
    """GetTrailType(esteraCorta)
    Crea un TrailType , o tipo de estelas."""


def GetTriggerSectorData():
    """GetTriggerSectorFunc(string TriggerSectorName)
    Devuelve el objeto Python asociado al campo Data del triggersector TriggerSectorName.
    """


def GetTriggerSectorFloorHeight():
    """GetTriggerSectorFloorHeight(string TriggerSectorName)
    Devuelve la altura del suelo asociada al trigersector TriggerSectorName."""


def GetTriggerSectorFunc():
    """GetTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Devuelve la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """


def GetTriggerSectorGroup():
    """GetTriggerSectorGroup(string TriggerSectorName)
    Devuelve el grupo asociado al trigersector TriggerSectorName."""


def GetTriggerSectorName():
    """string GetTriggerSectorName(int idx)
    Devuelve el triggersector de índice idx, None si no existe."""


def GetTriggerSectorPoints():
    """GetTriggerSectorPoints(string TriggerSectorName)
    Devuelve los puntos asociados al trigersector TriggerSectorName."""


def GetTriggerSectorRoofHeight():
    """GetTriggerSectorRoofHeight(string TriggerSectorName)
    Devuelve la altura del techo asociada al trigersector TriggerSectorName."""


def GetWeaponCombos():
    """tuple GetWeaponCombos(blah blah BLAH!)"""


def GetWindowId():
    """int GetWindowId()
    Devuelve identificador de la ventana de la aplicación.
    (HWND en Windows)"""


def GetWorldFileName():
    """string GetWorldFileName()
    Obtiene el nombre del archivo del que se ha cargado el mundo actual."""


def GetnAfterFrameFuncs():
    """int GetnAfterFrameFuncs()
    Devuelve el nº de funciones AfterFrame en el sistema."""


def GetnParticleGType():
    """int GetnParticleGType(void)
    Devuelve el nº de tipos de partículas."""


def GetnScheduledFuncs():
    """int GetnScheduledFuncs(void)
    Devuelve el nº de funciones diferidas."""


def GetnTimers():
    """int GetnTimers(void)
    Devuelve el número de timers del sistema."""


def GiveAnims():
    """GiveAnims(race_name). Da las anims de la raza en cuestion"""


def GoToTime():
    """bool SetClockTime(float time)
    Establece el tiempo del juego en segundos...."""


def HeapCheckAllAllocations():
    """HeapCheckAllAllocations(integer)
    Sets the Heap Checking to be performed on every allocation.  Functions only in debug.
    """


def HeapCheckDelayFree():
    """HeapCheckDelayFree(integer)
    Simulates low memory conditions by delaying freeing until program termination.  Functions only in debug.
    """


def HeapCheckLeaks():
    """HeapCheckSystemMemory(integer)
    Enables leak checking on program termination.  Functions only in debug."""


def HeapCheckSetMark():
    """HeapCheckSetMark()
    Sets a memory checkpoint.  Reterns current bytes allocated. Only working in DEBUG"""


def HeapCheckSystemMemory():
    """HeapCheckSystemMemory(integer)
    Includes memory used in runtime libraries for checking.  Functions only in debug."""


def Input():
    """Input(string texto)
    Crea una ventana de introducción de datos."""


def InsideActionArea():
    """InsideActionArea(int AA,double x,double y,double z)
    ....blah blah !"""


def KillMusic():
    """KillMusic ()
    Guess...;) .n"""


def LoadAnmRaceData():
    """bool LoadAnmRaceData(string filename,string race)
    Carga las animaciones de la raza en el archivo filename."""


def LoadAnmSoundData():
    """bool LoadAnmSoundData(string filename,string race)
    Carga la información de sonido de las animaciones de la raza en el archivo filename.
    """


def LoadCombustionData():
    """bool LoadCombustionData(string filename)
    Carga los datos de los combustion data del archivo filename."""


def LoadEntitiesData():
    """bool LoadEntitiesData(string filename)
    Carga los datos de las entidades del archivo filename."""


def LoadLevel():
    """LoadLevel(string dir_name)
    Lee de disco el nivel en el directorio dir_name."""


def LoadMusicState():
    """loadMusicState(filename)"""


def LoadParticleSystemsData():
    """bool LoadParticleSystemsData(string filename)
    Carga los datos de los sistemas de partículas del archivo filename."""


def LoadSampledAnimation():
    """LoadSampledAnm(str File,str InternalName,int Type)"""


def LoadSoundDataBase():
    """loadSoundDataBase(filename)"""


def LoadWorld():
    """LoadWorld(string filename)
    Lee de disco el mapa (.bw) de nombre filename."""


def OpenDebugChannel():
    """bool OpenDebugChannel(string channel_name)
    Abre el canal de depuración de nombre channel_name."""


def OpenProfileSection():
    """bool OpenProfileSection(int section[,string comment])
    Tiene que estar activado el profiler interno.
    Abre la sección i."""


def PauseSoundSystem():
    """PauseSoundSystem ()
    Guess...;) .n"""


def PauseSoundSystemButMusic():
    """PauseSoundSystemButMusic ()
    Idem than pauseSoundSystem BUt with muzic ."""


def PerformHeapCheck():
    """PerformHeapCheck()
    Performs an integrity check on the heap now.  Integrity assertion only working in DEBUG
    """


def PlaySound():
    """PlaySound(int i,double x,double y,double z)
    Reproduce el sonido i en la posición (x,y,z)."""


def Quit():
    """bool Quit()
    Termina el programa."""


def ReadAlphaBitMap():
    """ReadAlphaBitMap(string file_name,string internal_name)
    Lee de disco una textura alpha."""


def ReadBitMap():
    """ReadBitMap(string file_name,string internal_name)
    Lee de disco una textura."""


def ReadLevel():
    """ReadLevel(string filename)
    Lee de disco el nivel (.lvl) filename."""


def ReassignCombustionData():
    """bool ReassignCombustionData(void)
    Reasigna los datos de los combustion data del archivo filename."""


def RemoveAfterFrameFunc():
    """GetAfterFrameFunc(name)
    Devuelve la función AfterFrame del sistema de nombre name."""


def RemoveBipedAction():
    """"""


def RemoveBoundFunc():
    """RemoveBoundFunc(string key,proc)
     Quita el procedimiento pr del suceso key.
    RemoveBoundFunc(string key,string predproc)
     Quita el procedimiento predefinifo predproc  del suceso key.
     predproc puede ser: Forward, Backwards, Up, Down, Left, Right, RotateLeft, RotateRight, RotateUp, RotateDown (más, preguntar a Jose)
    """


def RemoveInputAction():
    """RemoveInputAction(string action_name)
    Quita una acción existente."""


def RemoveScheduledFunc():
    """RemoveScheduledFunc(atring FuncName)
    Removes a previously named sceduled function.  Removes first func found with this name.
    """


def RemoveTriggerSectorFunc():
    """RemoveTriggerSectorFunc(string TriggerSectorName,string FuncType)
    Desvincula la funcion asociada al evento FuncType del triggersector TriggerSectorName.
    """


def RestartTime():
    """RestartTime(void)
    Reinicia el tiempo del juego."""


def ResumeSoundSystem():
    """ResumeSoundSystem ()
    Guess...;) .n"""


def SaveAnmRaceData():
    """bool SaveAnmRaceData(string filename,string race)
    Guarda las animaciones de la raza race en el archivo filename."""


def SaveAnmSoundData():
    """bool SaveAnmSoundData(string filename,string race)
    Guarda información de sonido de las animaciones de la raza race en el archivo filename.
    """


def SaveCombustionData():
    """bool SaveCombustionData(string filename)
    Guarda los datos de los combustion  data en el archivo filename."""


def SaveEntitiesData():
    """bool SaveEntitiesData(string filename)
    Guarda los datos de las entidades en el archivo filename."""


def SaveMusicState():
    """saveMusicState(filename)"""


def SaveParticleSystemsData():
    """bool SaveParticleSystemsData(string filename)
    Guarda los datos de los sistemas de partículas en el archivo filename."""


def SaveProfileData():
    """bool SaveProfileData(string filename)
    Tiene que estar activado el profiler interno.
    Guarda información de los tiempos de las secciones activas en el archivo filename.
    """


def SaveSSConfig():
    """Undoc"""


def SaveScreenShot():
    """SaveScreenShot(filename,width,height)
    Acaso necesita descripcion?"""


def SaveSoundDataBase():
    """saveSoundDataBase(filename)"""


def SaveStats():
    """Save statistics"""


def SetActionCameraMovement():
    """SetActionCameraMovement(char* action_name,double angle,double start_pos,double end_pos)
    Interpolates the camera in the given action , the given angle in the given gap"""


def SetActionEventTable():
    """"""


def SetAecGap():
    """bool SetAutoEngageCombat(double aec_gap)
    Establece tiempo auto encaramiento."""


def SetAfterFrameFunc():
    """SetAfterFrameFunc(name,function)
    Sets a function referenced with name that is going to be called at the end of each frame.
    """


def SetAnimationFactor():
    """SetAnimationFactor(string mov , float new_speed_factor )
    Cambia la velocidad del movimiento dado ."""


def SetAppMode():
    """bool SetAppMode(string mode)
    Establece el modo de la aplicación (Game, Menu,...)."""


def SetAutoEngageCombat():
    """bool SetAutoEngageCombat(bool auto)
    Establece si se encara automaticamente los enemigos."""


def SetAutoGenTexture():
    """SetAutoGenTexture (string TexturName , integer TextEfecct )
    A la texture con dicho nombre se le aplica el efecto dado ."""


def SetBloodLevel():
    """bool SetBloodLevel(int level)
    Establece el nivel de sangre."""


def SetCallCheck():
    """SetCallCheck(int check)
     Activa/desactiva la comprobación de errores de Python en las llamadas que hace Blade.
    Devuelve el estado anterior"""


def SetCombos():
    """bool SetCombos(tuple combos)"""


def SetCurrentMap():
    """bool SetCurrentMap(string dir_map)
    Establece el directorio de mapa actual."""


def SetDefaultMass():
    """SetDefaultMass(string entity_kind,double mass)
    Establece la masa mass predefinida para las nuevas entidades de tipo kind."""


def SetDefaultMaterial():
    """SetDefaultMaterial(string entity_kind,double material)
    Establece el material predefinido para las nuevas entidades de tipo kind."""


def SetDrawObjectShadows():
    """bool SetDrawObjectShadows(bool draw)
    Establece si se deben dibujar las sombras de los objetos/personajes."""


def SetEAX():
    """SetEAX(integer eax_flag)
    Establece la distorsion eax indicada."""


def SetEAXOverride():
    """SetEAXOverride(0/1)"""


def SetEventTableFunc():
    """"""


def SetEventTableFuncC():
    """"""


def SetGhostSectorGroupSound():
    """SetGhostSectorGroupSound(string GroupName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double Scale)
    Establece el sonido del archivo filename al grupo de sectores fantasma GhostName."""


def SetGhostSectorSound():
    """SetGhostSectorSound(string GhostName,string filename,double Volume,double BaseVolume,double MinDist,double MaxDist,double vMaxDist,double Scale)
    Establece el sonido del archivo filename al sector fantasma GhostName."""


def SetInputMode():
    """bool SetInputMode(string device,string mode)
    Establece el modo del dispositivo device."""


def SetListenerPosition():
    """SetListenerPosition(int modo[,double x,double y,double z])
    Cambia posicion o modo del oyente.
    mode : 0 - Punto en el mapa
           1 - Personaje
           2 - Cámara"""


def SetMenuTgapFunc():
    """SetMenuTgapFunc(function)
    Sets a function blah blah blah..."""


def SetMouseState():
    """SetMouseState(invert,xsens,ysens)"""


def SetMusicVolume():
    """SetMusicVolume (float factor)
    Guess...;) .n"""


def SetMutilationLevel():
    """bool SetMutilationLevel(int level)
    Establece el nivel de mutilaciones."""


def SetParticleGVal():
    """"""


def SetRootWidget():
    """SetRootWidget(widget w)
    Establece el Widget raiz."""


def SetRunString():
    """void SetRunString(string variable)
    Ejecuta la cadena de caracteres variable."""


def SetSS2dChannels():
    """SetSS2dChannels (int num_ch)
    Tells the sound system the number of 2d channels ."""


def SetSS3dChannels():
    """SetSS3dChannels (int num_ch)
    Tells the sound system the number of 3d channels ."""


def SetSSFilter():
    """SetSSFilter (bool)
    Tells the sound system to filter the output or not ."""


def SetSSFrecuency():
    """SetSSFrecuency (int frec)
    Tells the sound system the base frecuency to use ."""


def SetSSQuality():
    """Undoc(0-2)"""


def SetSaveInfo():
    """int SetSaveInfo(tuple info)
    Establece información de estado."""


def SetSolidMask():
    """"""


def SetSoundVolume():
    """SetSoundVolume(double Volume)
    Establece el volumen del sistema de sonido."""


def SetSpeakerConfig():
    """Undoc(0-3)"""


def SetStringValue():
    """bool SetStringValue(string variable,string value)
    Guarda la cadena de caracteres value cobn el nombre variable."""


def SetSun():
    """SetSun(int exists,double x,double y,double z)
    Establece la posicion del sol mediante la direccion de la luz exterior. exists indica si se dibuja (1) o no (0)
    """


def SetTime():
    """bool SetTime(float time)
    Establece el tiempo del juego en segundos."""


def SetTimeSpeed():
    """GetTimeSpeed(void)
    Devuelve la velocidad tiempo del juego."""


def SetTriggerSectorData():
    """SetTriggerSectorData(string TriggerSectorName,Data)
    Asigna el objeto Python Data al campo Data del triggersector TriggerSectorName."""


def SetTriggerSectorFunc():
    """SetTriggerSectorFunc(string TriggerSectorName,string FuncType,Func)
    Asigna la funcion Func al evento FuncType del triggersector TriggerSectorName."""


def SetTurnSpeed():
    """SetTurnSpeed(string name_raza,float new_speed )
    Cambia la velocidad de giro de una raza . En radianes."""


def ShowActionAreas():
    """"""


def ShowSounds():
    """ShowSounds(int sh)
    Establece si se debe mostrar un objeto para indicar donde estan los sonido ambiente.
    """


def ShutDownSoundChannels():
    """ShutDownSoundChannels ()
    Guess...;) .n"""


def SoundSystemActive():
    """SoundSystemActive ()
    Tells if the sound system if active or not ."""


def StartProfile():
    """bool StartProfile(void)
    Tiene que estar activado el profiler interno.
    Reinicia sesión."""


def StopTime():
    """StopTime(void)
    Detiene el tiempo del juego."""


def TakeSnapShot():
    """Takes a snapshot"""


def UnBindAll():
    """UnBindAll()
    Borra la configuración de teclado."""


def WriteText():
    """"""


def YSSInfo():
    """YSSInfo()"""


def nEntities():
    """int nEntities(void)
    Devuelve el nº de entidades en el mapa."""


def nMaterials():
    """nMaterials(void)
    Devuelve el nº de materiales."""


def nSectors():
    """int nEntities(void)
    Devuelve el nº de sectors en el mapa."""


def nSounds():
    """int nSounds(void)
    Devuelve el nº de sonidos en el mapa."""


def nTriggerSectors():
    """int nTriggerSectors(void)
    Desvincula el número de triggersectors en el mapa."""


########
######## reissue


def ApplyVideoSettings():
    """*reissue only*
    bool ApplyVideoSettings()
    Apply changed video settings"""


def FakeInputAction():
    """*reissue only*
    FakeInput(string action_name)"""


def GetActiveControllerType():
    """*reissue only*
    GetActiveControllerType()"""


def GetActiveMonitor():
    """*reissue only*
    int GetActiveMonitor()
    Get active monitor"""


def GetAntialiasing():
    """*reissue only*
    bool GetAntialiasing()
     Get antialiasing"""


def GetAspectRatio():
    """*reissue only*
    int GetAspectRatio()
    Get aspect ratio"""


def GetFieldOfView():
    """*reissue only*
    bool GetFieldOfView()
     Get field of view"""


def GetHideUI():
    """*reissue only*
    bool GetHideUI()
     Get Hide UI"""


def GetLastUsedController():
    """*reissue only*
    GetLastUsedController()"""


def GetLimitFps():
    """*reissue only*"""


def GetNumMonitor():
    """*reissue only*
    int GetNumMonitor()
    Get number of available monitor"""


def GetPlayIntro():
    """*reissue only*
    bool GetPlayIntro()
    Devuelve true si se encara automaticanmente si se puede."""


def GetResolution():
    """*reissue only*
    string GetResolution()
    Get window resolution"""


def GetReworkedCamera():
    """*reissue only*
    bool GetReworkedCamera()
    Use a new non stuttering camera"""


def GetScreenMode():
    """*reissue only*
    int GetScreenMode()
    Get if window is in fullscreen mode"""


def GetSubtitlesEnable():
    """*reissue only*
    bool GetSubtitlesEnable()
     Get usability of subtitles"""


def GetSupportedResolution():
    """*reissue only*
    bool GetSupportedResolution()
    Get all supported window resolution"""


def GetUIScaleFactor():
    """*reissue only*
    int GetUIScaleFactor()
     Get UI Scale Factor"""


def GetUpperCaseRussian():
    """*reissue only*
    GetUpperCaseRussian(string word)"""


def GetVerticalSync():
    """*reissue only*
    bool GetVerticalSync()
    get vertical sync"""


def GetVibration():
    """*reissue only*
    bool GetVibration()
    get vibration"""


def IsRunningOnHandheldDevice():
    """*reissue only*
    IsRunningOnHandheldDevice()
    Returns true if running on a handheld device."""


def IsUseMsgActive():
    """*reissue only*
    bool IsUseMsgActive()
    Is Use active this frame"""


def PlayHaptic():
    """*reissue only*
    PlayHaptic(hapticValue)"""


def SetActiveMonitor():
    """*reissue only*
    int SetActiveMonitor(int active_monitor)
    Set active monitor"""


def SetAntialiasing():
    """*reissue only*
    SetAntialiasing(bool antialiasing)
     Set antialiasing"""


def SetAspectRatio():
    """*reissue only*
    int SetAspectRatio(char* aspect_ratio)
    set aspect ratio"""


def SetFieldOfView():
    """*reissue only*
    SetFieldOfView(float field_of_view)
     Set field of view"""


def SetGamepadChangeFunc():
    """*reissue only*
    SetGamepadChangeFunc(controllerType,function)"""


def SetGamepadDisconnectFunc():
    """*reissue only*
    SetGamepadDisconnectFunc(isDisconnect,function)"""


def SetHideUI():
    """*reissue only*
    SetHideUI(float field_of_view)
     Hide UI"""


def SetLimitFps():
    """*reissue only*"""


def SetMessageWidget():
    """*reissue only*
    SetMessageWidget(widget w)
     Establece el Widget raiz."""


def SetPlayIntro():
    """*reissue only*
    bool SetPlayIntro(bool auto)
    Establece si se encara automaticamente los enemigos."""


def SetResolution():
    """*reissue only*
    bool SetResolution(int width, int height)
    Set screen resolution"""


def SetReworkedCamera():
    """*reissue only*
    bool SetReworkedCamera(bool reworked)
    Set reworked camera"""


def SetScreenMode():
    """*reissue only*
    bool SetScreenMode(bool windowed)
    Set screen mode"""


def SetSubtitlesEnable():
    """*reissue only*
    SetSubtitlesEnable(bool subtitles_enable)
     Set usability of subtitles"""


def SetUIScaleFactor():
    """*reissue only*
    SetUIScaleFactor(int v)
     Set UI Scale Factor"""


def SetVerticalSync():
    """*reissue only*
    int SetVerticalSync()
    Set vertical sync"""


def SetVibration():
    """*reissue only*
    bool SetVibration(bool reworked)
    Set vibration"""


def ShowCriticalWarning():
    """*reissue only*
    ShowCriticalWarning(string title,string msg)"""


def TriggerEvent():
    """*reissue only*
    TriggerEvent(string event_name)
    Pass the index of the achievement to be activated."""


def TriggerEventInner():
    """*reissue only*
    TriggerEventInner()
    Tries to unlock complete game as (id=50..53)."""


def TurnAround():
    """*reissue only*
    bool TurnAround()
    Turn around"""
