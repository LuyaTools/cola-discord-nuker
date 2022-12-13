filen=InputBox ("Webhook URL", "COLA NUKER", "https://...")
Set objFileToWrite = CreateObject("Scripting.FileSystemObject").OpenTextFile("app\webhook.url2.txt",2,true)
objFileToWrite.WriteLine(filen)
objFileToWrite.Close
Set objFileToWrite = Nothing
