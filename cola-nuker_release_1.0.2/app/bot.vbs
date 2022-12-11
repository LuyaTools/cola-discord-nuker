filen=InputBox ("Bot Token", "COLA NUKER", "...")
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("app\token.txt",2,true)
objFileToWrite.WriteLine(filen)
objFileToWrite.Close
Set objFileToWrite = Nothing