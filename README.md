# Andromeda

Andromeda malware domain list customized for some commonly used dns servers, like unbound, bind, power dns, and raw format in text. 
The goal of this project block andromeda malware activity by fake dns resolve technique.

# Philosophy:
If you choose this way: Don't forget the interdiction just sometimes enough, the perfect solution to the success remove procedure!

Recommendation: You can use this toolset, for interdiction the operation of andromeda malware, but it is not enough, 
if you use a log analyzer(to analyze your dns queries), you have the opportunity to make a perfect solution (as you can read it, is a success remove process).

The simple text format domain list can be found in the text directory.

text/andromeda_black_list.txt.

# For unbound users:

Configuration requirements for unbound:

The unbound users can be find the full parsed zone file ( unbound/andromeda_black_list ) in the unbound directory.

* You have to pull this file the black_list folder of your unbound install directory(unbound/black_list/).
* Please insert the following line into unbound.conf. 
* * include: "/etc/unbound/black_lists/andromeda_black_list"
* After you reboot your dns service, you will ready.

# For bind users:

The bind users can be find an options file and all of Andromeda zone files. Note: If you satisfied the SERVFAIL answer, the zone files are not necessaries.

* The options file can be find here:
* * bind/named.conf.andromeda
* The zone files can be find here:
* * bind/andromeda_zonefiles/

Configuration requirements:

* Insert the following line into named.conf
* * include "/etc/bind/named.conf.andromeda";
* Pull or download bind/named.conf.andromeda file into your /etc/bind directory.
* Run the following commands.
* * mkdir /etc/bind/andromeda_zonefiles
* * chown bind:bind /etc/bind/andromeda_zonefiles
* Pull or download the zone files from bind/andromeda_zonefiles/ to your /etc/bind/andromeda_zonefiles/ directory.
* Reload your dns service.