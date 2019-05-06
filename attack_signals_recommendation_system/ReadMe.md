# Attack Signals Recommendation System

### This project has copy right ‼️


## Potential Data Source
* [KDD 99 attacks - some features & tasks description][1]
  * [To download the data][3]
  * Even though it's UCI data, there are problems in their data description
    * They didn't list all the 41 features, and the order of the features are not correct.
    * The correct order of features in downloaded data is: `'duration', 'protocol_type', 'service', 'flag', 'src_bytes', 'dst_bytes', 'land', 'wrong_fragment',
                   'urgent', 'hot', 'num_failed_logins', 'logged_in', 'num_compromised', 'root_shell', 'su_attempted',
                   'num_root', 'num_file_creations', 'num_shells', 'num_access_files', 'num_outbound_cmds', 
                    'is_hot_login', 'is_guest_login', 'count', 'srv_count', 'serror_rate', 'srv_serror_rate',
                    'rerror_rate', 'srv_rerror_rate', 'same_srv_rate', 'diff_srv_rate', 'srv_diff_host_rate', 
                  'dst_host_count', 'dst_host_srv_count', 'dst_host_same_srv_rate', 'dst_host_diff_srv_rate',
                  'dst_host_same_src_port_rate', 'dst_host_srv_diff_host_rate', 'dst_host_serror_rate',
                  'dst_host_srv_serror_rate', 'dst_host_rerror_rate', 'dst_host_srv_rerror_rate', 'attack_type'`
     * [To check data sample][7]
  * [My code R - Quickly check full dataset][2]
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
[7]:https://datahub.io/machine-learning/kddcup99#resource-kddcup99_zip
