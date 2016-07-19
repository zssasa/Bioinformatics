# Bioinfomatics Data Skills

Just take some notes and get used to *Markdown* language!



## Chapter 1

1. **Reproducible** and **Robust** research

2. **Never** trust your tools or data


3. Let **Code** test 

	unit test for python
	
## Chapter2

1. Project Documentation
	* methods and workflows
	* when, where, what, how of all data
		* when: time
		* where: url, databases
		* what: version
		* how: Internet or colleague
	* version of software
2. organizing data
	* directory
	* filename, extention
3. shell expansion
	* {}
	* *
	* ()
	* []
	* ?

## Chapter3

1. Unix Philosophy: Modularity
2. Text Streams
	* stdout redirection: > or >>
	* stderr redirection: 2>
	* input redirection: <
	* pseudodevice: /dev/null
3. <font size=5>***tail***</font>: get the lat 10 lines of the file
4. Unix Pipe: |
5. <font size=5>***grep***</font>: The grep utility searches any given input files, selecting lines that match one or more patterns.

6. tee: standard output is both written to file and pip to standard input
7. background process: &
	
	foreground process: fg
8. <font size=5>***top***</font>
9. <font size=5>***ps***</font>
10. <font size=5>***kill***</font>
11. exit status: $?
12. command substitution: ${ }
13. <font size=5>***alias***</font>

## Chapter4

1. ssh
2. scp: copy files or dirs from local/remote to remote/local
	* local file --> remote :
	
	~~~bash  
	scp local_file remote_username@remote_ip:remote_folder  

	scp local_file remote_username@remote_ip:remote_file  
 
	scp local_file remote_ip:remote_folder  

	scp local_file remote_ip:remote_file
	~~~
  
	* local dir --> remote: 
	  
	~~~bash
	scp -r local_folder remote_username@remote_ip:remote_folder  
	
	scp -r local_folder remote_ip:remote_folder
	~~~

	* remote file/dir --> local:
	The same as above

3. `nohup program &` 
	
	ignore the HUP signal, so the program will not be interrupted if your terminal were to close or the remote connection were to drop
	
	Additionally, add a line `tail -f nohup.out`to follow the preocess
	
4. Tmux

	There still much work to learn about tmux
	
## Chapter5

1. Git: Need to Specify a new Note

~~~git
git config --global user.name
git config --global user.email
~~~

~~~git
git init

git clone http[s]://example.com/path/to/repo.git/
git clone ssh://example.com/path/to/repo.git/
git clone git://example.com/path/to/repo.git/
git clone /opt/git/project.git 
git clone file:///opt/git/project.git
git clone ftp[s]://example.com/path/to/repo.git/
git clone rsync://example.com/path/to/repo.git/
git clone [user@]example.com:path/to/repo.git/
~~~
通常来说，Git协议下载速度最快，SSH协议用于需要用户认证的场合

~~~git
git status

git add

git commit -m "Message"
git commit -a -m "" = git add + git commit -m
git commit --amend

git diff

git log

git mv
git rm

git reset
~~~

~~~git
git remote

git push

git fetch

git pull
~~~

~~~git
git checkout

git stash

git branch
git branch --all
git checkout
git checkout -b

git merge
~~~