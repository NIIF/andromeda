# Andromeda

Andromeda malware domain list customized for some common used dns servers, like unbound, bind, power dns, and raw format in text.
Teh goal of this project block all andromeda activity by fake dns resolve technique.


# Philosophy:

If you choose this way: Don't forget the detection just sometimes enough, the perfect solution the remove procedure.

Recomendation: You can use this tool set, for impossible the operation of andromeda malware, but it is not enough, if you use a log analyzer(to analyze your dns queryes), 
you have the opportunity to make a perfect solution (as you can read it, is a success remove process).


* The simple text format domain list can be find in the text directory 
* * text/andromeda_black_list.txt.

# For unbound users:

Configuration requirements for unbound:

The unbound users can find the full parsed zona file ( unbound/andromeda_black_list ) in the unbound directory.

* 1, You have to pull this file the black_list folder of your unbound install directory(unbound/black_list/).
* 2, Please insert the following line into unbound.conf.
  include: "/etc/unbound/black_lists/andromeda_black_list"
* 3, After you reboot your dns service, you will ready.

# For bind users:

The bind useres can find an options file, and all of andromeda zona files.
Note: If you statisfied the SERVFAIL answer, the zone files are not nesesseries.

* The options file can be find here:
* *  bind/named.conf.andromeda
* The zone files can be find here:
* * bind/andromeda_zonafiles/

Configuration requirements:
* 1, Insert the following line into named.conf
* * include "/etc/bind/named.conf.andromeda";
* 2, Pull or download bind/named.conf.andromeda file into your /etc/bind directory.
* 3, Run the following commands.
* * mkdir /etc/bind/andromeda_zonefiles
* * chown bind:bind /etc/bind/andromeda_zonefiles
* 4, Pull or download the zone files from bind/andromeda_zonefiles/ to your /etc/bind/andromeda_zonefiles/ directory.
* 5, Reload your dns service.




