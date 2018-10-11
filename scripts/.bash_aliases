#personal_aliases

#Function to Move files to trash folder
# move_to_trash() {
#     [ ! -d ~/.Trash ] && mkdir ~/.Trash;
#     if [ "$1" == "-rf" ]; then
#        mv -t ~/.Trash ${@:2}
#     elif [ "$1" == "clean" ]; then
#         /bin/rm -rf ~/.Trash
#     else
#         mv -t ~/.Trash $@
#     fi
# }

# alias rm='move_to_trash'
alias s129='scp root@10.10.68.129:$1 .'
alias s7='f() { scp root@10.10.78.7:$1 .;}; f'
alias s129='f() { scp root@10.10.68.129:$1 .;}; f'

# res='f() { grep "Return  code is : $1" * 2>/dev/null; unset -f f;}; f'

alias tm='ssh root@10.10.78.7'
alias pkr='ssh vishal@10.3.41.3'
alias vv='sudo vpnc'
alias vt='sudo vpnc && tm'
alias vpd='sudo vpnc-disconnect'

alias chzsh='chsh -s $(which zsh)'
alias chbash='chsh -s $(which bash)'

alias rda='sudo rdesktop -g 50% -u Administrator -p Ssl12345#'
alias rdd='sudo rdesktop -g 50% -u dipankarc -p Ssl12345#'
alias rdv='sudo rdesktop -g 50% -u vishalc -p Ssl12345#'
alias rdr='sudo rdesktop -g 50% -u tester -p Ssl12345#'
alias rdt='sudo rdesktop -g 50% -u root -p Ssl12345#'

alias a='cd /home/vishalc/work/assignment'
alias emacs='emacs -nw'

alias ww='rm *~;rm *.pyc~;rm *.o~;rm a.out~;rm exe~;rm *.class'
alias s='git status'
alias l='ls -cf'
alias e='rm ~/.bash_aliases~  ~/.zshrc~ ~/.bashrc~ ~/.emacs~ ~/.profile~ ~/.screenrc~'

alias ll='ls -alF'
alias la='ls -A'
alias l='ls -CF'

alias m='alsamixer'
alias rb='sudo init 6'
alias po='sudo poweroff'

alias web='sudo ln -s $(pwd) /var/www/html'
alias gopkg='sudo ln -s $(pwd) /usr/local/gopkg/src/'
alias subl='/home/vishalc/sublime_text_3/sublime_text'

alias NetService='sudo service networking restart'

alias sw='setwwwperm'
setwwwperm(){
    sudo chmod -R 0777 /var/www/html/;
        sudo chown -R www-data:www-data /var/www/html/;
	}
#GO Environment
export GOPATH=/usr/local/gopkg
export GOROOT=/usr/local/go/
export CONDA=/home/anaconda
export PATH=$PATH:$GOROOT/bin:$GOPATH/bin:$CONDA/bin

#screen helping hand
alias sls='screen -ls'
alias slr='screen -r'

