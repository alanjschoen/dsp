# Learn command line

Please follow and complete the free online [Command Line Crash Course
tutorial](http://cli.learncodethehardway.org/book/). This is a great,
quick tutorial. Each "chapter" focuses on a command. Type the commands
you see in the _Do This_ section, and read the _You Learned This_
section. Move on to the next chapter. You should be able to go through
these in a couple of hours.

---

###Q1.  Cheat Sheet of Commands  

Make a cheat sheet for yourself: a list of at least **ten** commands and what they do, focused on things that are new, interesting, or otherwise worth remembering.

> > 1. du [-hs]: see size of directory contents. -h for human readable, -s for summary.
> > 2. cut: remove or isolate columns in CSV
> > 3. head/tail: get beginning or end of file
> > 4. tr: string replace 
> > 5. sort: sort lines
> > 6. uniq: get rid of repeating lines (order matters)
> > 7. find: search within directory
> > 8. grep: search files with regular expressions
> > 9. sed: regular expression operations on streams
> > 10. awk: operate on structured data with regular expressions


---

###Q2.  List Files in Unix   

What do the following commands do:  
> > - `ls`: list directory contents 
> > - `ls -a`: include hidden files
> > - `ls -l`: show results in list form
> > - `ls -lh`:  list for with readable file size
> > - `ls -lah`: list form including hidden files with readable file size
> > - `ls -t`: sort by time and date
> > - `ls -Glp`: list form with directories formatted with / and coloring


---

###Q3.  More List Files in Unix  

Explore these other [ls options](http://www.techonthenet.com/unix/basic/ls.php) and pick 5 of your favorites:

> > I picked 7.
> >
> > 1. `-L`: de-reference symbolic links
> > 2. `-m`: comma-separated list of names
> > 3. `-q`: show ? for non-printing chars
> > 4. `-R`: recurse into subdirectories
> > 5. `-u`: show file access time
> > 6. `-x`: justify as columns
> > 7. `-1:` put each file on a new line

---

###Q4.  Xargs   

What does `xargs` do? Give an example of how to use it.

> > transforms piped data into command line arguments.  Useful for commands like `rm` and `cp` that don`t accept piped input

 

