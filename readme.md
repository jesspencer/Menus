$:downloads jessicaspencer$ ls
Atom.app
Install Disk Creator.app
fullstack
git-2.20.1-intel-universal-mavericks.dmg
$:downloads jessicaspencer$ rm -a install disk creator.app
rm: illegal option -- a
usage: rm [-f | -i] [-dPRrvW] file ...
       unlink file
$:downloads jessicaspencer$ rm -f install disk creator.app
$:downloads jessicaspencer$ ls
Atom.app
Install Disk Creator.app
fullstack
git-2.20.1-intel-universal-mavericks.dmg
$:downloads jessicaspencer$ cd fullstack/vagrant/menuProj
$:menuProj jessicaspencer$ git init
Reinitialized existing Git repository in /Users/jessicaspencer/Downloads/fullstack/vagrant/menuProj/.git/
$:menuProj jessicaspencer$ git status 
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   webserver.py

$:menuProj jessicaspencer$ git commit -m "first commit" 

*** Please tell me who you are.

Run

  git config --global user.email "you@example.com"
  git config --global user.name "Your Name"

to set your account's default identity.
Omit --global to set the identity only in this repository.

fatal: unable to auto-detect email address (got 'jessicaspencer@$.(none)')
$:menuProj jessicaspencer$   git config --global user.email "you@example.com"
$:menuProj jessicaspencer$ git config --global user.email "jessicaspencer12@gmail.com"
$:menuProj jessicaspencer$ git config --global user.name "Jessica.E.Spencer"
$:menuProj jessicaspencer$ git status 
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   webserver.py

$:menuProj jessicaspencer$ git stage webserver.py
$:menuProj jessicaspencer$ git status
On branch master

No commits yet

Changes to be committed:
  (use "git rm --cached <file>..." to unstage)

	new file:   webserver.py

$:menuProj jessicaspencer$ git commit -m "web server file"
[master (root-commit) d3d3f27] web server file
 1 file changed, 32 insertions(+)
 create mode 100644 webserver.py
$:menuProj jessicaspencer$ git remote add origin https://github.com/js13142/menus.git
fatal: remote origin already exists.
$:menuProj jessicaspencer$ git push -u origin master
Username for 'https://github.com': js13142
Password for 'https://js13142@github.com': 
remote: Invalid username or password.
fatal: Authentication failed for 'https://github.com/js13142/menus.git/'
$:menuProj jessicaspencer$ remote origin ls
-bash: remote: command not found
$:menuProj jessicaspencer$ git init 
Reinitialized existing Git repository in /Users/jessicaspencer/Downloads/fullstack/vagrant/menuProj/.git/
$:menuProj jessicaspencer$ git remote add origin https://github.com/js13142/menus.git
fatal: remote origin already exists.
$:menuProj jessicaspencer$ git push -u origin master
Username for 'https://github.com': js13142
Password for 'https://js13142@github.com': 
Counting objects: 3, done.
Delta compression using up to 4 threads.
Compressing objects: 100% (2/2), done.
Writing objects: 100% (3/3), 660 bytes | 660.00 KiB/s, done.
Total 3 (delta 0), reused 0 (delta 0)
To https://github.com/js13142/menus.git
 * [new branch]      master -> master
Branch 'master' set up to track remote branch 'master' from 'origin'.
$:menuProj jessicaspencer$ git status
On branch master
Your branch is up to date with 'origin/master'.

nothing to commit, working tree clean
$:menuProj jessicaspencer$ git status -p
error: unknown switch `p'
usage: git status [<options>] [--] <pathspec>...

    -v, --verbose         be verbose
    -s, --short           show status concisely
    -b, --branch          show branch information
    --show-stash          show stash information
    --ahead-behind        compute full ahead/behind values
    --porcelain[=<version>]
                          machine-readable output
    --long                show status in long format (default)
    -z, --null            terminate entries with NUL
    -u, --untracked-files[=<mode>]
                          show untracked files, optional modes: all, normal, no. (Default: all)
    --ignored[=<mode>]    show ignored files, optional modes: traditional, matching, no. (Default: traditional)
    --ignore-submodules[=<when>]
                          ignore changes to submodules, optional when: all, dirty, untracked. (Default: all)
    --column[=<style>]    list untracked files in columns

$:menuProj jessicaspencer$ echo #readme readme.md

$:menuProj jessicaspencer$ ls
webserver.py
$:menuProj jessicaspencer$ vi #readme.md


readme file 
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
~                                                                               
-- INSERT --
