ayyMessage

##### Description

We have captured a message from bob to alice. We believe it contains sensetive information. Allice's message server runs at: . Can you find the contents of the message?

server.py, rsapubkey.pem, message.txt

##### Points

200/250

##### Flag

hackim20{digital_singatures_does_not_always_imply_authenticitaaayyy}

##### Solution

This challenge is inspired from https://blog.cryptographyengineering.com/2016/03/21/attack-of-week-apple-imessage/ . We have removed compression and changed reciept to sending the hash of the read message thus one can bruteforce the flag one byte at a time.