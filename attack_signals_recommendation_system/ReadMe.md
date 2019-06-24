# Attack Signals Recommendation System

### This project has copy right ‼️

## Data Preparation
### [Data Preprocessing][8]
* As you can see in the comments, many outliers are for the majority of a certain attack types, therefore, I dind't clean the outliers, didn't normalize the data either.
* Meanwhile, <b>the main purpose</b> here is NOT to use machine learning to improve prediction accuracy, but to generate simulated cyber signals generated in real world, imagine those cyber analysists manually look into the data and create rules (signals). The data here will be used in tree model in order to create rules. So just need to find some patterns will be enough.
* <b>Learning Note</b>
  * This is a multi-class prediction problem. When you want to show confusion matrix, you need both categorical and numerical labels. To convert categorical labels to numerical ones, "factoring" is better than "label encoding", since factoring will obey the original label order, encoding won't.
  * Models like random forest in Python accepts "object" data type, but the value should be numbers. So the problem that python random forest do not like R which has "factor" data type should not exist any more.
    * However, the factorized label has to be "int64" type
### [Generate Rules][9]
* <b>Learning Notes</b>
  * Even though sklearn random forest supports object features, lime doesn't. All the features in lime has to be int or float, but you can indicate which features should be categorical
  * Xgboost also requires all the features to be int or float, but <b>also can be bool</b>. You can not indicate which features should be categorical type, but need label encoding.
  * When it comes to multi-classification problem, random forest has params easier to be tuned, faster and tend to get better results than xgboost.
  * Originally I was planning to use xgboost to generate model artifact so that I can extract rules from those trees directly, but xgboost prediction result was too bad (all predicted as normal), you need to set weights in objective function for xgboost, may resolve some problem, but this is more troublesome than random forest.
  * With each estimator of random forest, you are able to visualize the trees and find rules. All the estimators are saved as .dot files. [To find all the images and dot file][10]
### [Extract Rules][11]
* Each estimator here is too giant, with so much tree branches. What I am trying to do here is, to generate the "if...else..." code from an estimator, this makes generating the final rules much easier
### [Simulate Data][12]
* Simulate Clients' Data
  * Each client has a bunch of records, some are has the right attack type (triggered rule), some are wrong, all randomly asigned. This is trying to mimic the real work situation, when business analysts manually create rules, not all of them are right. Although the wrongly labeled percentage in this simulated is much smaller than real world data.
* Simulation for Signal Grouping
  * Each signal will have different params and settings, this part is to simulate this type of situation and trying to group similar signals based on their settings' similarities
* Simulation for Association Rules
  * To simulate the real situation when each record could get 1+ signals, with association rules, it's trying to find rules that tend to appear together, either to help group signals or to help predict attacks. 
  * To understand the metrics used in association rules:
    * Support and Confidence are min values, means the rules have at least passed the min support and min confidence
    * Lift is a measure of importance of a rule.
      * `Lift = confidence / expected_confidence = confidence / support of rule head`
      * A lift value greater than 1 indicates that the rule body and the rule head appear more often together than expected, this means that the occurrence of the rule body has a positive effect on the occurrence of the rule head.
      * A lift smaller than 1 indicates that the rule body and the rule head appear less often together than expected, this means that the occurrence of the rule body has a negative effect on the occurrence of the rule head.
      * A lift value near 1 indicates that the rule body and the rule head appear almost as often together as expected, this means that the occurrence of the rule body has almost no effect on the occurrence of the rule head.
      * [Refernece][14]
### [Recommend Signals to Clients][13]
* Recommend signals to a target client based on clients' similarities, signal ratings in each client
  * Default signal rating is normalized frequency here
  * The rating here can also be a mix of default ratings and business analytics manually adjustment, this will allow business experts to interact with machine learning algorithms, which will improve recommendation results. <b>Flexibility of expert & machine learning interaction</b>
  * From the returned results, you can also check recommendation score and decide how many (k) signals you want for the target client. Because the recommendation score could have a sharp drop.

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
* Remember to calculate of the lost of attacks, financial impact



[1]:http://kdd.ics.uci.edu/databases/kddcup99/task.html
[2]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/Data_Sources/kdd99_data_check.R
[3]:http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
[4]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/
[5]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/dataset
[6]:http://bigdata.ise.bgu.ac.il/sherlock/index.html#/download
[7]:https://datahub.io/machine-learning/kddcup99#resource-kddcup99_zip
[8]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/data_preprocessing.ipynb
[9]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/generate_rules.ipynb
[10]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/tree/master/attack_signals_recommendation_system/images
[11]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/extract_rules.ipynb
[12]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/simulate_data.ipynb
[13]:https://github.com/hanhanwu/Hanhan_Break_the_Limits/blob/master/attack_signals_recommendation_system/recommend_signals2clients.ipynb
[14]:https://www.ibm.com/support/knowledgecenter/SSEPGG_10.1.0/com.ibm.im.model.doc/c_lift_in_an_association_rule.html
