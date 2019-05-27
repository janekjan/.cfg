function config
    eval command /usr/bin/git --git-dir=$HOME/.cfg --work-tree=$HOME $argv
    set -gx PATH $PATH /opt/texlive/2019/bin/x86_64-linux/
end
