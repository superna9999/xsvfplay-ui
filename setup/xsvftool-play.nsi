
; The name of the installer
Name "XSVFPlayFPGATool"

; The file to write
OutFile "XSVFPlayFPGATool.exe"

; The default installation directory
InstallDir $PROGRAMFILES\XSVFPlayFPGATool

; Registry key to check for directory (so if you install again, it will 
; overwrite the old one automatically)
InstallDirRegKey HKLM "Software\XSVFPlayFPGATool" "Install_Dir"

; Request application privileges for Windows Vista
RequestExecutionLevel admin

;--------------------------------

; Pages

Page components
Page directory
Page instfiles

UninstPage uninstConfirm
UninstPage instfiles

;--------------------------------

; The stuff to install
Section "XSVFPlayFPGATool (required)"

  SectionIn RO
  
  ; Set output path to the installation directory.
  SetOutPath $INSTDIR
  
  ; Put file there
  File /r ..\dist\*.*
  
  ; Write the installation path into the registry
  WriteRegStr HKLM SOFTWARE\XSVFPlayFPGATool "Install_Dir" "$INSTDIR"
  
  ; Write the uninstall keys for Windows
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\XSVFPlayFPGATool" "DisplayName" "XSVFPlayFPGATool"
  WriteRegStr HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\XSVFPlayFPGATool" "UninstallString" '"$INSTDIR\uninstall.exe"'
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\XSVFPlayFPGATool" "NoModify" 1
  WriteRegDWORD HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\XSVFPlayFPGATool" "NoRepair" 1
  WriteUninstaller "uninstall.exe"
  
SectionEnd

; Optional section (can be disabled by the user)
Section "Start Menu Shortcuts"

  CreateDirectory "$SMPROGRAMS\XSVFPlayFPGATool"
  CreateShortCut "$SMPROGRAMS\XSVFPlayFPGATool\Uninstall.lnk" "$INSTDIR\uninstall.exe" "" "$INSTDIR\uninstall.exe" 0
  CreateShortCut "$SMPROGRAMS\XSVFPlayFPGATool\FPGA Programming Tool.lnk" "$INSTDIR\xsvfplay.exe" "" "$INSTDIR\xsvfplay.exe" 0
  
SectionEnd

;--------------------------------

; Uninstaller

Section "Uninstall"
  
  ; Remove registry keys
  DeleteRegKey HKLM "Software\Microsoft\Windows\CurrentVersion\Uninstall\XSVFPlayFPGATool"
  DeleteRegKey HKLM SOFTWARE\XSVFPlayFPGATool

  ; Remove directories used
  RMDir /r "$SMPROGRAMS\XSVFPlayFPGATool"
  RMDir /r "$INSTDIR"

SectionEnd
