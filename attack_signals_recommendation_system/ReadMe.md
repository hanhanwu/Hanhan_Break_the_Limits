# Attack Signals Recommendation System

### This project has copy right ‼️


## Potential Data Source
* [KDD 99 attacks - some features & tasks description][1]
  * [My code R - Quickly check full dataset][2]
    * [To download the data][3]
  * [The complete list of features][7]
  * Attack Types in KDD99
    * normal: non-attack
      * normal
    * Denial of Service (dos): Attacker tries to prevent legitimate users from using a service.
      * smurf, neptune, back, teardrop, pod, land
    * Remote to Local (r2l): Attacker does not have an account on the victim machine, hence tries to gain access.
      * warezclient, guess_passwd, warezmaster, imap, ftp_write, multihop, phf, spy
    * User to Root (u2r): Attacker has local access to the victim machine and tries to gain super user privileges.
      * buffer_overflow, rootkit, loadmodule, perl
    * Probe: Attacker tries to gain information about the target host.
      * satan, ipsweep, portsweep, nmap
  * The attack types can serve as signals. But this data has focus more on "user" data - the features (about 40 features), but the types of attack are limited. Testing data has new type of attacks that never appeared in training data, which can be interesting.
* [Sherlock - Smartphone Sensor Malware Data][4]
  * [Data Description][5]
  * [To get full access - Sign the agreement for 3 years license][6]
  * Different types of malware data is stored in different files, each malware type has different features. If use one-hot to put all the columns together, there will be many columns, and many empty values
  
  
## Potential Delight User Points
* In industry, there can be so many signals, based on those signals always appear together in a client/user, the recommendation system can also generate higher level signal categories, similar to "crowd sourcing".
  * The benefit is, 
* New types of attacks that never appeared in any existing "user" records, is that possible to detect?


[1]:http://kdd.ics.uci.edu/databases/kddcup99/task.html
[2]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/Data_Sources/kdd99_data_check.R
[3]:http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
[4]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/
[5]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/dataset
[6]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/download
[7]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/screenshots/41_features.PNG
