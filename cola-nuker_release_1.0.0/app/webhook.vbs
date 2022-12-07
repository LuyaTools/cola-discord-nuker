filen=InputBox ("Webhook URL", "COLA NUKER", "https://...")
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("app\webhook.url.txt",2,true)
objFileToWrite.WriteLine(filen)
objFileToWrite.Close
Set objFileToWrite = Nothing
filen=InputBox ("Message", "COLA NUKER", "message here")
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("app\webhook.txt.txt",2,true)
objFileToWrite.WriteLine(filen)
objFileToWrite.Close
Set objFileToWrite = Nothing

