filen=InputBox ("Enter Token to spy on!", "COLA NUKER", "token")
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("app\target.token.txt",2,true)
objFileToWrite.WriteLine(filen)
objFileToWrite.Close
Set objFileToWrite = Nothing