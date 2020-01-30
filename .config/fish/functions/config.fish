function config
    eval command /usr/bin/git --git-dir=$HOME/.cfg --work-tree=$HOME $argv
    set -gx PATH $PATH /opt/texlive/2019/bin/x86_64-linux/
    #set -gx PATH /home/janek/.local/bin/ $PATH
    set -gx -p PATH /home/janek/.local/bin
end
