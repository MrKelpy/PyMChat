# Please refer to [PythMC](https://github.com/MrKelpy/PythMC) instead. It's a more complete, clean and intuitive library made by me, to replace MESL and PyMChat. PyMChat will not be continued or any given any support.

## Installation
```bash
pip install pymchat
```

## Usage

### Reading chat messages
```python
from pymchat.chat import Chat

chat = Chat()

# Limit in get_history is defaulted to 50**50.
message_list = chat.get_history(limit=10)

for message in message_list:
  print(message.content)
```

This sample output was taken from a real server.
```bash
[+] JohnRockefailure has joined
[+] Senseimasterman9 has joined
Welcome | Steve | Senseimasterman9 to the server!
<| Investor | *Blist> Welcom
<| Griffin | *Jay> W e l c o m e ! E n j o y y o u r s t a y a t S a f e S u r v i v a l
<| Event Staff | *Enelis> o-o
<| Griffin | *Jay> oof
<| Veteran | Parkemon20000> thats... not normal
[-] JohnRockefailure has left
<| Phoenix | *Kelp> Gn all
```
### Sending chat messages
```python
from pymchat.chat import Chat

chat = Chat()
message_list = chat.send("This is a sample message!")
```
Using this method will briefly attempt to locate a Minecraft Window, open the chat, send the message, and then switch back to the previous active window.
A MinecraftWindowNotFoundError will be thrown if a Minecraft Window isn't found.

## Message Objects

Properties:
  > content
 
  > id
 
  > date

Content Property: Holds the content of a message. It represents exactly what the user sees, without colours.

ID Property: An unique number for the message, for the current session. This helps distinguishing between messages effectively.

Date Property: The date of when the message was sent. It follows the format from the `latest.log` file's date.

## Chat Object

Properties:
  > default_logs_path
 
  > _chat_key
 
  > _window_searchname

Methods:
  > get_history | Limit defaulted to 50**50, gets the chat messages history

  > send | Sends a message to the chat.

Default_Logs_Path Property: Can be altered, defines the location of the latest.log file. Defaults to `\.minecraft\logs\latest.log`

_Chat_Key Property: Can be altered, defines the key that triggers the text chat on minecraft. Defaults to 'T'.

_Window_SearchName: Can be altered, defines the title of the window that the Minecraft Client launches as. Defaults to "Minecraft"


### Special Thanks
```
To SafeSurvival, for being the testing ground for this project.
To Shaztopia, SafeSurvival's Owner, for allowing me to test it there.
```
