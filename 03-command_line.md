# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](https://web.archive.org/web/20160708171659/http://cli.learncodethehardway.org/book/) or [Codecademy's Learn the Command Line](https://www.codecademy.com/learn/learn-the-command-line). These are helpful tutorials. Each "chapter" focuses on a command. Type the commands you see in the _Do This_ section, and read the _You Learned This_ section. Move on to the next chapter. You should be able to go through these in a couple of hours.

---

### Q1.  Cheat Sheet of Commands  

Here's a list of items with which you should be familiar:  
* show current working directory path
* creating a directory
* deleting a directory
* creating a file using `touch` command
* deleting a file
* renaming a file
* listing hidden files
* copying a file from one directory to another

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do.  (Use the 8 items above and add a couple of your own.)  

* ls - show current working directory path
* mkdir - creating a directory
* rmdir - deleting a directory
* touch - creating a file using `touch` command
* rm - deleting a file
* mv - renaming a file
* ls -a -listing hidden files
* cp - copying a file from one directory to another
* more/less - view a file without editing
* grep - find text within a directory

---

### Q2.  List Files in Unix   

What do the following commands do:  
`ls`  
`ls -a`  
`ls -l`  
`ls -lh`  
`ls -lah`  
`ls -t`  
`ls -Glp`  

`ls`  - list files in a directory
`ls -a`  - list hidden files also
`ls -l`  - list long format including permissions
`ls -lh`  - include file size
`ls -lah`  - hidden files and file size
`ls -t`  - sort by time and date
`ls -Glp`  - list with colorized output

---

### Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

-R
-t
-d
-l
-a

---

### Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

-xargs calls a command using the STDOUT of the previous command as a list for STDIN
ex: % grep 'metis' * | xargs cksum
 

