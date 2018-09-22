# Andromeda

Andromeda malware domain list customized for some common used dns servers like unbound, bind, power dns, and raw format in text.
Teh goal of this project block all andromeda activity by fake dns resolve technique.


Philosophy: If you choose this way: Don't forget the detection just sometimes enough, the perfect solution is the remove procedure.

Recomendation: You can use this tool set for impossible the operation of andromeda malware, but it is not enough, if you use a log analyzer(analyze your dns queryes), 
you have the opportunity to make a perfect solution (as you can read it, is a success remove process).


The simple text format domain list can be find in the text directory text/andromeda_black_list.txt.

For unbound users
Configuration requirements for unbound:

For unbound users can be found the full parsed zona file in the unbound directory.

* 1, You have to pull this file the black_list folder of your unbound install directory(unbound/black_list/).
* 2, Please insert the following line into unbound.conf.
  include: "/etc/unbound/black_lists/andromeda_black_list"
* 3, You are ready





