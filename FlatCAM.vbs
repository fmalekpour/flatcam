Set oShell = CreateObject ("Wscript.Shell") 
Dim strArgs
strArgs = "python-3.11.9.amd64\pythonw.exe flatcam-org\flatcam.py"
oShell.Run strArgs, 3, false
