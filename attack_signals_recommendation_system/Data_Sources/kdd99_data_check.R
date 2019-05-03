library(data.table)
library(plyr)

path <- "[your file folder path]"  # CHANGE TO YOUR FILE FOLDER PATH
setwd(path)

# I downloaded the full dataset from http://kdd.ics.uci.edu/databases/kddcup99/kddcup99.html
kdd99_raw <- fread('kddcup.data.corrected')
summary(kdd99_raw)
head(kdd99_raw)

# check all the labels for attack type or normal, and their counts
attack_type_freq <- count(kdd99_raw, 'V42')  
attack_type_freq[order(attack_type_freq$freq),]
# V42    freq
# 20             spy.       2
# 13            perl.       3
# 14             phf.       4
# 9         multihop.       7
# 3        ftp_write.       8
# 8       loadmodule.       9
# 17         rootkit.      10
# 5             imap.      12
# 23     warezmaster.      20
# 7             land.      21
# 2  buffer_overflow.      30
# 4     guess_passwd.      53
# 15             pod.     264
# 21        teardrop.     979
# 22     warezclient.    1020
# 1             back.    2203
# 11            nmap.    2316
# 16       portsweep.   10413
# 6          ipsweep.   12481
# 18           satan.   15892
# 12          normal.  972781
# 10         neptune. 1072017
# 19           smurf. 2807886

