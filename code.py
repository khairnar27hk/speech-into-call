import messagebird

clint= messagebird.client (' api-key ')

try:

msg= client.voice_message_create (' mobie number ')
 

' message ' ,


{

'voice ' : 'male'} )


except messagebird.client.errorexpection as e:

for error in e.errors:

print (' error')
