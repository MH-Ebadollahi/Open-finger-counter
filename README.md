Hand detection and open-finger counter program

This project is developed in Aug 2021 by python 3.9. It can connect to the Siemens S7-1500 as a client with TIA Portal software through OPCUA communication.

Library requirements:
OpenCV:  pip install opencv-python
 Mediapipe: pip install mediapipe
 Opcua: pip install opcua
How is working:
On the side of the TIA Portal, you have to activate the OPCUA server and copy the server address.
After greeting, the software takes the server address from the user in a special format that is noted in the example: (opc.tcp://255.255.255.255:0000)
In the next step, the software needs the NodeID of the parameter from the server, which has Int type, and data from python is stored in it. The NodeId has a special format that is noted in the example: 
(ns=3;s="DB name"."Attribute name")
String Notation
There is a string notation for NodeIds defined as part of the OPC UA XML Schema which represents a fully qualified NodeId. The format of the string is:

ns=<namespaceIndex>;<identifiertype>=<identifier>

with the fields
<namespace index>
The namespace index formatted as a base 10 number. If the index is 0, then the entire “ns=0;” clause is omitted.
<identifier type>
A flag that specifies the identifier type. The flag has the following values:
  Flag
 Identifier Type

Flag         	Identifier Type
i	NUMERIC      (UInteger)
s	STRING     (String)
g	GUID (Guid)
b	OPAQUE (ByteString)
 
 <identifier>
The identifier encoded as string. The identifier is formatted using the XML data type mapping for the identifier type. Note that the identifier may contain any non-null UTF8 character including whitespace.
Examples:
ns=2;s=”MyTemperature”




On the next step, if you are passed the previous steps correctly the client can connect to the server and use your camera for running.
